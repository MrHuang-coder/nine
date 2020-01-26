from user import User
from admin import Admin, Privileges

admin_one = Admin('huang', 'haitao', 'cool', '178')
admin_one.privileges.show_privileges()
