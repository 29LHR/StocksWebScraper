The Base of a Python Web Scraper to Scrape Stocks off of the Internet.

Runs a Flask app which can be opened in a browser however there is currently no CSS
Uses requests and Beautiful Soup to Scrap stockanalysis.com

# 📈 Stocks Web Scraper

A Python-based web scraper that pulls real-time stock data from the internet and displays it through a simple Flask web application.

## 🚀 Features
- Scrapes stock data from [stockanalysis.com](https://stockanalysis.com) using **Requests** and **BeautifulSoup**.
- Runs a **Flask** web server to view results in your browser.
- Lightweight and easy to set up.
- Open for customization (currently no CSS styling).

## 🛠️ Requirements
Make sure you have Python 3 installed, then install the dependencies:

```bash
pip install -r requirements.txt
```

**Dependencies:**
- Flask
- requests
- beautifulsoup4

## 📦 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/StocksWebScraper.git
   cd StocksWebScraper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## 🎯 Roadmap
- [ ] Add CSS styling for better UI.
- [ ] Add search and filter functionality.
- [ ] Enable scraping from multiple sources.

## 📜 License
This project is licensed under the MIT License.