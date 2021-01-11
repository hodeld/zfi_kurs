#! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.
import random
from pathlib import Path
import os
   # The quiz data. Keys are states and values are their capitals.
capitals = {'Aargau': 'Aarau',
 'Appenzell Innerrhoden': 'Appenzell',
 'Appenzell Ausserrhoden': 'Herisau',
 'Basel-Land': 'Liestal',
 'Basel-Stadt': 'Basel',
 'Bern': 'Bern',
 'Fribourg': 'Fribourg',
 'Genève': 'Genève',
 'Glarus': 'Glarus',
 'Graubünden': 'Davos',
 'Jura': 'Delémont',
 'Luzern': 'Luzern',
 'Neuchâtel': 'Neuchâtel',
 'Nidwalden': 'Stans',
 'Obwalden': 'Sarnen',
 'Schaffhausen': 'Schaffhausen',
 'Schwyz': 'Schwyz',
 'Solothurn': 'Solothurn',
 'St.Gallen': 'St. Gallen',
 'Thurgau': 'Frauenfeld',
 'Ticino': 'Bellinzona',
 'Uri': 'Altdorf',
 'Valais': 'Sion',
 'Vaud': 'Lausanne',
 'Zug': 'Zug',
 'Zürich': 'Zürich',
            }
#create folder
cwd = Path.cwd()
quiz_path = cwd / 'quizes'

try:
    os.makedirs(quiz_path)  # create folder
except FileExistsError:
    pass

# Generate X quiz files.
for quizNum in range(5):
# Create the quiz and answer key files.
    quizFile = open(Path(quiz_path, f'capitalsquiz{quizNum + 1}.txt'), 'w')
    answerKeyFile = open(Path(quiz_path, f'capitalsquiz_answers{quizNum + 1}.txt'), 'w')
    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    # Loop through all 50 states, making a question for each.

    for questionNum in range(26):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
            # Write the question and the answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n")
            quizFile.write('\n')
        # Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()