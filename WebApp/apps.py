
from flask import Flask, render_template, request, session
from flask_session import Session



app=Flask(__name__)
#app.secret_key = "super secret key" # need to run by sessions by using the linking: https://stackoverflow.com/questions/26080872/secret-key-not-set-in-flask-session-using-the-flask-session-extension
# app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]='filesystem'

sess = Session()

notes=[]
@app.route("/", methods=["GET","POST"])

def index():
    
    if session.get("notes") is None:
        session["notes"] = []

    if request.method=="POST":
        note=request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])

@app.route("/more")

def more():
    return render_template("extra.html")
@app.route("/hello", methods=["GET","POST"]) # notice if we submit data by  GET, it can be seen in the web
def hello():
    if request.method=="GET":
        return "Please submit the form instead"
    else:
        name=request.form.get("name")
        return render_template("hello.html", name=name)


if __name__ == "__main__":


#     sess.init_app(app)
#     app.debug = True
      app.run()

