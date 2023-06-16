from flask import Flask
from flask_restx import Api, Resource, fields
from lib.usercontroller import UserController

app = Flask(__name__)

info = {
    'version': '1.1',
    'title': 'XFusition',
    'description': 'For simple web api developemnt environment'
}

api = Api(app, **info)


userModel = api.model('User', {
    'id': fields.String(readonly=True, description='The User unique identifier'),
    'firstname': fields.String(required=True, description='User firstname'),
    'lastname': fields.String(required=True, description='User lastname'),
    'email': fields.String(required=True, description='User Email')
})

usersObj = UserController()
# add moc data into the UserControlller Class 
usersObj.create({'fname': 'david', 'lname': 'gupta', 'email': "dgupta@xfusion.com"})
usersObj.create({'fname': 'Raj', 'lname': 'Mcmamra', "email": "dgupta@xfusion.com"})


# create a namespace that create a certain type of group inside the swagger
unm = api.namespace('api/v4/users', description='For users specific related task')

@unm.route("")
class UsersRoute(Resource):
    def get(self):
        '''Get all the current users'''
        return usersObj.users
    
    @unm.expect(userModel)
    def post(self):
        '''Create the new users'''
        return usersObj.create(api.payload)


# _____________________________________________________________________________________________________

# ns = api.namespace('user-controller', description='For User-service')

# todo = api.model('User', {
#     'id': fields.Integer(readonly=True, description='The User unique identifier'),
#     'firstname': fields.String(required=True, description='User firstname'),
#     'lastname': fields.String(required=True, description='User lastname'),
#     'email': fields.String(required=True, description='User Email')
# })

# class TodoDAO(object):
#     def __init__(self):
#         self.counter = 0
#         self.todos = []

#     def get(self, id):
#         for todo in self.todos:
#             if todo['id'] == id:
#                 return todo
#         api.abort(404, "Todo {} doesn't exist".format(id))

#     def create(self, data):
#         todo = data
#         todo['id'] = self.counter = self.counter + 1
#         self.todos.append(todo)
#         return todo

#     def update(self, id, data):
#         todo = self.get(id)
#         todo.update(data)
#         return todo

#     def delete(self, id):
#         todo = self.get(id)
#         self.todos.remove(todo)


# DAO = TodoDAO()
# DAO.create({'task': 'Build an API'})
# DAO.create({'task': '?????'})
# DAO.create({'task': 'profit!'})


# @ns.route('/')
# class TodoList(Resource):
#     '''Shows a list of all todos, and lets you POST to add new tasks'''
#     @ns.doc('list_todos')
#     @ns.marshal_list_with(todo)
#     def get(self):
#         '''List all tasks'''
#         return DAO.todos

#     @ns.doc('create_todo')
#     @ns.expect(todo)
#     @ns.marshal_with(todo, code=201)
#     def post(self):
#         '''Create a new task'''
#         return DAO.create(api.payload), 201


# @ns.route('/<int:id>')
# @ns.response(404, 'Todo not found')
# @ns.param('id', 'The task identifier')
# class Todo(Resource):
#     '''Show a single todo item and lets you delete them'''
#     @ns.doc('get_todo')
#     @ns.marshal_with(todo)
#     def get(self, id):
#         '''Fetch a given resource'''
#         return DAO.get(id)

#     @ns.doc('delete_todo')
#     @ns.response(204, 'Todo deleted')
#     def delete(self, id):
#         '''Delete a task given its identifier'''
#         DAO.delete(id)
#         return '', 204

#     @ns.expect(todo)
#     @ns.marshal_with(todo)
#     def put(self, id):
#         '''Update a task given its identifier'''
#         return DAO.update(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)