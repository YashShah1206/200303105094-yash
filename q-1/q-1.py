from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/numbers')
def get_numbers():
    urls = request.args.getlist('url')

    numbers = set()

    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            if response.ok:
                data = response.json()
                numbers.update(data['numbers'])
        except (requests.exceptions.Timeout, requests.exceptions.RequestException):
            pass

    sorted_numbers = sorted(numbers)
    result = {'numbers': sorted_numbers}

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8008)
