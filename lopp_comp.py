from unicodedata import name


name = "name"
password = "password"
role = "role"
user = 1
allowed_m = ['admin', 'user']
users = [{name: '123', password: 'admin', role: "root"},
         {name: '456', password: 'user', role: "root"},
         {name: '456', password: 'user', role: "user"},
         {name: '789', password: 'user', role: "super"},
         {name: '000', password: 'user', role: "admin"}]

item={k:v for k,v in users[user].items() if allowed_m in [name, password, role]}
# print(item)
# print(users[user].items() )

is_user=[u for u in users if u[role]=='root']
valid_users="user" in [u[role] for u in users]
print(is_user)
print(valid_users)