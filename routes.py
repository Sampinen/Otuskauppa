from app import app
#from flask import Flask
import messageforum
import users
import creatures
from flask import Flask 
from flask import render_template, request,url_for,redirect,session, flash
from flask_sqlalchemy import SQLAlchemy 
from os import getenv
from sqlalchemy import text
from dotenv import load_dotenv
load_dotenv()
from werkzeug.security import check_password_hash, generate_password_hash
import sqlalchemy as sql

#from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean,select, update, insert



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    user = users.login(username)
    if not user:
        flash("Väärä käyttäjätunnus tai salasana")
        return redirect("/logout")
    else:
        hash_value = users.login(username).password
        if check_password_hash(hash_value, password):
            flash("Kirjautuminen onnistui")
            money = users.get_money(username)
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
        is_unique = users.unique(username)
        if len(username) <1:
            session.pop('_flashes', None)
            flash("Käyttäjänimi ei voi olla tyhjä.")
            redirect("/")
        if is_unique == False:
            session.pop('_flashes', None)
            flash("Samanniminen käyttäjä on jo olemassa. Valitse toinen käyttäjänimi")
            return redirect("/")
        if len(password) <8:
            session.pop('_flashes', None)
            flash("Salasanan tulee olla vähintään 8 merkkiä")
            return redirect("/")
        if len(password) >30:
            session.pop('_flashes', None)
            "Salasanan pituus ei saa ylittää 30 merkkiä"
            return redirect("/")
        if len(username) >20:
            session.pop('_flashes', None)
            flash("Käyttäjänimen maksimipituus on 20 merkkiä")
            return redirect("/")
        hash_value = generate_password_hash(password)
        users.signup(username,hash_value)
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
        session.pop('_flashes', None)
        flash("Sinun täytyy ensin kirjautua sisään")
        return redirect("/")
    haukerias_price = creatures.get_price("haukerias")
    session["haukerias_price"] = haukerias_price

    lohari_price = creatures.get_price("lohari")
    session["lohari_price"]=lohari_price

    return render_template("shop.html", haukerias_price = haukerias_price, lohari_price=lohari_price)
#Osta otus
@app.route("/buy/<creature_type>")
def buy(creature_type):
    username = session.get("username")
    if not username:
        session.pop('_flashes', None)
        flash("Sinun täytyy ensin kirjautua sisään")
        return redirect("/")
    current_money = users.get_money(username)
    creature_price = session.get(f"{creature_type}_price")
    if current_money < creature_price:
        flash("Ei tarpeeksi rahaa")
        return redirect("/shop")

    updated_money = current_money - creature_price
    users.update_money(username, updated_money)

    creatures.add_creature(username,creature_type)
    session["money"] = updated_money

    return redirect("/shop")

#sivu, jonka kautta pääsee katselemaan omistamiaan otuksia
@app.route("/mycreatures")
def mycreatures():
    username = session.get("username")
    if not username:
        session.pop('_flashes', None)
        flash("Sinun täytyy ensin kirjautua sisään")
        return redirect("/")
    my_creatures=creatures.get_creatures(username)
    return render_template("mycreatures.html",my_creatures = my_creatures)
#luo automaattisesti sivun otuksen id:n mukaan. Kaikkilla kirjautuneilla on pääsy katsomaan otuksia, mutta ominaisuudet ovat avoinna ainoastaan omistajalle (nimen vaihto, myynti jne.)
@app.route("/creature/<int:id>")
def page(id):
    username = session.get("username")
    if not username:
        session.pop('_flashes', None)
        flash("Sinun täytyy ensin kirjautua sisään")
        return redirect("/")
    creature = creatures.get_info(id)
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
    #Tällä hetkellä is_owner muuttuja ei vielä tee mitään
    if username == creature_owner:
        is_owner = True
    else:
        is_owner = False

    return render_template("creature.html",creature_id=creature_id,creature_name=creature_name,creature_type=creature_type, creature_owner =creature_owner,picture=picture,is_owner = is_owner)

#Ei vielä toiminnassa
@app.route("/changename/<creature_id>",methods=["POST"])
def changename(creature_id):
    username = session.get("username")
    is_owner = session.get(creature_id)
    if not username or not creature_id:
        session.pop('_flashes', None)
        flash("Sinulla ei ole oikeuksia toteuttaa toimintoa.")
        redirect("/")
    new_name = request.form["name"]
    creatures.change_name(new_name)
    return redirect("/creature/"+str(creature_id))

@app.route("/forum")
def forum():
    messages = messageforum.get_messages()
    return render_template("forum.html", messages = messages)




@app.route("/send", methods=["POST"])
def send():
    username = session.get("username")
    if not username:
        session.pop('_flashes', None)
        flash("Sinun täytyy ensin kirjautua sisään")
        return redirect("/")
    webcontent = request.form["content"] 
    if len(webcontent) >250:
        session.pop('_flashes', None)
        flash("Viestin pituus ei saa ylittää 250 merkkiä")
        return redirect("/forum")
    if len(webcontent) <1:
        session.pop('_flashes', None)
        flash("Et voi lähettää tyhjää viestiä")
        return redirect("/forum")
    message = messageforum.send_message(username,webcontent)
    return redirect("/forum")

@app.route("/giftcodes")
def giftcodes():
    giftcode = request.form["giftcode"]
    return render_template("giftcodes.html")