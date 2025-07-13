# youtube-analytics-dashboard
# 📊 YouTube Analytics Dashboard

A smart and elegant dashboard that allows users to search for any news topic and receive the **top-viewed YouTube videos** and **most-read articles** related to that topic. Designed for data-driven insights with a clean and responsive UI.

---

## 🚀 Features

- 🔍 **Topic Search:** Enter any news topic to get real-time related data.
- 📺 **Top YouTube Videos:** Fetches top-viewed videos related to the topic using the YouTube Data API.
- 📰 **Top News Articles:** Retrieves most-read articles (e.g., via News API).
- 🧠 **Summarization:** Short summaries of news articles for quick reading (optional feature).
- 📈 **Responsive Dashboard:** Interactive and intuitive interface built for performance.

---

## 🛠️ Tech Stack

| Layer           | Technology               |
|----------------|---------------------------|
| Backend         | Python, FastAPI / Django  |
| Frontend        | HTML, CSS, JavaScript     |
| External APIs   | YouTube Data API, News API|
| Summarization   | NLP (TextRank / GPT APIs) |
| Hosting         | (e.g., Vercel / Render)   |

---

## 📷 Screenshots

> Add screenshots into a folder named `screenshots/` and reference them below

```
![Search Page](screenshots/search-page.png)
![Results Page](screenshots/results-page.png)
```

---

## 🔑 API Keys Required

To run this project, you will need:

- **YouTube Data API v3 Key**
- **News API Key** (e.g., https://newsapi.org)

Create a `.env` file in the root directory and add your keys:

```
YOUTUBE_API_KEY=your_youtube_api_key
NEWS_API_KEY=your_news_api_key
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/harsha151/youtube-analytics-dashboard.git
cd youtube-analytics-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file with your API keys as shown above.

### 4. Run the application

If using **FastAPI**:

```bash
uvicorn main:app --reload
```

If using **Django**:

```bash
python manage.py runserver
```

---

## 🧠 Future Improvements

- [ ] Add user login and profiles
- [ ] Store and view search history
- [ ] Enable dark/light theme toggle
- [ ] Advanced NLP summarization (e.g., OpenAI or BART)
- [ ] Multilingual support
- [ ] Deploy live version (e.g., on Vercel / AWS)

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome!

1. Fork the project
2. Create your branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> **Made with ❤️ by [Harsha Vardhana](https://github.com/harsha151)**
