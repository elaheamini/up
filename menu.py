import db
while True:
    keyboard=input("adad")
    def keyboard1():
        if keyboard=="1":
            firstname, lastname, shomare_kart, password, mobile = input().split()
            db.new_user(firstname, lastname, shomare_kart, password, mobile)
            #if each person has only one mobile number
    continue
        #elif keyboard=="2"
