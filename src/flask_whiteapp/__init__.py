from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

# from .apis import blueprint as api
from .apis.farm import blueprint as bp_farm
from .apis.shelter import blueprint as bp_shelter


def create_app():
    _app = Flask(__name__)
    bp_farm.register_blueprint(bp_shelter)  # Example for nested blueprint
    _app.register_blueprint(bp_farm)
    # app.register_blueprint(bp_shelter)
    _app.wsgi_app = ProxyFix(_app.wsgi_app)
    return _app


if __name__ == "__main__":
    # app.run(debug=True)
    app = create_app()
    app.run(Debug=True)
