#sign-up

#login


#getmoney
def get_money(username):
    select_sql = text("SELECT money FROM registered WHERE username=:username")
    sql_execute = db.session.execute(select_sql, {"username":username})
    current_money = sql_execute.scalar()

#updatemoney
def update_money(username, money):
    update_sql = text(f"UPDATE registered SET money =:{money} WHERE username=:{username}")
    db.session.execute(update_query)
    db.session.commit()
