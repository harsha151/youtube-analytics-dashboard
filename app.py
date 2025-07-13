from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/youtube'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize YouTube Data API
api_key = 'AIzaSyDbbJ2mhYTojAq85MHt5H6OMP38bppsrCM'
youtube = build('youtube', 'v3', developerKey=api_key)

class VideoStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    view_count = db.Column(db.Integer)
    like_count = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, video_id, title, view_count, like_count, comment_count):
        self.video_id = video_id
        self.title = title
        self.view_count = view_count
        self.like_count = like_count
        self.comment_count = comment_count

def get_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            p = parse_qs(parsed_url.query)
            return p['v'][0]
        if parsed_url.path[:7] == '/embed/':
            return parsed_url.path.split('/')[2]
        if parsed_url.path[:3] == '/v/':
            return parsed_url.path.split('/')[2]
    return None

def fetch_video_stats(video_id):
    request = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    )
    response = request.execute()
    if response['items']:
        item = response['items'][0]
        title = item['snippet']['title']
        stats = item['statistics']
        return {
            'title': title,
            'view_count': int(stats.get('viewCount', 0)),
            'like_count': int(stats.get('likeCount', 0)),
            'comment_count': int(stats.get('commentCount', 0))
        }
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    video_stats = None
    estimated_earnings = 0
    
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        video_id = get_video_id(youtube_url)
        if video_id:
            stats = fetch_video_stats(video_id)
            if stats:
                # Calculate estimated earnings (assuming $4 CPM)
                estimated_earnings = (stats['view_count'] / 1000) * 4
                
                new_entry = VideoStats(
                    video_id=video_id,
                    title=stats['title'],
                    view_count=stats['view_count'],
                    like_count=stats['like_count'],
                    comment_count=stats['comment_count']
                )
                db.session.add(new_entry)
                db.session.commit()
                
                video_stats = {
                    'title': stats['title'],
                    'view_count': stats['view_count'],
                    'like_count': stats['like_count'],
                    'comment_count': stats['comment_count'],
                    'video_id': video_id
                }
    
    return render_template('user_interface.html', 
                         video_stats=video_stats,
                         estimated_earnings=estimated_earnings)

@app.route('/admin')
def admin():
    # Retrieve the current page number from the query parameters; default to 1
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Define the number of items per page

    # Paginate the query
    pagination = db.paginate(
        db.select(VideoStats).order_by(VideoStats.recorded_at.desc()),
        page=page,
        per_page=per_page,
        error_out=False
    )

    # Retrieve the items for the current page
    videos = pagination.items

    # Define the local timezone
    local_tz = pytz.timezone('Asia/Kolkata')

    # Convert the recorded_at timestamps to the local timezone
    for video in videos:
        utc_time = video.recorded_at.replace(tzinfo=pytz.utc)
        video.recorded_at = utc_time.astimezone(local_tz)

    # Render the template with the paginated videos and pagination object
    return render_template('admin.html', videos=videos, pagination=pagination)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
