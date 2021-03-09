from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()
