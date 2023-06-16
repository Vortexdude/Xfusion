import uuid

class UserController(object):
    def __init__(self):
        self.users = []

    def create(self, data: dict):
        if not 'id' in data:
            id = str(uuid.uuid4())
            data['id'] = id
        self.users.append(data)
        return self.users

    def get(self, id):
        for user in self.users:
            if user[id] == id:
                return user
            else:
                return {"message": "Perticullar user not found inthe database"}

    def update(self, data):
        id = data['id']
        newdata = self.get[id]
        newdata.update(data)
        return newdata

    def delete(self, id):
        self.users.pop[id]
        return {"message": "User Updated succesfully!"}