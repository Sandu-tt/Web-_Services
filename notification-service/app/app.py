from flask import Flask
from flask_restful import Api
from routes.notification_routes import HealthCheck, Notify

app = Flask(__name__)
api = Api(app)

# Define routes
api.add_resource(HealthCheck, '/health')
api.add_resource(Notify, '/notify')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
