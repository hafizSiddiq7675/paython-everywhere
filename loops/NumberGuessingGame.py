# count = 0
# while count < 9:
#     print('Number:', count)
#     count = count + 1
# print('Goodbye')


import random
n = 20
Number_to_be_guessed = int(n * random.random() + 1)
guess = 0
while guess != Number_to_be_guessed:
    guess = int(input('Enter number: '))
    if guess > 0:
        if guess < Number_to_be_guessed:
            print('Number is too small')
        elif guess > Number_to_be_guessed:
            print('Number is too big')
    else:
        print('You are giving up')
        break
else:
    print('Congratulations you have made it')
