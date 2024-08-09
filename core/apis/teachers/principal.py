from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from core.libs import assertions
from .schema import TeacherSchema

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p: decorators.AuthPrincipal):
    assertions.assert_auth(p.principal_id is not None)
    
    """List all teachers"""
    teachers = Teacher.query.all()
    teachers_dump = TeacherSchema.dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)