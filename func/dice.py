import random

MIN = 1
MAX = 6
def main():
    again = 'y'
    while again == 'y' or again == 'Y':
        print('The dice is rolling ... ... ...')
        print('Their values are: ')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        again = input('Roll dice again?(y = yes):')

main()
# number = random.randrange(10)
# print(number)