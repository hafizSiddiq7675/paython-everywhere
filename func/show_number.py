number = 0
def main():
    global number
    number = int(input('Enter a number: '))
    show_number()
def show_number():
    print('Number you entered is ', number)

main()