import sqlite3

def create_table():
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS main(
                   firstname VARCHAR(31) NOT NULL,
                   lastname VARCHAR(31) NOT NULL,
                   shomare_kart INT NOT NULL UNIQUE,
                   password INT NOT NULL,
                   mobile VARCHAR(11) NOT NULL,
                   etebar INT NOT NULL DEFAULT 100,
                   charge INT NOT NULL DEFAULT 0
                   );""")
    conn.commit()
    cursor.close()
    conn.close()

def new_user(firstname: str, lastname: str, shomare_kart: int, password: int, mobile: str):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO main (firstname, lastname, shomare_kart, password, mobile)
                   VALUES (?, ?, ?, ?, ?);""",(firstname, lastname, shomare_kart, password, mobile))
    conn.commit()
    cursor.close()
    conn.close()

def get_user_by_name(firstname: str, lastname: str):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM main WHERE firstname = ? AND lastname = ?;",
                   (firstname, lastname))
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return result

def transaction(sender_card: int, receiver_card: int, amount: int):
    # check if amount is allowed
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT etebar FROM main WHERE shomare_kart = {sender_card};")
    sender_etebar = cursor.fetchone()[0]
    if amount <= sender_etebar:
        new_sender_etebar = sender_etebar - amount
        cursor.execute(f"SELECT etebar FROM main WHERE shomare_kart = {receiver_card};")
        receiver_etebar = cursor.fetchone()[0]
        new_receiver_etebar = receiver_etebar + amount
        cursor.execute(f"UPDATE main SET etebar = {new_receiver_etebar} WHERE shomare_kart = {receiver_card};")
        cursor.execute(f"UPDATE main SET etebar = {new_sender_etebar} WHERE shomare_kart = {sender_card};")
        conn.commit()
        cursor.close()
        conn.close()
        
    else:
        conn.commit()
        cursor.close()
        conn.close()
        raise Exception("NOT ENOUGH ETEBAR!")


    