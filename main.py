import functions as fn
import json
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Quiz'))

inp = input("1. Student\n2. Teacher\n")
if(inp == "1"):
    print("\n----- QUIZ STARTS NOW! -----")
    name = input("Enter you name: ")
    roll_num = input("Enter you roll number: ")
    tup = fn.quiz(roll_num,name,'quiz.json')
    print("Your score:",tup[0],"\nTotal Questions:",tup[1])
elif(inp == "2"):
    with open('quiz.json',"r") as f:
      data = json.load(f)
      if(data["password"]):
            passw = input("Enter password to access panel: ")
            if(passw == data["password"]):
                util = input("1. Add questions\n2. Remove questions\n3. Show Results\n4. Change panel password")
                if(util == "1"):
                    ques = input("Enter the question: ")
                    options = [input("Enter option A: "),input("Enter option B: "),input("Enter option C: "),input("Enter option D: ")]
                    correct_opt = (input("Enter which is the correct option (A,B,C,D): ")).upper()
                    fn.add('quiz.json',ques,options,correct_opt)
                    print("Question Added!!")
                if(util == "2"):
                    fn.remove('quiz.json')
                if(util == "3"):
                    fn.showResults('quiz.json')
                if(util == "4"):
                    passw = input("Enter the new password for panel: ")
                    fn.changePass('quiz.json',passw)
            else:
              print("INCORRECT PASSWORD")      