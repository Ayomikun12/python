from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ayomikun'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .auth import auth

    # Register blueprints with no overlapping prefixes
    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app



# from flask import Flask

# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'ayomikun'

#     from .views import views
#     from .auth import auth

#     app.register_blueprint(views, url_prefix='/')
#     app.register_blueprint(auth, url_prefix='/')

#     return app