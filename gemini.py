import time 
score = 0
player_name = ("Input your name:")
print(player_name + "!Lets test your knowledge")
print("you wil get 10 points fro each correct answer")
time.sleep(1)
questions [
    {
        "question":"1. what is the output of (2==3)?"
        "Options":"a.6/n b.8 c.7"
        "answer":"b"
    }
    {
       "question":"what is the square of 2"
        "Options":"a.4/n b.40 c.6"
        "answer":"a" 
    }
    {
       "question":"what is the square of 4"
        "Options":"a.15/n b.4 c.16"
        "answer":"c"  
    }
    {
        "question":"what is 2+3"
        "Options":"a.15/n b.5 c.16"
        "answer":"b"  
    }
    {
        "question":"what is 56-678796897"
        "Options":"a.-678796897/n b.5 c.16"
        "answer":"a"  
    }

]
for q in questions:
    print("/n"["questions"])
    for options in q["options"]:
        print(option)

        while True
        ans = input("enter your answer a/b/c").upper()
        if ans in ["a","b","c"]