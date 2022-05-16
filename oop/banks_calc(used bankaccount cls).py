import bankaccount
def main():
    # Get starting balance.
    start_bal = float(input("Enter your starting balance: "))
    # Create bankacoount object.
    savings = bankaccount.BankAccount(start_bal)
    # Deposit user's pay check
    pay = float(input("How much you were paid last week? :"))
    print('I will deposit $', pay, ' into your account.')
    savings.deposit(pay)
    # Display the balance
    print('Your account balance is $', format(savings.get_balance(), ',.2f'),sep='')
    # Get amount to withdraw.
    cash = float(input('How much you would like to withdraw? :'))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)
    # display the balance
    print('Your account balance is $', format(savings.get_balance(), ',.2f'),sep='')
# call the main function
main()
