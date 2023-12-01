import sqlite3
con = sqlite3.connect(r"G:\reps\minor-project\Database\Career_Recommedation_System.db")
cur = con.cursor()
def fetchname(user_id):
    statement = f"SELECT First_name from user_info WHERE User_id='{user_id}';"
    cur.execute(statement)
    result = cur.fetchone()
    name = result[0] if result else ""
    return name
print(fetchname("Tikna123"))
