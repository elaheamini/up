import sqlite3

def create_tables():
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    
    # Table for user information
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstname VARCHAR(31) NOT NULL,
                   lastname VARCHAR(31) NOT NULL,
                   card_number INT NOT NULL UNIQUE,
                   password VARCHAR(4) NOT NULL,
                   balance INT NOT NULL DEFAULT 100
                   );""")

    # Table for mobile numbers
    cursor.execute("""CREATE TABLE IF NOT EXISTS mobile_numbers (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INT,
                   mobile VARCHAR(11) NOT NULL,
                   charge INT NOT NULL DEFAULT 0,
                   FOREIGN KEY (user_id) REFERENCES users (id)
                   );""")
    
    conn.commit()
    cursor.close()
    conn.close()

def new_user(firstname: str, lastname: str, card_number: int, password: str, mobile_numbers: list):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    
    cursor.execute("""INSERT INTO users (firstname, lastname, card_number, password)
                   VALUES (?, ?, ?, ?);""", (firstname, lastname, card_number, password))
    
    user_id = cursor.lastrowid
    charge=0
    
    for mobile in mobile_numbers:
        cursor.execute("""INSERT INTO mobile_numbers (user_id, mobile, charge)
                       VALUES (?, ?, ?);""", (user_id, mobile, charge))

    conn.commit()
    cursor.close()
    conn.close()

def get_user_by_name(firstname: str, lastname: str):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    
    cursor.execute("""SELECT users.*, GROUP_CONCAT(mobile_numbers.mobile, ', ')
                   FROM users
                   LEFT JOIN mobile_numbers ON users.id = mobile_numbers.user_id
                   WHERE users.firstname = ? AND users.lastname = ?
                   GROUP BY users.id;""", (firstname, lastname))
    
    result = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return result

def transaction(sender_card: int, receiver_card: int, amount: int, password: str):
    conn = sqlite3.connect("up.db")
    cursor = conn.cursor()
    check_password(card_number=sender_card, password=password)
    cursor.execute(f"SELECT balance FROM users WHERE card_number = {sender_card};")
    sender_balance = cursor.fetchone()[0]
    # check if amount is allowed
    if amount <= sender_balance:
        new_sender_balance = sender_balance - amount
        cursor.execute(f"SELECT balance FROM users WHERE card_number = {receiver_card};")
        receiver_balance = cursor.fetchone()[0]
        new_receiver_balance = receiver_balance + amount
        cursor.execute(f"UPDATE users SET balance = {new_receiver_balance} WHERE card_number = {receiver_card};")
        cursor.execute(f"UPDATE users SET balance = {new_sender_balance} WHERE card_number = {sender_card};")
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
    #for i in range(len(mobile_numbers)):
    cursor.execute(f"SELECT charge FROM mobile_numbers WHERE mobile = '{simcard}';")
    # error cursor.fetchone() returns None
    db_result = cursor.fetchone()
    if db_result is not None:
        charge_feli=db_result[0]
    else:
        print("SIM not found!")
        new_user(firstname, lastname, card_number, password, mobile_numbers)
            
        #raise Exception("simcard not found!")
    card_number=int(input("card number: "))
    password=input("password: ")
    check_password(card_number, password)
    cursor.execute(f"SELECT balance FROM users WHERE card_number = {card_number};")
    balance_feli = cursor.fetchone()[0]
    if balance_feli>=amount:
        new_balance=balance_feli-amount
        new_charge=charge_feli+amount
        cursor.execute(f"UPDATE users SET balance = {new_balance} WHERE card_number = {card_number};")
        cursor.execute(f"UPDATE mobile_numbers SET charge = {new_charge} WHERE mobile = '{simcard}';")
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
    cursor.execute(f"SELECT password FROM users WHERE card_number = {card_number};")
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
    cursor.execute(f"SELECT balance FROM users WHERE card_number = {card_number};")
    balance = cursor.fetchone()[0]
    print(f"balance: {balance}")
create_tables()