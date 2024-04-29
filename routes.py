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
            return redirect("/")
        if len(password) >30:
            "Salasanan pituus ei saa ylittää 30 merkkiä"
            return redirect("/")
        if len(username) >20:
            flash("Käyttäjänimen maksimipituus on 20 merkkiä")
            return redirect("/")
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
#Osta otus
@app.route("/buy/<creature_type>")
def buy(creature_type):
    username = session.get("username")
    if not username:
        session.pop('_flashes', None)
        flash("Sinun täytyy ensin kirjautua sisään")
        return redirect("/")
    
    money_query = select(registered.c.money).where(registered.c.username == username)
    update_query = db.session.execute(money_query)
    current_money = update_query.scalar()
    creature_price = session.get(f"{creature_type}_price")
    if current_money < creature_price:
        flash("Ei tarpeeksi rahaa")
        return redirect("/shop")

    updated_money = current_money - creature_price
    update_query = registered.update().values(money=updated_money).where(registered.c.username == username)
    db.session.execute(update_query)
    db.session.commit()

    add_creature = insert(creatures).values( type=creature_type, owner = username)
    db.session.execute(add_creature)
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
        flash("Sinulla ei ole oikeuksia toteuttaa tätä toimintoa.")
        redirect("/")
    new_name = request.form["name"]
    update_query = creatures.update().values(name=new_name).where(creatures.c.id == creature_id)
    db.session.execute(update_query)
    db.session.commit()
    return redirect("/creature/"+str(creature_id))

@app.route("/forum")
def forum():
    return render_template("forum.html")

@app.route("/send", methods=["POST"])
def send():
    webcontent = request.form["content"]
    if len(webcontent) >250:
        session.pop('_flashes', None)
        flash("Viestin pituus ei saa ylittää 250 merkkiä")
        return redirect("/forum")
    if len(webcontent) <1:
        session.pop('_flashes', None)
        flash("Et voi lähettää tyhjää viestiä")
        return redirect("/forum")
    ins = messages.insert().values(content = webcontent)
    db.session.execute(ins)
    db.session.commit()
    return redirect("/forum")