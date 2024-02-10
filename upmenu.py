import mydb
while True:
    keyboard = input("""
                   enter 1 to register your information,
                   enter 2 to transact,
                   enter 3 to charge SIM,
                   enter 4 to print card balance: """)
    
    if keyboard == "1":
      firstname = input("firstname: ")
      lastname = input("lastname: ")
      card_number = int(input("card number: "))
      password = input("password: ")
      mobile_numbers = input("Enter mobile numbers separated by commas and one space like ', ': ").split(', ')
      mydb.new_user(firstname, lastname, card_number, password, mobile_numbers)

    elif keyboard=="2":
      sender_card = int(input("sender card: "))
      receiver_card = int(input("receiver card: "))
      amount = int(input("the amount you wanna transact: "))
      password = input("password: ")
      mydb.transaction(sender_card, receiver_card, amount, password)

    elif keyboard=="3":
      simcard = input("enter your mobile number: ")
      amount = int(input("amount: "))
      mydb.to_charge(simcard, amount)

    elif keyboard=="4":
      card_number = int(input("card number: "))
      password = input("password: ")
      mydb.print_balance(card_number, password)


