from flask_restx import Namespace, Resource, fields

api = Namespace("cats", description="Cats related operations")

cat = api.model(
    "Cat",
    {
        "id": fields.String(required=True, description="The cat identifier"),
        "name": fields.String(required=True, description="The cat name"),
    },
)

CATS = [
    {"id": "1", "name": "Felix"},
]


@api.route("/")
class CatList(Resource):
    @api.doc("list_cats")
    @api.marshal_list_with(cat)
    def get(self):
        """List all cats"""
        return CATS


@api.route("/<id>")
@api.param("id", "The cat identifier")
@api.response(404, "Cat not found")
class Cat(Resource):
    @api.doc("get_cat")
    @api.marshal_with(cat)
    def get(self, l_id):
        """Fetch a cat given its identifier"""
        for l_cat in CATS:
            if l_cat["id"] == l_id:
                return l_cat
        api.abort(404)
