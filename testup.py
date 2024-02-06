kb=input("1:sabte kart,2:kharide charge,3:mande hesab,4:kart be kart")
t=0
info=[]
a=[]
b=[]
c=[]
d=[]
e=[]
while True:
    if kb=="1":
        firstname=input("nam: ")
        #a[i]
        a.append(firstname)
        lastname=input("neme khanevadegi: ")
        #b[i]
        b.append(lastname)
        kart=input("shomare kart: ")
        #c[i]
        c.append(kart)
        while len(kart)<16:
            kart=input("shomare kart bayad 16 raghami bashad.")
        passw=input("ramz: ")
        #d[i]
        d.append(passw)
        #ramz 4 raghami?
        mobile=input("mobile: ")
        #e[i]
        e.append(mobile)
        while mobile[0]!="0" or len(mobile)!=11:
            smobile=input("mobile bayad 11 ragham bashad va ba 0 shorou shavad.")
        info=[a,b,c,d,e]
        
    file=open('etelaat.txt', 'w')
    for line in info:
        file.write(','.join(line)+'\n')
    file.close()