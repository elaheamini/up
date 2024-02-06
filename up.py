etelaat={}
kb=input("1:sabte kart,2:kharide charge,3:mande hesab,4:kart be kart")
t=0
while True:
    if kb=="1":
        for i in range(0,t+1):
            firtname=input("fnam ra")
            lastname=input("lname ra")
            kart=input("shomare kart ra vared konid")
            while len(kart)<16:
                kart=input("shomare kart bayad 16")
                passw=input("ramz ra")
                b[i]=passw
                #ramz 4 raghami?
                mobile=input("mobile ra")
                while shomare[0]!="0" or len(shomare)!=11:
                shomare=input("shomare namotabar ast. dobare talash konid. shomare bayad 11 ragham bashad va ba 0 shorou shavad.")
                t=t+1
            
        file=open('etelaat.txt', 'w')
        file.write('write here')
    elif kb=="2":
        mobile=input("hfueg")
        if mobile not in etelaat:
            mobile=input("sabt nashode. mojadad talash ya shomare kart jadid sabt")
        if mobile in etelaat:
            mablagh=int(input())
            kart=input()
            passw=input()
            if #check kardan value and key passw and kart and etebar>=mablagh
                etebar=etebar-mablagh
    elif kb=="3":
        print(etebar)
    elif kb=="4":
        kart1=input()
        kart2=input()
        etebar1=c[i]
        if mablagh<=etebar:
            etebar1=etebar1-mablagh
            etebar2=etebar2+mablagh



