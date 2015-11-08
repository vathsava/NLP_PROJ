from jaccard import calcJaccard

def getSentencesFromStory(completeText):
    story = completeText.split("TEXT:")
    sentences = story[1].split(".")
    return sentences

def getQuestionsFromFile(completeText):
    questions = []
    for line in completeText:
        if line.find("Question: ") == 0:
            questions.append(line)
    return questions


def generateAnswers(story,questions):
    sentences = getSentencesFromStory(story)
    questions = getQuestionsFromFile(questions)
    
    maxd=0;
    ans="bbb";
    for q in questions:
        for s in sentences:
            f=calcJaccard(q, s);
            if maxd<f:
                ans=s;
                maxd=f;
        print q;
        print ans;
        maxd=0.0;
    ans="";