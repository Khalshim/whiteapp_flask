from flask_restx import Namespace, Resource, fields

api = Namespace("sheeps", description="Sheeps related operations")

sheep = api.model(
    "Sheep",
    {
        "id": fields.String(required=True, description="The sheep identifier"),
        "name": fields.String(required=True, description="The sheep name"),
    },
)

SHEEPS = [
    {"id": "1", "name": "Bouclette"},
]


@api.route("/")
class SheepList(Resource):
    @api.doc("list_sheeps")
    @api.marshal_list_with(sheep)
    def get(self):
        """List all sheeps"""
        return SHEEPS


@api.route("/<id>")
@api.param("id", "The sheep identifier")
@api.response(404, "Sheep not found")
class Sheep(Resource):
    @api.doc("get_sheep")
    @api.marshal_with(sheep)
    def get(self, l_id):
        """Fetch a sheep given its identifier"""
        for l_sheep in SHEEPS:
            if l_sheep["id"] == l_id:
                return l_sheep
        api.abort(404)
