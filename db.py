import sqlite3

def create_table():
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS main(
                   firstname VARCHAR(31) NOT NULL,
                   lastname VARCHAR(31) NOT NULL,
                   shomare_kart INT NOT NULL UNIQUE,
                   password VARCHAR(4) NOT NULL,
                   mobile VARCHAR(11) NOT NULL,
                   etebar INT NOT NULL DEFAULT 100,
                   charge INT NOT NULL DEFAULT 0
                   );""")
    conn.commit()
    cursor.close()
    conn.close()

def new_user(firstname: str, lastname: str, shomare_kart: int, password: str, mobile: str):
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

def transaction(sender_card: int, receiver_card: int, amount: int, password: str):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    check_password(shomare_kart=sender_card, password=password)
    cursor.execute(f"SELECT etebar FROM main WHERE shomare_kart = {sender_card};")
    sender_etebar = cursor.fetchone()[0]
    # check if amount is allowed
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
        raise Exception("NOT ENOUGH ETEBAR!") #???????????????
   
def to_charge(simcard: str, mablagh: int): #without checking password
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    shomare_kart, password=input().split()
    shomare_kart=int(shomare_kart)
    check_password(shomare_kart, password)
    cursor.execute(f"SELECT etebar FROM main WHERE shomare_kart = {shomare_kart};")
    etebar_feli = cursor.fetchone()[0]
    if etebar_feli>=mablagh:
        new_etebar=etebar_feli-mablagh
        cursor.execute(f"SELECT charge FROM main WHERE mobile = '{simcard}';")
        # error cursor.fetchone() returns None
        db_result = cursor.fetchone()
        if db_result is not None:
            charge_feli=db_result[0]
        else:
            raise Exception("simcard peyda nashod!")
        new_charge=charge_feli+mablagh
        cursor.execute(f"UPDATE main SET etebar = {new_etebar} WHERE shomare_kart = {shomare_kart};")
        cursor.execute(f"UPDATE main SET charge = {new_charge} WHERE mobile = '{simcard}';")
        conn.commit()
        cursor.close()
        conn.close()

    else:
        conn.commit()
        cursor.close()
        conn.close()
        raise Exception("NOT ENOUGH ETEBAR!")




def check_password(shomare_kart: int, password: str):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT password FROM main WHERE shomare_kart = {shomare_kart};")
    password_main=cursor.fetchone()[0]
    if password==password_main:
        #print("yeessss")
        return True

    else:
        while password!=password_main:
            password=input("incorrect password. try again or enter 4 to back to menu.") 
            #if password=="4":
                #pass #add back to menu option later
        check_password(shomare_kart, password)
        #print("incorrect")
        conn.commit()
        cursor.close()
        conn.close()
