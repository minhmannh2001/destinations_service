from flask import jsonify
from flask_jwt_extended import jwt_required


@jwt_required()
def test():
    return jsonify({"msg": "Successfully"})
