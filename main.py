import time
h = int(input("Enter time"))
if 5<=h<12:
    print("Good morning")
elif 12<=h<16:
    print("Good afternoon")
elif 16<=h<20:
    print("Good evening")
else:
    print("Good night")