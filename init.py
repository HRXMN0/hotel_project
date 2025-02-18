from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Load configuration from a config file or object

    # Initialize database
    db.init_app(app)

    # Register routes (blueprints)
    with app.app_context():
        from routes import main_routes
        app.register_blueprint(main_routes)

        # Create database tables if not already created
        db.create_all()

    return app

