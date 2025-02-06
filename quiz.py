import random
level=int(input("enter the level'1= easy or 2= hard : "))
if level==1:
    b=random.randint(1,20)
    a=random.choice("+-*/")
    c=random.randint(1,10)

    print (b)
    print(a) 
    print(c)
    if a=="+":    
        e=b+c
    elif a=="-":
        e=b-c
    elif a=="*":
        e=b*c
    elif a=="/":
        e=b/c
    
    # user in put
    user=float(input("enter your answer: "))
    if user==e:
        print("you are correct")
    else:
        print("you are wrong plese try again")

elif level==2:
    b=random.randint(1,100)
    a=random.choice("+-*/")
    c=random.randint(1,100)

    print (b)
    print(a) 
    print(c)
    if a=="+":    
        e=b+c
    elif a=="-":
        e=b-c
    elif a=="*":
        e=b*c
    elif a=="/":
        e=b/c
    
    # user in put
    user=float(input("enter your answer: "))
    if user==e:
        print("you are correct")
    else:
        print("you are wrong plese try again")
