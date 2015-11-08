#####################################################################################################
#This file will contain function calls to various methods that we will implement to generate answers
#####################################################################################################

from refineText import getSentencesFromStory
from refineText import getQuestionsFromFile
from jaccard import generateAnswersUsingJaccard

def generateAnswers(story,questions):
    sentences = getSentencesFromStory(story)
    questions = getQuestionsFromFile(questions)
    
    generateAnswersUsingJaccard(questions, sentences)