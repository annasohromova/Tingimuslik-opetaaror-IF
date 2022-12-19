
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

