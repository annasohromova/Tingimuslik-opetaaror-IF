
from base64 import b16decode
from math import *


#try:
    #nimi=str(input("Mis sinu nimi on? ->"))


#    if nimi.upper()=="JUKU":
#        print("Lähme kinno?")
#       vanus=int(input("Kui vana sa oled?"))
#        if vanus<=0 or vanus>=100:
#            print("Viga andmetega")
#        elif vanus<6:
#            print("Tasuta")
#        elif vanus>=6 and vanus<=14:
#            print("Lapsepilet")
#        elif vanus>=15 and vanus<65: 
#            print("Täispilet")
#        elif vanus>=65: 
#            print("Sooduspilet")
#    else:
#        print("Otsime Juku")
#except:
#    print("Vale andmetüüp")


#2 Küsi kahe inimese nimed ning teata, et nad on täna pinginaabrid

#nimi1=input("Mis sinu nimi on? ")
#nimi2=input("Mis sinu nimi on? ")
#if nimi1.isalpha()==True and nimi2.isalpha():
#    if nimi1.lower()==("juku") and nimi2.lower()==("mari"): 
#        print(f"{nimi1} ja {nimi2} olete täna naabrid")    
#    else:
#        print()
#else:
#    print("Vale andmetüüp")


#3 Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind



a=float(input("Sisestage seina pikkus ->"))
b=float(input("Sisesatge seina laius ->"))
if a<=0 and b<=0:
    print("Error")
else:
 
    try:
        küsimus=float(input("Kas soovite renoveerida? 0-ei, 1-jah => \n"))
    except:
        print("Vale andmetüüp")
    if küsimus==1:
        k=input("Kui palju on ruutmeeter?")
        c=input("Kui palju põrandavahetus maksab?")
        S=print("See läheb teile", a*b)
        print("Head aega!")
    else:
        print("Head aega!")




#4 Leia 30% hinnasoodustusega hinna, kui alghind on suurem kui 700
try:
    hind=float(input("Milline hind on?"))
    if hind>700:
        print(f"sul on soodus 30%, {hind-hind*0.3}")
    else:
        print(hind)
except:
    print("Error")


    #8

#try:

#    a=int(input("Kas soovite piima osta?(jah-1 või ei-0): "))
#    b=int(input("Kas soovite saia osta?(jah-1 või ei-0): "))
#    c=int(input("Kas soovite leiba osta?(jah-1 või ei-0): "))
#    if a<0 and b<0 and c<0:
#        print("Error")
#    if a==1 and b==0 and c==0:
#        piim=0.79
#        sai=0
#        leib=0
#        S=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",S)
#    elif a==0 and b==1 and c==0:
#        piim=0
#        sai=0.8
#        leib=0
#        P=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",P)
#    elif a==0 and b==0 and c==1:
#        piim=0
#        sai=0
#        leib=0.8
#        F=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",F)
#    elif a==1 and b==1 and c==0:
#        piim=0.79
#        sai=0.8
#        leib=0
#        L=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",L)
#    elif a==0 and b==1 and c==1:
#        piim=0
#        sai=0.8
#        leib=0.8
#        O=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",O)
#    elif a==1 and b==0 and c==1:
#        piim=0.79
#        sai=0
#        leib=0.8
#        U=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",U)
#    elif a==1 and b==1 and c==1:
#        piim=0.79
#        sai=0.8
#        leib=0.8
#        A=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",A)
#except:
#    print("Vale Andmetüüp")

#9

#try:
#    a=float(input("ütle pool a "))
#    b=float(input("ütle pool b "))
#    if a==b:
#        print("See on ruut")
#    else:
#        print("See ei ole ruut")
#except:
#    print("Value Error")

#10

#try:
#    a=float(input("1 number "))
#    b=float(input("1 number "))
#    c=input("mis märk sa oled +-*/ \n ")
#    if c==("+"):
#        print(a+b)
#    elif c==("-"):
#        print(a-b)
#    elif c==("*"):
#        print(a*b)
#    elif c==("/"):
#        if b==0:
#            print("Väiksem kui 0")
#        else:
#            print(a/b)
#except:
#    print("Value Error")

#11

#now = datetime.datetime.now()
#try:
#    a=int(input("Sisesta sünniaasta. "))
#except:
#    print("Value Error")
#b=int(now.year)
#c=int(b-a)
#print(c)
#f=c%5
#if f==0:
#    print("teil on juubel")
#else:
#    print("Kui kahju")

#12

#try:
#    a=float(input("sisesta toote hind "))
#    if a<=10:
#        print("sul on soodus 10%",a-a*0.1)
#    elif a>10:
#        print("sul on soodus 20%",a-a*0.2)
#except:
#    print("Value Error")



#13

try:
    a=int(input("Kas sa oled mees?(jah-1 või ei-0) \n"))
    if a==1:
        b=int(input("Kui vana sa oled? "))
        if b>=16 and b<=18:
            print("sobid")
    else:
        print("sa oled naine sest, et sa ei sobi")
except:
    print("Value Error")
