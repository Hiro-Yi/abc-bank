
def statement(userId):
    db.execute("SELECT * FROM transactions WHERE user_id = %s", (userId,))  
    result = db.fetchall()
    for i in result:
        print()