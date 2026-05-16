import random
def FizzBuzz(number, useranswer):
    iscorrect = False
    isdivisable3 = number % 3== 0
    isdivisable5 = number % 5== 0
    if (isdivisable3 and isdivisable5):
        iscorrect = useranswer == "Fizzbuzz"
    elif(isdivisable3):
        iscorrect = useranswer == "Fizz"
    elif(isdivisable5):
        iscorrect = useranswer =="Buzz"
    else:
        iscorrect = useranswer == (str(number))
    return iscorrect 
turn = 1
myscore = 0 
computerscore = 0
for i in range (10):
    number = random.randint(0,100)
    print("the number is: " + str(number) )
    ismyturn = turn % 2 == 1
    turn += 1
    if (ismyturn):
        myanswer =  (str(input()))
        iscorrect = FizzBuzz(number, myanswer) 
        if ( iscorrect == False):
            print ("The answer is incorrect: ❌")
        elif iscorrect == True:
            print("The answer is correct:✅")
            myscore += 1 
    else:
        print("it's the computers turn")
        iscomputercorrect = random.randint(0,1)
        if(iscomputercorrect):
            print("The computer is correct:✅")
            computerscore += 1
        else:
            print ("The answer is incorrect:❌")
    print ("My score: " + str(myscore))
    print ("Computer score: " + str(computerscore))
    print("---")
    