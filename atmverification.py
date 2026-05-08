
print("welcome")
print()
print()
set_password=1234
available_balance=10000


password=int(input("enter your password:"))

def pin_change(a):
           set_password=a
           return print("password has been changed, now your password is ",a)
           
print()

if(password==set_password):
    print("CHOOSE YOUR NEED")
    amount=1
    print("amount widraw prees - 1")
    balance=2
    print("balance enquiry press - 2")
    pin=3
    print("pin chance press - 3")
    user=int(input("enter valid input  :"))
    if(user==amount):
        enter_balance=int(input("enter amount:"))
        if(enter_balance<=available_balance):
            print("available notes")
            total_notes=enter_balance//500
            choose_note_500=1
            print("500 x",total_notes,"=",enter_balance)
            if(choose_note_500==1):
                print("take cash")
            else:
                print("invalid input")
        else:
            print("insufficent blance")
    elif(user==balance):
        print("available balance:",available_balance)
    elif(user==pin):
        old_password=int(input("enter your old password   :"))
        if(old_password==set_password):
            new_password=int(input("enter your new password  :"))
            pin_change(new_password)
        else:
            print("password incorrect")
            
        
else:
    print("invalid password")
