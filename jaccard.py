from __future__ import division

def jaccardDistance(quesString,ansString):
    wordsInQues = quesString.split(" ");
    wordsInAns = ansString.split(" ");
    
    match = 0
    nonMatch = 0
    for qw in wordsInQues:
        for aw in wordsInAns:
            if qw == aw :
                match+=1
            else:
                nonMatch += 1
    return (match/(match + nonMatch))

def generateAnswersUsingJaccard(questions, sentences):
    maxd=0;
    ##############################################################################
    #q is a list, 0th element contains Question ID, 1st element contains question
    # and 2nd element contains difficulty rating
    ##############################################################################
    for q in questions:
        if len(q) < 3:
            continue 
        ques = q[1]
        ans = ""
        maxd = 0 
        for s in sentences:
            f = jaccardDistance(ques, s)
            if maxd<f:
                ans = s
                maxd = f
        print ques
        print ans



    