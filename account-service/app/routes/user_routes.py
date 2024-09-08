from flask import request, jsonify
from flask_restful import Resource

class HealthCheck(Resource):
    def get(self):
        return jsonify({"status": "Account Service is running"})

class User(Resource):
    def get(self, user_id=None):
        # Mock user retrieval
        user = {
            "user_id": "U123456",
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
        return jsonify(user)

    def post(self):
        data = request.json
        # Mock user creation
        user_id = "U654321"
        return jsonify({"message": "User created", "user_id": user_id}), 201
