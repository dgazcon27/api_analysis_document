from flask import request, Blueprint, jsonify
from flask_restful import Api, Resource
from .schemas import AuthSchema
from ..models import Auth
from app.users.models import User
from app.common.error_handling import ObjectNotFound
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
import datetime

auth_v1_0_bp = Blueprint('auth_v1_0_bp', __name__)

auth_schema = AuthSchema()

api = Api(auth_v1_0_bp)


class AuthListResource(Resource):
    def post(self):
        data = request.get_json()
        user = User.get_user(data['username'])
        if user:
            check = user.check_password(data['password'])
            if check:
                additional_claims = {"user_id": user.id}
                access_token = create_access_token(
                    identity=user.username,
                    additional_claims=additional_claims)
                auth = Auth(token=access_token, user_id=user.id)
                auth.save()
                res = auth_schema.dump(auth)
                return res, 201
            else:
                return {"msg": "Password incorrect"}, 404
        else:
            return ObjectNotFound(f"User {data['username']} doesn't exist"), 404

    def get(self):
        print("hello")
        data = request.get_json()
        # print(data)
        pass


class AuthResource(Resource):
    def post(self):
        data = request.get_json()
        schema_auth = auth_schema.load(data)
        auth = Auth.get_by_token(schema_auth['token'])
        if auth:
            user = User.get_by_id(auth.user_id)
            access_token = create_access_token(user.username)
            auth.token = access_token
            auth.save()
            res = auth_schema.dump(auth)
            return res, 201
        else:
            raise ObjectNotFound("invalid authorization token")


class AuthCurrent(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        user = User.get_by_id(current_user["user_id"])
        data = {
            "name": user.name,
            "lastname": user.lastname,
            "email": user.email,
            "direction": user.direction
        }
        return data, 200


api.add_resource(AuthResource, '/api/v1.0/auth/refresh',
                 endpoint='user_resource')
api.add_resource(AuthListResource, '/api/v1.0/auth/',
                 endpoint='auth_list_resource')
api.add_resource(AuthCurrent, '/api/v1.0/auth/current',
                 endpoint='auth_current')
