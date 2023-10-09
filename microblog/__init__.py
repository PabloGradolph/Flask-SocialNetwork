from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(test_config=None):
    app = Flask(__name__)

    # A secret for signing session cookies
    app.config["SECRET_KEY"] = "93220d9b340cf9a6c39bac99cce7daf220167498f91fa"

    # Database config
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://24_webapp_031:dGlvdf65@mysql.lab.it.uc3m.es/24_webapp_031a"
    db.init_app(app)

    # In order to work with sqlite.
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///microblog.db"

    # Register blueprints
    # (we import main from here to avoid circular imports in the next lab)
    from . import main
    from . import auth

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    return app
