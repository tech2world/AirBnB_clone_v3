#!/usr/bin/python3
"""Flask API config file"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_app(exception):
    """
    disconnects db session
    """
    storage.close


if __name__ == '__main__':
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
