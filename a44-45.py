from flask import Flask

app=Flask(__name__)

@app.route("/calculator/<int:x>/<string:operation>/<int:y>")
def calculator(x,operation,y):
    res=None
    if operation =="+":
        res=x+y
    elif operation=="-":
        res=x-y
    elif operation=="*":
        res=x*y
    elif operation=="/":
        res=x/y
    else:
        return"<h2>error:division by zero</h2>"
    if res is None:
        return "<h2>Error:Invalid Arguments</h2>"

if "__main__"==__name__:
    app.run(debug=True)