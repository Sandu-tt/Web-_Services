from flask import Flask, request
from flask_restful import Api
from routes.logging_routes import HealthCheck, LogEntry

app = Flask(__name__)
api = Api(app)

# Define routes
api.add_resource(HealthCheck, '/health')
api.add_resource(LogEntry, '/log')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
