###################################################
#This file contains functions that refine the text
###################################################
def getSentencesFromStory(completeText):
    story = completeText.split("TEXT:")
    sentences = story[1].split(".")
    return sentences

def getQuestionsFromFile(completeText):
    lines = []
    for line in completeText:
        lines.append(line)
    
    questions = []    
    count = 0
    while (count < len(lines)):
        questionRow = []
        if lines[count].find("QuestionID: ") == 0:
            if lines[count + 1].find("Question: ") == 0:
                if lines[count + 2].find("Difficulty: ") == 0:
                    qID = lines[count].split(": ")[1].rstrip()
                    ques = lines[count+1].split(": ")[1].rstrip()
                    diff = lines[count+2].split(": ")[1].rstrip()
                    questionRow.append(qID)
                    questionRow.append(ques)
                    questionRow.append(diff)
                    questions.append(questionRow)
                count += 1
            count += 1
        count += 1        
        
    return questions