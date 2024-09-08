import flask
from flask_restful import Api
from routes.gateway_routes import HealthCheck, Proxy

app = Flask(__name__)
api = Api(app)

# Define routes
api.add_resource(HealthCheck, '/health')
api.add_resource(Proxy, '/<string:service>/<path:endpoint>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
