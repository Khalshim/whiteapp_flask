from flask_restx import Api
from flask import Blueprint

from .namespace_cats import api as ns1
from .namespace_dogs import api as ns2


blueprint = Blueprint("shelter_api", __name__, url_prefix="/shelter")

api = Api(
    blueprint,
    title="My shelter API",
    version="1.0",
    description="API to manage cats and dogs"
    # All API metadatas
)

api.add_namespace(ns1, path="/litiere")
api.add_namespace(ns2, path="/chenil")
