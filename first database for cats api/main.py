from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user, UserMixin
import requests
app=Flask(__name__)
login_manager = LoginManager(app)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
db=SQLAlchemy(app)
with app.app_context():
    class User( db.Model,UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        phone = db.Column(db.String(100), unique=True)
        password = db.Column(db.String(1000))
        tries=db.Column(db.Integer)


    db.create_all()
class MyModelView(ModelView):
    def is_accessible(self):
        return True
admin = Admin(app)
admin.add_view(MyModelView(User, db.session))
@app.route("/")
def start():
    return "welcom"
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        phone=request.form.get("phone")
        password=request.form.get("password")
        new_user=User(phone=phone,password=generate_password_hash(password, method='pbkdf2:sha256',
            salt_length=8))
        db.session.add(new_user)
        db.session.commit()
        return "register "

    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        phone=request.form.get("phone")
        password=request.form.get("password")
        target=User.query.filter_by(phone=phone).first()
        if target and check_password_hash(target.password,password):
            login_user(target)
            return redirect("/dash")
        else:
            credential_ = "wrong credential "
            return credential_
    return render_template("login.html")
@app.route("/dash")
def dash():
    return render_template("dash.html")

@app.route("/get_temp",methods=["GET","POST"])
def get_temp():
    if request.method =="POST":
        city_name=request.form.get("city")
        api_key = "3604913102aab83b144488bdaf38a6e5"
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(url=url, params=params)
        data = response.json()

        if response.status_code==200:
            data = response.json()
            temp=data["main"]["temp"]

            if current_user.tries==None:
                current_user.tries=0

            current_user.tries+=1

            db.session.commit()
            return f"the temp is {temp}"


if __name__=="__main__":
    app.run(debug=True)