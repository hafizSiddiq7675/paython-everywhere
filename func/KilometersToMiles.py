
def main():
    kilometers = int(input('Enter number of kilometers: '))
    kilometers_in_miles(kilometers)

def kilometers_in_miles(distance_in_kilometers):
    miles = distance_in_kilometers * 0.621371
    print('Number of kilometers entered are', format(miles, '.2f', ), 'miles')

main()