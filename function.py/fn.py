def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is" , sum / len(numbers))
    
average(5, 6)  

# def add(num1, num2, num3):
#     i =0
#     i =sum(num1+num2+num3)
#     print(i)

# add(10, 20, 30)
