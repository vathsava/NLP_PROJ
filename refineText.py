###################################################
#This file contains functions that refine the text
###################################################
import nltk
from string import maketrans
from nltk.tokenize import sent_tokenize
def getSentencesFromStory(completeText):
    story = completeText.split("TEXT:")
    #lines = sent_tokenize(story[1]);
    sentences= sent_tokenize(story[1]);
  #  for line in lines:
   #     l = line.replace("\n", " ")
    #    l2 = removeExtraSpaces(l)
     #   sentences.append(l2)
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

def removeSpecialCharacters(string1):
    chars = "!@#$%^&*()[]{};:,./<>?\|`~-=_+"
    repChars = "                              "
    trantab = maketrans(chars,repChars);
    st = string1.translate(trantab)
    return st

def removeExtraSpaces(string1):
    string2 = " ".join(string1.split())
    return string2

def getWordsInString(fullString):
        repString = removeSpecialCharacters(fullString)
        repString2 = removeExtraSpaces(repString)
        words = repString2.split(" ")
        return words
