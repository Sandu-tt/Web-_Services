from flask import Flask
from flask_restful import Api
from routes.trading_routes import HealthCheck, Trade

app = Flask(__name__)
api = Api(app)

# Define routes
api.add_resource(HealthCheck, '/health')
api.add_resource(Trade, '/trade')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
