from flask import Flask

# from .apis import blueprint as api
from .apis.farm import blueprint as bp_farm
from .apis.shelter import blueprint as bp_shelter

from werkzeug.middleware.proxy_fix import ProxyFix


def create_app():
    app = Flask(__name__)
    bp_farm.register_blueprint(bp_shelter)  # Example for nested blueprint
    app.register_blueprint(bp_farm)
    # app.register_blueprint(bp_shelter)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    return app


if __name__ == "__main__":
    # app.run(debug=True)
    app = create_app()
    app.run(Debug=True)
