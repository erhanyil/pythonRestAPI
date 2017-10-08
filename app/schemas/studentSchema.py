from app import app
from flask_marshmallow import Marshmallow
from ..models.studentModel import studentModel 

ma = Marshmallow(app)

class studentSchema(ma.ModelSchema):
    class Meta:
        model = studentModel
        fields = ('id', 'name', 'city', 'addr', 'pin')