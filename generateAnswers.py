from refineText import getSentencesFromStory
from refineText import getQuestionsFromFile
from jaccard import generateAnswersUsingJaccard

def generateAnswers(story,questions):
    sentences = getSentencesFromStory(story)
    questions = getQuestionsFromFile(questions)
    
    generateAnswersUsingJaccard(questions, sentences)