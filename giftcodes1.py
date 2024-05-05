from sqlalchemy.sql import text
from db import db

def add_code(code, reclaimable,money):
    insert_sql = text("INSERT INTO giftcodes (code, reclaimable, money) VALUES (:code,:reclaimable,:money)")
    sql_execute = db.session.execute(insert_sql, {"code":code,"reclaimable":reclaimable,"money":money})
    db.session.commit()

def find_code(code):
    select_sql = text("SELECT claimed,reclaimable,money FROM giftcodes WHERE (code=:code)")
    sql_execute = db.session.execute(select_sql,{"code":code})
    return sql_execute.fetchone()
def update_claimed(code):
    update_sql = text("UPDATE giftcodes SET claimed =true WHERE code=:code")
    db.session.execute(update_sql,{"code":code})
    db.session.commit()