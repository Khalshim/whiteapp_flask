from flask_restx import Namespace, Resource, fields

api = Namespace("cows", description="Cows related operations")

cow = api.model(
    "Cow",
    {
        "id": fields.String(required=True, description="The cow identifier"),
        "name": fields.String(required=True, description="The cow name"),
    },
)

COWS = [
    {"id": "1", "name": "Marguerite"},
]


@api.route("/")
class CowList(Resource):
    @api.doc("list_cows")
    @api.marshal_list_with(cow)
    def get(self):
        """List all cows"""
        return COWS


@api.route("/<id>")
@api.param("id", "The cow identifier")
@api.response(404, "Cow not found")
class Cow(Resource):
    @api.doc("get_cow")
    @api.marshal_with(cow)
    def get(self, id):
        """Fetch a cow given its identifier"""
        for cow in COWS:
            if cow["id"] == id:
                return cow
        api.abort(404)
