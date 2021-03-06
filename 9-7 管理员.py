class User:
    def __init__(self, first_name, last_name, looks, height):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.looks = looks
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        print("%s的长相%s身高%s" % (self.full_name.title(), self.looks, self.height))

    def greet_user(self):
        print("Hello %s" % self.full_name.title())
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print("You have permission" + str(self.privileges))

admin = Admin('huang', 'haitao', 'cool', '178')
admin.show_privileges()
