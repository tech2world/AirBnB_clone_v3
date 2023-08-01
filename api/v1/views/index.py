#!/usr/bin/python3
"""Index view module"""

from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from flask import jsonify
from models.review import Review
from models.state import State
from models import storage
from models.user import User


@app_views.route('/status')
def get_status():
    """get the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_stats():
    """gets number of object by type"""
    objects = {
        'amenities': Amenity,
        'cities': City,
        'reviews': Review,
        'states': State,
        'users': User
    }

    results = {}
    for key, value in objects.items():
        results[key] = storage.count(value)
    return jsonify(results)


if __name__ == "__main__":
    pass
