import random

#This quiz compiles a list of Indian CM's and gives various randomized options in selecting the CM's for a correct
#state

chief_ministers={'Andhra Pradesh':'N Chandrababu Naidu',
                 'Arunachal Pradesh':'Pema Khandu',
                 'Assam':'Sarbananda Sonowal',
                 'Bihar':'Nitish Kumar',
                 'Chattisgarh':'Raman Singh',
                 'Delhi':'Arvind Kejriwal',
                 'Goa':'Laxmikant Parsekar',
                 'Gujarat':'Vijay Rupani',
                 'Haryana':'Manohar Lal Khattar',
                 'Himachal Pradesh':'Vir Bhadra Singh',
                 'Jammu And Kashmir':'Mehbooba Mufti',
                 'Jharkhand':'Raghubar Das',
                 'Karnataka':'Siddharamiah',
                 'Kerala':'Pinrayi Vijayan',
                 'Madhaya Pradesh':'Shivraj Singh Chouhan',
                 'Maharastra':'Devendra Fadnavis',
                 'Manipur':'Okram Ibobi Singh',
                 'Meghalaya':'Mukul Sangama',
                 'Mizoram':'Lal Thanhawla',
                 'Nagaland':'T.R. Zeliang',
                 'Odisha':'Naveen Patnaik',
                 'Pondicherry':'V Narayanswamy',
                 'Punjab':'Prakash Singh Badal',
                 'Rajasthan':'Vasundhara Raje',
                 'Sikkim':'Pawan Kumar Chamling',
                 'Tamil Nadu':'J Jayalalithaa',
                 'Telengana':'N Chandra Sekhar Rao',
                 'Uttar Pradesh':'Akhilesh yadav',
                 'Uttarakhand':'Harish Rawat',
                 'West Bengal':'Mamata Banarjee'}

for quizNum in range(10):

    #Todo : Create the quiz files
    cmquizfile=open('/home/zac/Documents/quiz/cmquiz%s.txt' %(quizNum+1),'w')
    cmquizAnsFile = open('/home/zac/Documents/quiz/cmquiz_answer%s.txt' %(quizNum+1),'w')

    #Todo : Writing the header for the quiz
    cmquizfile.write('Name of the Student : \n\n Roll Number : \n\n Registration Number : \n\n')
    cmquizfile.write((''*20) + 'State Chief Minister Quiz (Form%s)' %(quizNum+1))
    cmquizfile.write('\n\n')

    #Todo : Shuffle the order of CM's
    state_cm=list(chief_ministers.keys())
    random.shuffle(state_cm)


    #Todo : Loop through the options and select correct answer
    for questionNum in range(30):
        #Todo : Get the correct answer
        correctAnswer = chief_ministers[state_cm[questionNum]]
        wrongAnswer = list(chief_ministers.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        answerOptions = wrongAnswer +[correctAnswer]
        random.shuffle(answerOptions)


        #Todo : Write the question and answer options to the file
        cmquizfile.write('%s.    Who is the Chief Minister of  %s \n' %(questionNum+1, state_cm[questionNum]))
        for i in range(4):
            cmquizfile.write('          %s.  %s\n ' %('ABCD'[i], answerOptions[i]))
        cmquizfile.write('\n')



        #Todo : Write the answer key to the file
        cmquizAnsFile.write('%s.     %s \n' %(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))



cmquizfile.close()
cmquizAnsFile.close()