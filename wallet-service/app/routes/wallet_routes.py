from flask import request, jsonify
from flask_restful import Resource

class HealthCheck(Resource):
    def get(self):
        return jsonify({"status": "Wallet Service is running"})

class Wallet(Resource):
    def get(self):
        # Mock wallet retrieval
        wallet_id = "W123456"
        balance = 1000.0
        return jsonify({"wallet_id": wallet_id, "balance": balance})

    def post(self):
        data = request.json
        # Mock wallet creation
        wallet_id = "W654321"
        return jsonify({"message": "Wallet created", "wallet_id": wallet_id}), 201
