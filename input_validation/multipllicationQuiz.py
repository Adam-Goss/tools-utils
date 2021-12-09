#! python3

import pyinputplus as pyip
import random, time

numberOfQuestions = 3
correctAnswers = 0
for questionNumber in range(1, numberOfQuestions + 1):
    # pick two random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = f'#{questionNumber}: {num1} x {num2} = '

    try:
        # right answers handled by allowRegexes and wrong by blockRegexes
        pyip.inputStr(
            prompt, 
            allowRegexes=['^%s$' % (num1 * num2)],
            blockRegexes=[('.*', 'Incorrect!')],
            timeout=8, limit=3
        )
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries')

    else:
        # this block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers += 1

    time.sleep(1)   # brief pause to let user see result 

print(f'Score {correctAnswers} / {numberOfQuestions}')
