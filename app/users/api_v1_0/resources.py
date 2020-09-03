from flask import request, Blueprint
from flask_restful import Api, Resource
from .schemas import UserSchema
from ..models import User
from flask_jwt_extended import jwt_required

user_v1_0_bp = Blueprint('user_v1_0_bp', __name__)

user_schema = UserSchema()

api = Api(user_v1_0_bp)

class UserListResource(Resource):
	@jwt_required
	def get(self):
		users = User.get_all()
		result = user_schema.dump(users, many=True)
		return result

	@jwt_required
	def post(self):
		data = request.get_json()
		user_check = user_schema.load(data)
		film = User(name=user_check['name'],
			lastname=user_check['lastname'],
			birthday=user_check['birthday'],
			email=user_check['email'],
			username=user_check['username'],
			password=user_check['password'],
			direction=user_check['direction']
		)
		film.set_password(user_check['password'])
		film.save()
		resp = user_schema.dump(film)
		return resp, 201

class UserResource(Resource):
	@jwt_required
	def get(self, user_id):
		user = User.get_by_id(user_id)
		resp = user_schema.dump(user)
		return resp

api.add_resource(UserListResource, '/api/v1.0/users/', endpoint='user_list_resource')
api.add_resource(UserResource, '/api/v1.0/users/<int:user_id>', endpoint='user_resource')