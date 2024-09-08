from flask import request, jsonify
from flask_restful import Resource
import requests

class HealthCheck(Resource):
    def get(self):
        return jsonify({"status": "API Gateway is running"})

class Proxy(Resource):
    def get(self, service, endpoint):
        # Define service URLs
        services = {
            'trading': 'http://trading-service:5001',
            'wallet': 'http://wallet-service:5002',
            'account': 'http://account-service:5003',
            'notification': 'http://notification-service:5004',
        }

        service_url = services.get(service)
        if not service_url:
            return {"message": "Service not found"}, 404

        # Construct the full URL
        url = f"{service_url}/{endpoint}"

        # Forward the GET request
        response = requests.get(url, params=request.args)
        return (response.json(), response.status_code)

    def post(self, service, endpoint):
        services = {
            'trading': 'http://trading-service:5001',
            'wallet': 'http://wallet-service:5002',
            'account': 'http://account-service:5003',
            'notification': 'http://notification-service:5004',
        }

        service_url = services.get(service)
        if not service_url:
            return {"message": "Service not found"}, 404

        url = f"{service_url}/{endpoint}"

        # Forward the POST request
        response = requests.post(url, json=request.json)
        return (response.json(), response.status_code)
