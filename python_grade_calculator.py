#Create Calculator that gives average test score.


def inputscore() :
    print ('Enter Student ID :')
    id=int (input ())
    print ('Enter Exam Score: ')
    exam=int(input())
    print ('Enter All Test Scores:')
    score1=int (input())
    score2=int (input())
    score3=int (input())
    score4=int (input())
    score5=int (input())
    sum=(score1+score2+score3+score4+score5)
    avge=sum/5
    print('Test Average Is :' +str(avge))
    print('Final score is: ', compute_score(avge,exam))
    print('Letter Grade is: ',gradevalue(compute_score(avge,exam)))
    print_message(gradevalue(compute_score(avge,exam)))
    return avge
def compute_score (avge,exam):
    final_score=0.4*avge+0.6*exam
    return final_score
def gradevalue(final_score):
    if 90<=final_score<=100:
        grade='A'
    elif 80<=final_score<=89:
        grade='B'
    elif 70<=final_score<=79:
        grade='C'
    elif 60<=final_score<=69:
        grade='D'
    else:
        grade='F'
    return grade
def print_message(grade):
    if grade=='A':
        print('message : Excellent')
    elif grade=='B':
        print('message : Good')
    elif grade=='C':
        print('message : Satisfactory')
    elif grade=='D':
        print('message : Average')
    elif grade=='F':
        print('message : Poor')
    inputscore()

