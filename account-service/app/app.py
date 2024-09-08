from flask import Flask
from flask_restful import Api
from routes.user_routes import HealthCheck, User

app = Flask(__name__)
api = Api(app)

# Define routes
api.add_resource(HealthCheck, '/health')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
