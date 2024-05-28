questions=[
    ("which fruit is red in color?", ("a) apple","b) orange","c) mango","d) bannana"),"a"),
    ("who was future prime minister of india?", ("a) ashish","b) rahul","c) roshan","d)chandan"),"d")
]

for question,options,answer in questions:
    print(question)
    for option in options:
        print(option)
        
    user_answer=input("please enter your answer  :")
    # print(user_answer)
    if user_answer==answer:
        print("correct answer\n")
    
    else:
        print(f"worng answer correnct answer is,{answer}\n")
        print("you missed your chance\n thanks for participate ")
        break
        
    