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

# new_user(firstname="elahe",lastname="amini",shomare_kart=6037997503297156,password=1234, mobile="09120000000")
# create_table()
