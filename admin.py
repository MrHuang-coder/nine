from user import User
class Privileges():
    privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print("You have permission" + str(self.privileges))

class Admin(User):
    privileges = Privileges()

