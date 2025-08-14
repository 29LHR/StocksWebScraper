from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

tickers = ["aapl", "msft", "goog", "meta"]

def get_data(ticker: str):
    url = f"https://stockanalysis.com/stocks/{ticker.lower()}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = bs(response.text, "html.parser")

    main = soup.find('main')
    number = main.findChild('div')
    number = number.findChild('div', class_ = 'mb-5 flex flex-row items-end space-x-2 xs:space-x-3 bp:space-x-5')
    number = number.findChild('div')
    number = number.findChild('div')
    number = list(number)
    
    data = {}
    data['At Close'] = float(number[0])

    for row in soup.select("table tr"):
        cols = row.find_all("td")
        if len(cols) == 2:
            key = cols[0].get_text(strip=True)
            value = cols[1].get_text(strip=True)
            data[key] = value
    return data

@app.route('/')
def home():
    return render_template("home.html", tickers=tickers)

@app.route('/<ticker>')
def stockPage(ticker: str):
    data = get_data(ticker)
    return render_template('stock.html', ticker=ticker.upper(), data=data)

@app.route('/<ticker>/api')
def stockAPI(ticker : str):
    return get_data(ticker)

@app.route('/redirect/ts', methods=["POST"])
def redirectF():
    ticker = request.form["tickerIn"]
    return redirect(url_for('stockPage', ticker=ticker))

if __name__ == '__main__':
    app.run(debug=True)