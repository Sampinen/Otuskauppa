from flask import Flask 
from flask import render_template, request,url_for,redirect,session, flash
from flask_sqlalchemy import SQLAlchemy 
from os import getenv
from sqlalchemy.sql import text
from dotenv import load_dotenv
load_dotenv()
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy as sql
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean,select, update, insert



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost"
db = SQLAlchemy(app)
app.secret_key =getenv("SECRET_KEY")
meta = sql.MetaData()

#Taulu, joka sisältää kaikki rekisteröityneet pelaajat ja heidän tietonsa (käyttäjänimi, salasana, rahat)
registered = sql.Table(
    'registered', meta,
    sql.Column('id',Integer,primary_key=True),
    sql.Column('username',String),
    sql.Column('password',String),
    sql.Column('money',Integer)
)
#Taulu joka sisältää kaikki otustyypit ja niiden hinnat
creatureprices = sql.Table(
    'creatureprices',meta,
    sql.Column('id',Integer,primary_key=True),
    sql.Column('type',String),
    sql.Column('price',Integer)
)
#Taulu joka sisältää kaikkien pelaajien omistamat otukset
creatures = sql.Table(
    'creatures',meta,
    sql.Column('id',Integer,primary_key=True),
    sql.Column('name',String),
    sql.Column('type',String),
    sql.Column('owner',String)
)
#Taulu, joka sisältää lahjakoodeja, joilla voi lunastaa pelinsisäistä rahaa.
giftcodes = sql.Table(
    'giftcodes', meta,
    sql.Column('id',Integer,primary_key=True),
    sql.Column('code',String),
    sql.Column('claimed',Boolean)
)
#Taulu, joka sisältää foorumiin postatut viestit ja niiden lähettäjät
forumposts = sql.Table(
    'forumposts',meta,
    sql.Column('id',Integer,primary_key=True),
    sql.Column('content',String),
    sql.Column('username',String)
)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    jes = registered.select().where(registered.c.username == username)
    result = db.session.execute(jes)
    user = result.fetchone()
    if not user:
        flash("Väärä käyttäjätunnus tai salasana")
        return redirect("/logout")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            flash("Kirjautuminen onnistui")
            money_query=select(registered.c.money).where(registered.c.username == username)
            money_result = db.session.execute(money_query)
            money= money_result.scalar()
            session["money"] = money
            return redirect("/mypage")
        else:
            flash("Väärä käyttäjätunnus tai salasana")
            return redirect("/logout")
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
        if len(password) <8:
            flash("Salasanan tulee olla vähintään 8 merkkiä")
            return redirect("/logout")
        if len(password) >30:
            "Salasanan pituus ei saa ylittää 30 merkkiä"
            return redirect("/logout")
        if len(username) >20:
            flash("Käyttäjänimen maksimipituus on 20 merkkiä")
        hash_value = generate_password_hash(password)

        # sql = "INSERT INTO registered (username, password) VALUES (:content)"
        ins = registered.insert().values(username=username,password=hash_value)
        # db.session.execute(sql,{"username":username,"password":hash_value})
        db.session.execute(ins)
        db.session.commit()
        flash("Käyttäjän luonti onnistui, kirjaudu sisään")
        return redirect("/")
    return render_template("signup.html")
@app.route("/mypage")
def mypage():
    username = session.get("username")
    if not username:
        return redirect("/login")
    return render_template("mypage.html")


@app.route("/shop")
def shop():
    username = session.get("username")
    if not username:
        return redirect("/login")
    #session.pop('_flashes', None)
    haukerias_query= select(creatureprices.c.price).where(creatureprices.c.type == "haukerias")
    haukerias_result = db.session.execute(haukerias_query)
    haukerias_price= haukerias_result.scalar()
    session["haukerias_price"] = haukerias_price

    lohari_query= select(creatureprices.c.price).where(creatureprices.c.type == "lohari")
    lohari_result = db.session.execute(lohari_query)
    lohari_price= lohari_result.scalar()
    session["lohari_price"]=lohari_price

    return render_template("shop.html", haukerias_price = haukerias_price, lohari_price=lohari_price)
#Osta otus, joka on tyyppiä haukerias
@app.route("/buyhaukerias")
def buy():
    username = session.get("username")
    if not username:
        return redirect("/")
    
    money_query = select(registered.c.money).where(registered.c.username == username)
    update_query = db.session.execute(money_query)
    current_money = update_query.scalar()
    haukerias_price = session.get("haukerias_price")
    if current_money < haukerias_price:
        flash("Ei tarpeeksi rahaa")
        return redirect("/shop")

    updated_money = current_money - session.get("haukerias_price")
    update_query = registered.update().values(money=updated_money).where(registered.c.username == username)
    db.session.execute(update_query)
    db.session.commit()

    add_haukerias = insert(creatures).values( type="haukerias", owner = username)
    db.session.execute(add_haukerias)
    db.session.commit()
    session["money"] = updated_money

    return redirect("/shop")
#Osta otus, joka on tyyppiä lohari
@app.route("/buylohari")
def buylohari():
    username = session.get("username")
    if not username:
        return redirect("/")
    money_query = select(registered.c.money).where(registered.c.username == username)
    money_result = db.session.execute(money_query)
    current_money = money_result.scalar()
    lohari_price = session.get("lohari_price")
    if current_money < lohari_price:
        flash("Ei tarpeeksi rahaa")
        return redirect("/shop")
    updated_money = current_money - lohari_price
    update_query = registered.update().values(money=updated_money).where(registered.c.username == username)
    db.session.execute(update_query)
    db.session.commit()

    add_lohari = insert(creatures).values( type="lohari", owner = username)
    db.session.execute(add_lohari)
    db.session.commit()

    session["money"] = updated_money

    return redirect("/shop")
#sivu, jonka kautta pääsee katselemaan omistamiaan otuksia
@app.route("/mycreatures")
def mycreatures():
    username = session.get("username")
    if not username:
        return redirect("/")
    query = select(creatures).where(creatures.c.owner==username)
    get_creatures = db.session.execute(query)
    my_creatures = get_creatures.fetchall()
    return render_template("mycreatures.html",my_creatures = my_creatures)
#luo automaattisesti sivun otuksen id:n mukaan. Kaikkilla kirjautuneilla on pääsy katsomaan otuksia, mutta ominaisuudet ovat avoinna ainoastaan omistajalle (nimen vaihto, myynti jne.)
@app.route("/creature/<int:id>")
def page(id):
    username = session.get("username")
    if not username:
        return render_template("/")
    get_creature = select(creatures).where(creatures.c.id==id)
    creature = db.session.execute(get_creature).fetchone()
    if not creature:
        return "Sivua ei ole olemassa"
        
    creature_id = creature.id
    creature_name = creature.name
    creature_type = creature.type

    if creature_type == "haukerias":
        picture = "/static/haukerias.png"
    if creature_type == "lohari":
        picture = "/static/lohari.jpg"
    creature_owner = creature.owner
    if username == creature_owner:
        is_owner = True
    else:
        is_owner = False

    return render_template("creature.html",creature_id=creature_id,creature_name=creature_name,creature_type=creature_type, creature_owner =creature_owner,picture=picture,is_owner = is_owner)



