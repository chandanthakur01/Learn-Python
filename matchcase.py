x =int(input("enter the value of x: "))
match x:
    #if x is 0
    case 0 :
        print("x is 0 ")
    #if x is 2
    case 2 :
        print("x is 2")
    #if x is anything
    case _:
        print(x)
        
