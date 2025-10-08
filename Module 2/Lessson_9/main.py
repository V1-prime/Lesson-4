from questions import quiz
import os



def simple_quiz():
    correct_answers_count = 0

    for question, answers in quiz.items():
        print()
        user_answer = input(question)
        if user_answer in answers:
            correct_answers_count += 1  
            print(f"You answered {correct_answers_count} questions correctly out of {len(quiz)}!")
    print(f"Thanks for playing!")



with open("hello.txt","w") as file:
    file.write("Varvara" "\n")
    file.write("Art" "\n")
    file.write("Spaghetti" "\n")
    
with open("hello.txt","r") as file:
    text = file.read()
    print(text)