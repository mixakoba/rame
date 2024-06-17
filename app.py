from flask import Flask
from a46 import User

app=Flask(__name__)
user=User("users.json")

@app.route("/register/<string:username>/<string:password>")
def register(username,password):
    created_user=user.add_user(username,password)
    return f"<h2>{created_user}</h2>"

if "__main__"==__name__:
    app.run(debug=True)