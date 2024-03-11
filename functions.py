import json

def add(filename,ques: str,opt,correct_opt:str):
    new_data = {
        "question": ques,
        "correct": correct_opt,
        "options":{
            "A": opt[0],
            "B": opt[1],
            "C": opt[2],
            "D": opt[3]
        }
    }

    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["quiz"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def remove(filename):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        quiz = file_data["quiz"]
        
        for i in range(len(quiz)):
            print(str(i+1)+".",quiz[i]["question"])

        idx_del = (int(input("Enter which question number you want to remove: ")))-1
        quiz.remove(quiz[idx_del])
        file.close()
    with open(filename,"w") as f:
        f.seek(0)
        json.dump(file_data,f,indent=4)

def showResults(filename):
    # fully done
    with open(filename, "r") as file:
        results = json.load(file)["results"]
        for i in range(len(results)):
            print(f"{i+1})  {results[i]["name"]} (Roll Number - {results[i]["rollNum"]}) Scored: {results[i]["score"]}")

def changePass(filename,passw):
    with open(filename,"r+") as file:
        data = json.load(file)
        data["password"] = passw
    with open(filename,"w") as f:
        f.seek(0)
        json.dump(data,f,indent=4)

def quiz(roll_name,name,filename):
    total = 0
    with open(filename,"r") as file:
        quiz = json.load(file)["quiz"]
        if(len(quiz) == 0):
            print("No questions added yet!")
            return
        for i in range(len(quiz)):
            print(f"{i+1} {quiz[i]["question"]}\n A) {quiz[i]["options"]["A"]}\t\tB) {quiz[i]["options"]["B"]}\t\tC) {quiz[i]["options"]["C"]}\t\tD) {quiz[i]["options"]["D"]}")
            answer = (input("Enter your option(A/B/C/D): ")).upper()
            if(answer == quiz[i]["correct"]):
                total+=1
    with open(filename,"r+") as f:
        file_data = json.load(f)
        file_data["results"].append({
            "rollNum": roll_name,
            "name": name,
            "score": total
        })
        f.seek(0)
        json.dump(file_data,f,indent = 3)
    return total,len(file_data["quiz"])
