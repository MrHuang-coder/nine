class User:
    def __init__(self, first_name, last_name, looks, height):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.looks = looks
        self.height = height

    def describe_user(self):
        print("%s的长相%s身高%s" % (self.full_name.title(), self.looks, self.height))

    def greet_user(self):
        print("Hello %s" % self.full_name.title())

user_one = User('huang', 'haitao', 'cool', '178')
user_one.describe_user()
user_one.greet_user()

user_two = User('deng', 'jia', 'beauty', '160')
user_one.describe_user()
user_two.greet_user()