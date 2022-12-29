from flask import *

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ctfvgbuuniug gedrugi;reugn"

    from .view import views

    app.register_blueprint(views,url_prefix="/")



    return app