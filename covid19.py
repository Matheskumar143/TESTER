print("********************covid19 pandamic days********************")
print("1.covid19 affected in chennai")
print("2.covid19 affected in Trichy")
print("3.covid19 affected in Tuticorin")
print("4.covid19 affected in Tirunelveli")
print("5.covid19 affected in Madurai")
def chennai(percenttage,temperature):
    if percenttage>=90 or temperature<=50:
        if percenttage<70:
            print("chennai government hospital vaccancy is 100")
            print("chennai private hospital vaccancy is 150")
            print("patient temperature is 50 degree")
        elif percenttage>=80:
            print("chennai government hospital vaccancy is 170")
            print("chennai private hospital vaccancy is 100")
            print("patient temperature is 60 degree")
        elif percenttage<50:
            print("chennai government hospital vaccancy is 95")
            print("chennai private hospital vaccancy is 70")
            print("patient temperature is 90 degree")
    else:
        print("sorry! No hospital vaccancy")
def Trichy(percenttage,temperature):
    if percenttage>70 or temperature>=80:
        if percenttage>=95:
            print("Trichy government hospital vaccancy is 120")
            print("Trichy private hospital vaccancy is 100")
            print("patient temperature is 98 degree")
        elif percenttage<80:
            print("Trichy government hospital vaccancy is 75")
            print("Trichy private hospital vaccancy is 130")
            print("patient temperature is 75 degree")
        elif percenttage<50:
            print("Trichy government hospital vaccancy is 150")
            print("Trichy private hospital vaccancy is 98")
            print("patient temperature is 65 degree")
    else:
        print("sorry! No hospital vaccancy")
def Tuticorin(percenttage,temperature):
    if percenttage>=80 or temperature>=90:
        if percenttage>65:
            print("Tuticorin government hospital vaccancy is 75")
            print("Tuticorin private hospital vaccancy is 55")
            print("patient temperature is 75 degree")
        elif percenttage<50:
            print("Tuticorin government hospital vaccancy is 60")
            print("Tuticorin private hospital vaccancy is 45")
            print("patient temperature is 45 degree")
        elif percenttage>50:
            print("Tuticorin government hospital vaccancy is 25")
            print("Tuticorin private hospital vaccancy is 50")
            print("patient temperature is 55 degree")
    else:
        print("sorry! No hospital vaccancy")
def Tirunelveli(percenttage,temperature):
    if percenttage>=90 or temperature<=78:
        if percenttage>70:
            print("Tirunelveli government hospital vaccancy is 120")
            print("Tirunelveli private hospital vaccancy is 170")
            print("patient temperature is 69 degree")
        elif percenttage<80:
            print("Tirunelveli government hospital vaccancy is 95")
            print("Tirunelveli private hospital vaccancy is 100")
            print("patient temperature is 70 degree")
        elif percenttage<40:
            print("Tirunelveli government hospital vaccancy is 45")
            print("Tirunelveli private hospital vaccancy is 39")
            print("patient temperature is 95 degree")
    else:
        print("sorry! No hospital vaccancy")
def Madurai(percenttage,temperature):
    if percenttage>50 or temperature<60:
        if percenttage>=95:
            print("Madurai government hospital vaccancy is 65")
            print("Madurai private hospital vaccancy is 70")
            print("patient temperature is 60 degree")
        elif percenttage<80:
            print("Madurai government hospital vaccancy is 100")
            print("Madurai private hospital vaccancy is 110")
            print("patient temperature is 58 degree")
        elif percenttage<40:
            print("Madurai government hospital vaccancy is 75")
            print("Madurai private hospital vaccancy is 150")
            print("patient temperature is 80 degree")
    else:
        print("sorry! No hospital vaccancy")
user=int(input("enter your number:"))
if user==1:
    percenttage=int(input("enter your percenttage:"))
    temperature=int(input("enter your patient temperature:"))
    chennai(percenttage,temperature)
elif user==2:
    percenttage=int(input("enter your percenttage:"))
    temperature=int(input("enter your patient temperature:"))
    Trichy(percenttage,temperature)
elif user==3:
    percenttage=int(input("enter your percenttage:"))
    temperature=int(input("enter your patient temperature:"))
    Tuticorin(percenttage,temperature)
elif user==4:
    percenttage=int(input("enter your percenttage:"))
    temperature=int(input("enter your patient temperature:"))
    Tirunelveli(percenttage,temperature)
elif user==5:
    percenttage=int(input("enter your percenttage:"))
    temperature=int(input("enter your patient temperature:"))
    Madurai(percenttage=100,temperature=50)
else:
    ("No! available hospitals vaccancy" )
    import mysql.connector
    sathya=mysql.connector.connect(
        host="localhast",
        user="root",
        password="12345",
        database="covid",
    )
    mycursor=sathya.cursor()
    #mycursor.execute("create table covid_details(state_name varchar(225),possitive int,negative int,vaccination_completed_peoples int,death int)")
    sathya.commit()
    print("completed")    




