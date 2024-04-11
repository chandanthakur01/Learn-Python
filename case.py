x =int(input("enter the value of x: "))
match x:
    #if x is 0
    case 0 :
        print("x is 0 ")
    #if x is 2
    case 2 :
        print("x is 2")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    
    #if x is anything
    case _:
        print(x)
        
