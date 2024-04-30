#forummessage
    # ins = messages.insert().values(content = webcontent)
    # db.session.execute(ins)
    # db.session.commit()
def send(username,message):
    sql_insert = text("INSERT INTO forumposts VALUES ()")