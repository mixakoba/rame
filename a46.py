# from flask import Flask

# app=Flask(__name__)

# @app.route("/calculate/<int:x>/<string:operation>/<int:y>")
# def calculator(x,operation,y):
#     res=None
#     if operation =="+":
#         res=x+y
#     elif operation =="-":
#         res=x-y
#     elif operation =="/":
#         res=x/y
#         if y!=0:
#             res=x/y
#         else:
#             return "<h2>Error:division by zero</h2>"
#     elif operation == "*":
#         res=x*y
#     if res is None:
#         return "<h2>Error:Invalid arguments</h2>"
#     return f"<h2>{res}</h2>"

# if "__main__"==__name__:
#     app.run(debug=True)

# from flask import Flask

# app=Flask(__name__)
# users=[]
# class ID:
#     id =0
# @app.route("/")
# def main_page():
#     return "<h2>You are on main page</h2>"
# @app.route("/register/<string:username>/<string:password>")
# def register(username,password):
#     ID.id +=1
#     users.append(
#         {"id":ID.id,"username":username, "password":password}
#             )
#     return f"<h2>{users}</h2>"
# @app.route("/user/<int:id>")
# def get_user(id):
#     for user in users:
#         for key in user:
#             if user[key]==id:
#                 return f"{user}"
#     return "<h2>user not found</h2>"

# if "__main__"==__name__:
#     app.run(debug=True)
import json
class User:
    def __init__(self,file_name):
        self.file_name=file_name
        self.data=self.load()
        self.users=self.data
    
    def load(self):
        try:
            with open(self.file_name,"r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def add_user(self,username,password):
        obj={"username":username,"password":password}
        self.users.append(obj)
        self.save()
        return obj

    def save(self):
        with open(self.file_name,"r+") as f:
            json.dump(self.users,f,indent=4)