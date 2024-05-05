import random
import string
from sqlalchemy.sql import text
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sql
import os

base = declarative_base()
engine = sql.create_engine("postgresql://localhost")
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)



def add_code(code, reclaimable,money):
    insert_sql = text("INSERT INTO giftcodes (code, reclaimable, money) VALUES (:code,:reclaimable,:money)")
    sql_execute = session.execute(insert_sql, {"code":code,"reclaimable":reclaimable,"money":money})
    session.commit()

def generate():
    if os.path.exists("giftcodes.txt"):
        f = open("giftcodes.txt","r+")
    else:
        f= open("giftcodes.txt","w+")
    money = int(input("Paljonko rahaa haluat lahjakoodin antavan?"))
    howmany = int(input("Montako lahjakoodia haluat generoida?"))
    reclaim = input("Onko koodi kertakäyttöinen (K) vai monikäyttöinen (M)")
    reclaimable = True if reclaim =="M" else False
    while howmany >0:
        giftcode =''.join(random.choices(string.ascii_letters , k=12))
        add_code(giftcode, reclaimable,money)
        howmany -= 1
        f.write(str(giftcode)+"\n")
generate()

