from flask import request, Blueprint
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt
from werkzeug import datastructures, utils
import os
import uuid

from .schemas import DocumentsSchema
from ..models import Documents
from config.default import UPLOAD_FOLDER

documents_v1_0_bp = Blueprint('documents_v1_0_bp', __name__)

documents_schema = DocumentsSchema()

api = Api(documents_v1_0_bp)


class DocumentsListResource(Resource):
    @jwt_required()
    def get(self):
        doc = Documents.get_all()
        result = documents_schema.dump(doc, many=True)
        return result

    @jwt_required()
    def post(self):
        current_user = get_jwt()
        random_uuid = uuid.uuid4()
        parser = reqparse.RequestParser()
        parser.add_argument('document', help="File required",
                            required=True, location='files', type=datastructures.FileStorage)
        args = parser.parse_args()
        document = args['document']

        file_name = utils.secure_filename(document.filename)
        name_file = str(random_uuid)+"."+file_name.split(".")[1]
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER, name_file)
        doc = Documents(
            url=name_file,
            name=file_name,
            user_id=current_user["user_id"]
        )
        if doc.get_by_name() is None:
            doc.save()
            document.save(file_path)
            doc.get_stats_coincidence()
            # response = documents_schema.dump(doc)
            return {"msg": "ok"}, 201
        else:
            return {"message": {"document": f"Documents {file_name} already exist"}}, 400


class TestDocuments(Resource):
    def get(self):
        doc = Documents(
            url="1b5078c4-8451-43e1-a244-28a88811049b.pdf",
            name="test.pdf",
            id=1)
        doc.get_stats_coincidence()


api.add_resource(DocumentsListResource,
                 '/api/v1.0/documents/', endpoint='documents_list_resource')
api.add_resource(TestDocuments,
                 '/api/v1.0/test/', endpoint='test')
