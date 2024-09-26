from flask import Flask, Blueprint
from waitress import serve
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Create a Blueprint with a URL prefix
my_app_bp = Blueprint('my_app', __name__, url_prefix='/my-app')

@my_app_bp.route('/')
def index():
    app.logger.info('Index page accessed')
    return 'Hello, world!'

# Register the Blueprint with the Flask app
app.register_blueprint(my_app_bp)

mode = 'dev'  # Change to 'dev' for development mode

if __name__ == '__main__':
    if mode == 'dev':
        app.logger.info("Running in production mode")
        serve(app, host='0.0.0.0', port=8080, threads=2)
    else:
        app.run(debug=True, host='0.0.0.0', port=8080)
