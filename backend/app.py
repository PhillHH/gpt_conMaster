from flask import Flask
from config import Config
from backend.models import db
from backend.routes import auth_bp, post_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(post_bp, url_prefix='/posts')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()