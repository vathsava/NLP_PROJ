def printQuestion(question):
    q = "Question: " + question
    print q
    
def printDifficulty(question):
    q = "Difficulty: " + question
    print q
    
def printAnswer(answer):
    a = "Answer: " + answer
    print a
    
def printQuestionID(qID):
    q = "QuestionID: " + qID
    print q
    
def printQuestionIDtoFile(qID):
    q = "QuestionID: " + qID + "\n"
    wPrint(q)
    
def printAnswerToFile(answer):
    a = "Answer: " + answer + "\n"
    wPrint(a)
    
def wPrint(s):
    with open("answers.txt", "a") as myfile:
        myfile.write(s)