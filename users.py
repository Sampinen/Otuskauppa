from sqlalchemy.sql import text
from db import db

#sign-up
def signup(username, password_hash):
    insert_sql = text("INSERT INTO registered (username, password) VALUES (:username,:password_hash)")
    sql_execute = db.session.execute(insert_sql, {"username":username,"password_hash":password_hash})
    db.session.commit()
def login(username):
    select_sql = text("SELECT username, password FROM registered WHERE username=:username")
    sql_execute = db.session.execute(select_sql,{"username":username})
    user = sql_execute.fetchone()
    return user


#Tarkastaa onko käyttäjätunnus uniikki
def unique(username):
    select_sql = text("SELECT username FROM registered WHERE username=:username")
    sql_execute = db.session.execute(select_sql, {"username":username})
    is_user= sql_execute.fetchone()
    if is_user:
        return False
    else:
        return True



#Hae käyttäjän rahamäärä
def get_money(username):
    select_sql = text("SELECT money FROM registered WHERE username=:username")
    sql_execute = db.session.execute(select_sql, {"username":username})
    return sql_execute.scalar()

#Päivitä rahat
def update_money(username, money):
    update_sql = text("UPDATE registered SET money =:money WHERE username=:username")
    db.session.execute(update_sql,{"money":money,"username":username})
    db.session.commit()
