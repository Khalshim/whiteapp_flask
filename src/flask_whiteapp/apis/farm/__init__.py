from flask_restx import Api
from flask import Blueprint

from .namespace_cows import api as ns1
from .namespace_sheeps import api as ns2


blueprint = Blueprint("farm_api", __name__, url_prefix="/farm")

api = Api(
    blueprint,
    title="My Farm API",
    version="1.0",
    description="API to manage cows and sheeps"
    # All API metadatas
)

api.add_namespace(ns1, path="/barn")
api.add_namespace(ns2, path="/pen")
