travelling = input('yes or no: ')
while travelling == 'yes':
    num = int(input('Enter number of people travelling: '))
    for num in range(1, num +1):
        name = input('Name: ')
        age = input('Age: ')
        sex = input('Male or Female? ')
        print(num)
        print(age)
        print(sex)
    travelling = input('Forgot someone?')


