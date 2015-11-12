from __future__ import division
from printingText import printQuestion, printQuestionIDtoFile
from printingText import printAnswer, printAnswerToFile
from refineText import getWordsInString
from nltk.stem.snowball import SnowballStemmer

def jaccardDistance(quesWords,sentWords):
    stemmer = SnowballStemmer("english");
    match = 0
    nonMatch = 0
    for qw in quesWords:
        for aw in sentWords:
            if stemmer.stem(qw) == stemmer.stem(aw) :
                match += 1
            else:
                nonMatch += 1
    return (match)

def highestFrequency(quesWords,sentWords):
    stemmer = SnowballStemmer("english");
    match = 0
    nonMatch = 0
    for qw in quesWords:
        for aw in sentWords:
            if stemmer.stem(qw) == stemmer.stem(aw) :
                match += 1
            else:
                nonMatch += 1
    return (match)

def generateAnswersUsingJaccard(questions, sentences):
    maxd=0;
    ##############################################################################
    #q is a list, 0th element contains Question ID, 1st element contains question
    # and 2nd element contains difficulty rating
    ##############################################################################
    for q in questions:
        if len(q) < 3:
            #raise Err('Error in Extracting Question')
            continue
        qID = q[0] 
        quesString = q[1]
        quesWords = getWordsInString(quesString)
        
        ans = ""
        maxd = 0 
        for s in sentences:
            sentWords = getWordsInString(s)
            f = highestFrequency(quesWords, sentWords)
            if maxd<f:
                ans = s
                maxd = f
        
        answers = []        
        for s in sentences:
            sentWords = getWordsInString(s)
            f = highestFrequency(quesWords, sentWords)
            if maxd == f:
                answers.append(s)
                
        printQuestion(quesString)
        printQuestion(q[2])
        for an in answers:
            printAnswer(an)
        
        printQuestionIDtoFile(qID)
        printAnswerToFile(ans)
        print "\n"
