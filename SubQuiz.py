import random
import time

correctCount = 0 # count the correct answers
count = 0 # how many questions have been asked
NUMBER_OF_QUESTIONS = 5

startTime = time.time() #get the start time

while count < NUMBER_OF_QUESTIONS:
    # 1. Generate two random single-digit integers
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)

    # 2. If number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # 3. Prompt the student to answer "What is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " - " + str(number2)+"? "))

    # 4. Check the answer and display the result

    if answer == number1 - number2:
        print("You are correct!")
        correctCount += 1

    else:
        print("Your answer is wrong!")
        print(str(number1) + " - " + str(number2) + ' = ' + str(number1-number2))

    count += 1

endTime = time.time()
testTime = int(endTime - startTime)
print("Correct count is", correctCount, "out of", NUMBER_OF_QUESTIONS)
print("Test time was", testTime, "seconds")