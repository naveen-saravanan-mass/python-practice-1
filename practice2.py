#odd or even

"""a=int(input("enter the number:"))

if(a%2==0):
    print("your number id even")
else:
    print("your number is odd")


if(a>=0):
    print("positive number")

else:
    print("negative number")"""


#leap year finding

"""b=int(input("enter the year:"))

if(b%400==0 or b%4==0):
    if(b%100!=0):
        print(b,"is leap year")
    else:
        print(b,"is not leap year")
else:
    print(b,"is not leap year")"""

#vowvels finging

"""c=input("enter your alphabet:")
if(c=="a" or c=="e" or c=="i" or c=="o" or c=="u"):
    print(c,"is vowvels")
else:
    print(c,"is not vowels")"""

#season finding based

"""d=input("enter the month:")

if(d=="dec" or d=="jan" or d=="feb"):
    print("winter season")
elif(d=="march" or d=="april" or d=="may"):
    print("summer season")
elif(d=="june" or d=="july" or d=="aug" or d=="sep"):
    print("moonsoon season")
elif(d=="oct" or d=="nov"):
    print("autmn season")"""

#max num min num

"""e=int(input("enter the first number:"))
f=int(input("enter the second number:"))

if(e==f):
    print("nimber is equal")
if(e>f):
    print(e,"is max number",f,"is min")
else:
    print(f,"is max",e,"is min")"""

#days finding based on month

"""f=input("enter the month:")
if(f=="jan" and "march" and "may" and "july" and "aug" and "oct" and "dec"):
    print("31 days in ",f," month")
elif(f=="nov" and "sep" and "june" and "april"):
    print("30 days in ",f," month")
elif(f=="feb"):
    b=int(input("enter the year:"))
    if(b%400==0 or b%4==0):
        if(b%100!=0):
            print("29 days in ",f," month")
        else:
            print("28 days in ",f," month")
    else:
        print("28 days in ",f," month")"""
#multiple of 5

num=int(input("enter the input"))

if num%5==0:
    print("hello")
else:
    print("bye")


#water boing

temp=float(input("enter temp:"))

if temp>100:
    print("water id boiling")
else:
    print("water is not boiling")

#libarary charge calculatoin

days=int(input("enter the number of days:"))

if days<=5:
    print(days*2,"is your charge")
elif days<=10:
    print(days*3,"is your charge")
elif days<=15:
    print(days*4,"is your charge")
elif days<=10:
    print(days*5,"is your charge")


#police eligiblity

age=int(input("enter the age:"))
height=float(input("enter the height in cm:"))

if age>=18 and age<=25 and height>=165:
    print("eligible")
else:
    print("not eligible")

#employee bonus calculation

salary=float(input("enter salary:"))
years=int(input("enter years of services:"))

if years>5:
    print(salary*0.10,"is your bounus")
else:
    print(salary*0.5,"is your bounus")

#electricity bill

units=int(input("enter units consumed:"))

if units<=100:
    print(units*1.5,"is your bill")
elif units<=200:
    bill=100*1.5+(units-100)*2.5
elif units<=300:
    bill=100*1.5+100*2.5+(units-200)*4
else:
    bill=100*1.5+100*2.5+100*4+(units-300)*6

print("your bill is",bill)


    
    

    
