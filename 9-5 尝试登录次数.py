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

user = User('huang', 'haitao', 'cool', '178')
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)