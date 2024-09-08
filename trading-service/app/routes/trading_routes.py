from flask import request, jsonify
from flask_restful import Resource

class HealthCheck(Resource):
    def get(self):
        return jsonify({"status": "Trading Service is running"})

class Trade(Resource):
    def post(self):
        data = request.json
        # Mock trade processing
        trade_id = "T123456"
        return jsonify({"message": "Trade executed", "trade_id": trade_id}), 201
