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
                    qID = lines[count].split(": ")
                    ques = lines[count+1].split(": ")
                    diff = lines[count+2].split(": ")
                    questionRow.append(qID[1].rstrip())
                    questionRow.append(ques[1].rstrip())
                    questionRow.append(diff[1].rstrip())
                count += 1
            count += 1
        count += 1        
        questions.append(questionRow)
    return questions