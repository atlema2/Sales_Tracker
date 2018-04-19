#!/home/patrick/Programming/Sales_Tracker/bin/python3
from flask import Flask, jsonify, request
import requests
from store_requests import store_requests

app = Flask(__name__)


@app.route('/api/v1.0/<string:store>', methods=['GET'])


def show_products(store):
    store = store.lower()
    all_args = dict(request.args.lists())

    return jsonify(store_requests.get_json(store))

if __name__ == '__main__':
    app.run(debug=True)