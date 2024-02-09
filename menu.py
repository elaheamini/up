import db
while True:
    keyboard = input("""
                   enter 1 to register your information,
                   enter 2 to transact,
                   enter 3 to charge SIM,
                   enter 4 to print card balance: """)
    
    if keyboard=="1":
            firstname = input("firstname: ")
            lastname = input("lastname: ")
            card_number = int(input("card number: "))
            password = input("password: ")
            mobile = input("mobile number: ")
            db.new_user(firstname, lastname, card_number, password, mobile)
            #if each person has only one mobile number

    elif keyboard=="2":
          sender_card = int(input("sender card: "))
          receiver_card = int(input("receiver card: "))
          amount = int(input("the amount you wanna transact: "))
          password = input("password: ")
          db.transaction(sender_card, receiver_card, amount, password)

    elif keyboard=="3":
          simcard = input("enter your mobile number: ")
          amount = int(input("amount: "))
          db.to_charge(simcard, amount)

    elif keyboard=="4":
          card_number = int(input("card number: "))
          password = input("password: ")
          db.print_balance(card_number, password)


