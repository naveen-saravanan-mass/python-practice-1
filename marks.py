print()
print()
print()
print("*********************")
print("+1 - GROUP SUGGESTION")
print("*********************")
print()
print()


print("ENTER YOUR SUBJECT MARKS")
print("________________________")

print()

print()

print()

t=int(input("ENTER YOUR TAMIL MARK         :"))
print()
e=int(input("ENTER YOUR ENGLISH MARK       :"))
print()
m=int(input("ENTER YOUR MATHS MARK         :"))
print()
s=int(input("ENTER YOUR SCIENCE MARK       :"))
print()
ss=int(input("ENTER YOUR SOCIAL-SCIENCE MARK:"))
print("____________________________________")

#total calclation

total=(t+e+m+s+ss)
print()
print("                     total:",total,"/500")
print("____________________________________")

print()

#avarage calculation

avarage=total/5

print()

print("your avrage mark:",avarage)
print()


if(t and e and m and s and ss>=35):
    if(avarage>=35.0 and avarage<50.0):
        print("your eligible for arts!")
    elif(avarage>=50.0 and avarage<75.0):
        print("your eligible for maths-computer!")
    elif(avarage>=75.0 and avarage<100.0):
        print("your eligible for maths-biology")
else:
    if(t and e and m and s and ss<35):
        print("currently your not eligible for any groups")
        if(t<35):
            print("you should pass tamil")
        if(e<35):
            print("you should pass english")
        if(m<35):
            print("you should pass maths")
        if(s<35):
            print("you should pass science")
        if(ss<35):
            print("you should pass social-science")




