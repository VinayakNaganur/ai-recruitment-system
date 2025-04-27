from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate
from flask_mail import Mail
from pymongo import MongoClient
from .config import Config

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()
sess = Session()
mail = Mail()

# Initialize MongoDB client
mongo_client = MongoClient('mongodb://localhost:27017/')
mongodb = mongo_client['applications']
applications_collection = mongodb['applications']

def create_app():
    # Create Flask app instance
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize SQLAlchemy, Flask-Migrate, Session, Mail
    db.init_app(app)
    migrate.init_app(app, db)
    sess.init_app(app)

    # Flask-Mail Configuration (Optional, if using Mail)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = '   '      # <- Put your sender email here
    app.config['MAIL_PASSWORD'] = '   '  # <- Use Gmail app password
    
    mail.init_app(app)

    # Register Blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
