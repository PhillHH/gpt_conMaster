from flask import Flask
from routes.chat_routes import chat_bp
from models.db_init import db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.register_blueprint(chat_bp)
env = os.getenv('FLASK_ENV', 'default')
app.config.from_object(config[env])

db.init_app(app)  
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)