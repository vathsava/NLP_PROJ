import sys
from refineText import generateAnswers

#########################################################
#Reading the list of stories from input file
inputFile = sys.argv[1]

f = open(inputFile)

lineCount = 0
stories = []
for line in f:
    l = line.rstrip()
    if lineCount == 0:
        filesPath = l
    else:
        stories.append(l)
    lineCount += 1
# End of Reading the list of stories from input file
#########################################################


#########################################################
#Reading each story and corresponding question file
for eachStory in stories:
    storyFile = filesPath + eachStory + ".story"
    fStory = open(storyFile)
    story = fStory.read()
    
    questionsFile = filesPath + eachStory + ".questions"
    questions = open(questionsFile)
    generateAnswers(story, questions)
# End of Reading each story and corresponding question file
#########################################################