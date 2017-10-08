from sqlalchemy.sql.expression import null

from app import jsonify
from app.models.taskModel import taskModel
from ..configs.dbConfig import db
from ..models.studentModel import studentModel
from ..schemas.studentSchema import studentSchema

class student_orm:
    def getStudent(id=0):
        student_schema = studentSchema(many=True)
        if id > 0:
            allDatas = studentModel.query.filter(studentModel.id == id).all()
        else:
            allDatas = studentModel.query.all()
        result = student_schema.dump(allDatas)
        return jsonify({'data': result.data})

    def insertStudent(newStudent):
        student_schema = studentSchema(many=True)
        studentModel.student = newStudent
        db.session.add(studentModel(student=newStudent))
        return jsonify({'data': 1 if db.session.commit() is null else 0})
