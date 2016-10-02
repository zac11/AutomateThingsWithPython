#randomquiz generator- Creates quizes with questions and answers in random order , along with an answer key
#! python3
import random
capitals={'Alabama':'Montgomery',
          'Alaska':'Juneau',
          'Arizona':'Phoenix',
          'Arkansas':'Little Rock',
          'California':'Sacremento',
          'Colorado':'Denver',
          'Connecticut':'Hartford',
          'Delaware':'Dover',
          'Florida':'Tallahassee',
          'Georgia':'Atlanta',
          'Hawaii':'Honolulu',
          'Idaho':'Boise',
          'Illinois':'Springfield',
          'Indiana':'Indianapolis',
          'Iowa':'Des Moines',
          'Kansas':'Topeka',
          'Kentucky':'Frankfort',
          'Louisiana':'Baton Rouge',
          'Maine':'Augusta',
          'Maryland':'Annapolis',
          'Massachusetts':'Boston',
          'Michigan':'Lansing',
          'Minnesota':'Saint Paul',
          'Mississippi':'Jackson',
          'Missouri':'Jefferson City',
          'Montana':'Helena',
          'Nebraska':'Lincoln',
          'Nevada':'Carson City',
          'New Hampshire':'Concord',
          'New Jersey':'Trenton',
          'New Mexico':'Santa Fe',
          'New York':'Albany',
          'North Carolina':'Raleigh',
          'North Dakota':'Bismarck',
          'Ohio':'Columbus',
          'Oklahoma':'Oklahoma City',
          'Oregon':'Salem',
          'Pennsylvania':'Harrisburg',
          'Rhode Island':'Providence',
          'South Carolina':'Columbia',
          'South Dakota':'Pierre',
          'Tennessee':'Nashville',
          'Texas':'Austin',
          'Utah':'Salt Lake City',
          'Vermont':'Montpelier',
          'Virginia':'Richmond',
          'Washington':'Olympia',
          'West Virginia':'Charleston',
          'Wisconsin':'Madison',
          'Wyoming':'Cheyenne'}

#This part will generate 35 quiz files

for quiznum in range(35):

    #Todo : Create the quiz files
    quizFile=open('/home/zac/Documents/capitalsquiz%s.txt' % (quiznum+1),'w')
    answerKeyFile = open('/home/zac/Documents/captialsquiz_answers%s.txt' % (quiznum+1),'w')


    #Todo : Write out a header for the quiz files
    quizFile.write('Name of Student : \n\nPeriod :\n\n')
    quizFile.write((''*20) + 'State Capitals Quiz (Form%s)' % (quiznum+1))
    quizFile.write('\n\n')

    #Todo : Shuffle order of the states
    states=list(capitals.keys())
    random.shuffle(states)

    #Todo : Loop through the states, making a question for each
    for questionNum in range(50):
        #Todo : Get Right and Wrong Answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #Todo : Write the question and answer options to quiz files
        quizFile.write('%s. What is the capital of %s? \n' % (questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write('    %s.  %s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')


        #Todo: Write the answer to file
        answerKeyFile.write('%s.   %s \n' %(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))


quizFile.close()
answerKeyFile.close()