from unicodedata import name


name = "name"
password = "password"
role = "role"
user = 1
_id = "id"
allowed_m = ['admin', 'USER']
groups = [{_id: "1", name: "g1", role: "admin"}, {
    _id: "2", name: "g2", role: "user"}, {_id: "3", name: "g3", role: "user"}]
users = [{name: '123', password: 'admin', role: "root"},
         {name: '456', password: 'user', role: "root"},
         {name: '456', password: 'user', role: "user"},
         {name: '789', password: 'user', role: "super"},
         {name: '000', password: 'user', role: "admin"}]

item = {k: v for k, v in users[user].items() if allowed_m in [
    name, password, role]}
# print(item)
# print(users[user].items() )

is_user = [u for u in users if u[role] == 'root']
valid_users = "user" in [u[role] for u in users]
# print(is_user)
# print(valid_users)


sample = [{"_id": {"$oid": "6288de3d2a2a26dd0670e3a6"}, "username": "adminsuper", "email": "adminsuper@example.com",
           "role": {"role": "USER"}, "groups": [],
           "disbaled":"false", "verified":"false", "created_at":"2022-05-21 17:22:22.763989", "updated_at":"2022-05-21 17:22:22.763989", "id":"aa63178900555ef1ac0d80977af5b216", "salt":"$2b$12$T0OLMzBYUXCIgBhY9IObRu",
           "hashed_password":"$2b$12$r.KSANQGG/.pSB5fwG8VDe/DKVUYknAmt1.gkBP0TaZYIX1C1rRDO"},

          {"_id": {"$oid": "6288de3d2a2a26dd0670e3a6"}, "username": "adminsuper", "email": "adminsuper@example.com",
           "role": {"role": "ADMIN"}, "groups": [], "disbaled":"false", "verified":"false",
           "created_at":"2022-05-21 17:22:22.763989", "updated_at":"2022-05-21 17:22:22.763989",
           "id":"aa63178900555ef1ac0d80977af5b216", "salt":"$2b$12$T0OLMzBYUXCIgBhY9IObRu",
           "hashed_password":"$2b$12$r.KSANQGG/.pSB5fwG8VDe/DKVUYknAmt1.gkBP0TaZYIX1C1rRDO"}]
v=[v for v in sample if v['role']['role'] in allowed_m]
l=lambda d: d.get('id', 'default value'), v
# print(l)