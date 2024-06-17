from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///shop.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

class Nigger(db.Model):
    id=db.Column(db.Integer,primary_key = True)
    name=db.Column(db.String(100))
    price=db.Column(db.Integer)

if "__main__"==__name__:
    with app.app_context():
        db.create_all()
        session=db.session
        nigger=Nigger(name="levan",price=1)
        session.add(nigger)
        session.commit()