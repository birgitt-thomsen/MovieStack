""" This module handles all requests and queries tied to flask routes."""
from flask import Flask

app = Flask(__name__)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)