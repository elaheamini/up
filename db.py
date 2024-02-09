import sqlite3

def create_table():
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS main(
                   firstname VARCHAR(31) NOT NULL,
                   lastname VARCHAR(31) NOT NULL,
                   card_number INT NOT NULL UNIQUE,
                   password VARCHAR(4) NOT NULL,
                   mobile VARCHAR(11) NOT NULL,
                   balance INT NOT NULL DEFAULT 100,
                   charge INT NOT NULL DEFAULT 0
                   );""")
    conn.commit()
    cursor.close()
    conn.close()

def new_user(firstname: str, lastname: str, card_number: int, password: str, mobile: str):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO main (firstname, lastname, card_number, password, mobile)
                   VALUES (?, ?, ?, ?, ?);""",(firstname, lastname, card_number, password, mobile))
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
    check_password(card_number=sender_card, password=password)
    cursor.execute(f"SELECT balance FROM main WHERE card_number = {sender_card};")
    sender_balance = cursor.fetchone()[0]
    # check if amount is allowed
    if amount <= sender_balance:
        new_sender_balance = sender_balance - amount
        cursor.execute(f"SELECT balance FROM main WHERE card_number = {receiver_card};")
        receiver_balance = cursor.fetchone()[0]
        new_receiver_balance = receiver_balance + amount
        cursor.execute(f"UPDATE main SET balance = {new_receiver_balance} WHERE card_number = {receiver_card};")
        cursor.execute(f"UPDATE main SET balance = {new_sender_balance} WHERE card_number = {sender_card};")
        conn.commit()
        cursor.close()
        conn.close()
        
    else:
        conn.commit()
        cursor.close()
        conn.close()
        raise Exception("NOT ENOUGH BALANCE!") #???????????????
   
def to_charge(simcard: str, amount: int):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT charge FROM main WHERE mobile = '{simcard}';")
    # error cursor.fetchone() returns None
    db_result = cursor.fetchone()
    if db_result is not None:
        charge_feli=db_result[0]
    else:
        raise Exception("simcard not found!")
    card_number=int(input("card number: "))
    password=input("password: ")
    check_password(card_number, password)
    cursor.execute(f"SELECT balance FROM main WHERE card_number = {card_number};")
    balance_feli = cursor.fetchone()[0]
    if balance_feli>=amount:
        new_balance=balance_feli-amount
        new_charge=charge_feli+amount
        cursor.execute(f"UPDATE main SET balance = {new_balance} WHERE card_number = {card_number};")
        cursor.execute(f"UPDATE main SET charge = {new_charge} WHERE mobile = '{simcard}';")
        conn.commit()
        cursor.close()
        conn.close()

    else:
        conn.commit()
        cursor.close()
        conn.close()
        raise Exception("NOT ENOUGH balance!")




def check_password(card_number: int, password: str):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT password FROM main WHERE card_number = {card_number};")
    password_main=cursor.fetchone()[0]
    if password==password_main:
        #print("yeessss")
        return True

    else:
        while password!=password_main:
            password=input("incorrect password. try again or enter 5 to back to menu.")

            #if password=="4":
                #pass #add back to menu option later
        check_password(card_number, password)
        #print("incorrect")
        conn.commit()
        cursor.close()
        conn.close()

def print_balance(card_number, password):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    check_password(card_number, password)
    cursor.execute(f"SELECT balance FROM main WHERE card_number = {card_number};")
    balance = cursor.fetchone()[0]
    print(f"balance: {balance}")
#create_table()