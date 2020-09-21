from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

cors = CORS()

def create_app():
    app = Flask(__name__)

    cors.init_app(app)

    from .routes import api
    app.register_blueprint(api)

    return app
