###################################################
#This file contains functions that refine the text
###################################################
from string import maketrans
from nltk.tokenize import sent_tokenize
<<<<<<< HEAD
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

=======
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopset=[];
>>>>>>> 4ff15b45fe8de154fc1f9b27ba338040a698e825
def getSentencesFromStory(completeText):
    story = completeText.split("TEXT:")
    stopset=set(stopwords.words('english'));
    #lines = sent_tokenize(story[1]);
    lines = sent_tokenize(story[1]);
    #lines2 = sent_tokenize(completeText)
    sentences = []
    for line in lines:
        l = line.replace("\n", " ")
        l2 = removeExtraSpaces(l)
        sentences.append(l2)
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
<<<<<<< HEAD
        #repString = removeSpecialCharacters(fullString)
        #repString2 = removeExtraSpaces(repString)
        #words = repString2.split(" ")
        stopset = set(stopwords.words('english'))
        wds = word_tokenize(fullString)
        words = [w for w in wds if not w in stopset]
        return words
=======
    
        # repString = removeSpecialCharacters(fullString)
        #repString2 = removeExtraSpaces(repString)
        #words = repString2.split(" ")
        sa=word_tokenize(fullString)
        sa = [w for w in sa if not w in stopset]
        return sa
>>>>>>> 4ff15b45fe8de154fc1f9b27ba338040a698e825
