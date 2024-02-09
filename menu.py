import db
while True:
    keyboard=input("adad")
    
    if keyboard=="1":
            firstname, lastname, shomare_kart, password, mobile = input().split()
            db.new_user(firstname, lastname, shomare_kart, password, mobile)
            #if each person has only one mobile number
        

    elif keyboard=="2":
          sender_card, receiver_card, amount, password=input().split()
          amount=int(amount)
          db.transaction(sender_card, receiver_card, amount, password)