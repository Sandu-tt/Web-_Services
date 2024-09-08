from flask import request, jsonify
from flask_restful import Resource

class HealthCheck(Resource):
    def get(self):
        return jsonify({"status": "Centralized Logging Service is running"})

class LogEntry(Resource):
    def post(self):
        data = request.json
        # Mock log entry processing
        log_id = "L123456"
        return jsonify({"message": "Log entry received", "log_id": log_id}), 201
