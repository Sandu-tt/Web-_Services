from flask import request, jsonify
from flask_restful import Resource

class HealthCheck(Resource):
    def get(self):
        return jsonify({"status": "Notification Service is running"})

class Notify(Resource):
    def post(self):
        data = request.json
        # Mock notification sending
        notification_id = "N123456"
        return jsonify({"message": "Notification sent", "notification_id": notification_id}), 201
