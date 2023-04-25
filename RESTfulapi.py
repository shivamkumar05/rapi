from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = []

    urls = ['https://www.example1.com', 'https://www.example2.com', 'https://www.example3.com']

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            if query in link.text:
                results.append({
                    'title': link.text,
                    'url': link.get('href'),
                    'source': url
                })

    return jsonify(results)

if __name__ == '__main__':
    app.run()
