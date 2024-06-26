from sqlalchemy.sql import text
from db import db
#Tämä tiedosto sisältää creatures ja creatureprices taulukkoihin liittyvät SQL komennot


#get_price
def get_price(type):
    select_sql = text("SELECT price FROM creatureprices WHERE type =:type")
    sql_execute = db.session.execute(select_sql,{"type":type})
    return sql_execute.scalar()


#get_creature_info
def get_info(id):
    select_sql = text("SELECT * FROM creatures WHERE id=:id")
    sql_execute =db.session.execute(select_sql, {"id":id})
    return sql_execute.fetchone()

#get_creatures
def get_creatures(username):
    select_sql = text("SELECT * FROM creatures WHERE owner=:username")
    sql_execute = db.session.execute(select_sql, {"username":username})
    return sql_execute.fetchall()
#add_creature

def add_creature(username,creature_type):
    insert_sql = text("INSERT INTO creatures (type,owner) VALUES (:creature_type,:username)")
    db.session.execute(insert_sql, {"creature_type":creature_type,"username":username})
    return db.session.commit()
#changename

def change_name(id, new_name):
    update_sql = text("UPDATE creatures SET name =:new_name WHERE id=:id")
    sql_execute = db.session.execute(update_sql,{"new_name":new_name, "id":id})
    return db.session.commit()



