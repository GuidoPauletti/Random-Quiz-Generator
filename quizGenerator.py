#! Python 

'''
generates 20 quizes of 50 multiple choice questions, 
every one of them with different
order of questions and possible answers.
'''

import random 

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quizNum in range(1, 21):
    quizFile = open(f'C:\\Users\\guido\\MyPythonScripts\\menAtWork\\capitalquiz{quizNum}.txt', 'w')
    answerKeyFile = open(f'C:\\Users\\guido\\MyPythonScripts\\menAtWork\\capitalquiz_answers{quizNum}.txt', 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(('' * 20) + f'State Capitals Quiz {quizNum}\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        #get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #Write the question and the answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}\n')
        for i in range(4):
            quizFile.write(f'  {"ABCD"[i]}. {answerOptions[i]}\n')
        quizFile.write('\n')

        #Write the answer key to a file.
        answerKeyFile.write(f'{questionNum + 1}: {"ABCD"[answerOptions.index(correctAnswer)]}\n')
    
    quizFile.close()
    answerKeyFile.close()
