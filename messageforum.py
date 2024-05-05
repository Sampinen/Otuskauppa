from sqlalchemy.sql import text
from db import db

#sendmessage
def send_message(username,message):
    sql_insert = text("INSERT INTO forumposts (content, username) VALUES (:message, :username)")
    db.session.execute(sql_insert, {"message":message, "username":username})
    db.session.commit()
#getmessages
def get_messages():
    result = db.session.execute(text("SELECT content, username FROM forumposts"))
    return result