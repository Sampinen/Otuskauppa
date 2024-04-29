

#getcreatures
def get_creatures(username):
    select_sql = text("SELECT  FROM registered WHERE username=:username")
    sql_execute = db.session.execute(select_sql, {"username":username})
    current_money = sql_execute.scalar()
#add_creature

def add_creature(username,creature_type):
    insert_sql = text("INSERT INTO creatures (type,username) VALUES ({creature_type},{username})")
    db.session.execute(add_creature)
    db.session.commit()
    


    

#changename


