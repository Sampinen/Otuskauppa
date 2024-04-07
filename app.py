from flask import Flask 
from flask import render_template, request,url_for,redirect,session, flash
from flask_sqlalchemy import SQLAlchemy 
from os import getenv
from sqlalchemy.sql import text
from dotenv import load_dotenv
load_dotenv()
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy as sql
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost"
db = SQLAlchemy(app)
app.secret_key =getenv("SECRET_KEY")
meta = sql.MetaData()


registered = sql.Table(
    'registered', meta,
    sql.Column('id',Integer,primary_key=True),
    sql.Column('username',String),
    sql.Column('password',String),
)
creatureprices = sql.Table(
    'creatureprices',meta,
    sql.Column('id',Integer,primary_key=True),
    sql.Column('content',String),
)

@app.route("/")
def index():
    print ("aapeli")
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] =username
    session["password"] = password
    #sql = "SELECT id, password FROM registered WHERE username=:username"
    jes = registered.select().where(registered.c.username == username)
    #result = db.session execute(sql, {"username":username})
    result = db.session.execute(jes)
    user = result.fetchone()
    if not user:
        #TODO: invalid username
        flash("Väärä käyttäjätunnus tai salasana")
        return redirect("/")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            flash("Kirjautuminen onnistui")
            #TODO: correct username and password
            return redirect("/")
        else:
            flash("Väärä käyttäjätunnus tai salasana")
            return redirect("/")
            #TODO: invalid password
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/signup", methods=["POST","GET"])
def singup():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        hash_value = generate_password_hash(password)
        ins = registered.insert().values(username=username,password=hash_value)
        db.session.execute(ins)
        db.session.commit()
        #flash("Käyttäjän luonti onnistui, kirjaudu sisään")
        return redirect("/")
    return render_template("signup.html")



# @app.route("/shop")
# def shop():
#     return render_template("shop.html")

# @app.route("/mycreatures")
# def mycreatures():
#     p = sa.select(sa.text('content').select_from(sa.text('creatureprices')))
#     result = db.session.execute(p)
#     return render_template("mycreatures.html")



