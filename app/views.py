from app import app, make_response, abort, render_template, request, json, jsonify
from .configs.dbConfig import db
from .orm.student_orm import student_orm

tasks = 2

'''return render_template('index.html')'''

'''GET METHODS'''


@app.route('/student', defaults={'task_id': 0})
@app.route('/student/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return student_orm.getStudent(task_id)
    # return json.dumps(self.s, default=jdefault)


'''POST METHOD'''


@app.route('/student/add', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    return student_orm.insertStudent(request.get_json(silent=True))


'''404 Error'''


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def jdefault(o):
    return o.__dict__
