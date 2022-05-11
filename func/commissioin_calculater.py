# create main fnuction
#   then sales function
#   then advanced_pay function
#   then comm_rate function


def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = get_comm_rate(sales)

    pay = sales * comm_rate - advanced_pay
    print('The pay is $', format(pay, ',.2f'),sep='')

    if pay < 0:
        print('The salesperson must reimburse')
        print('the company.')


def get_sales():
    monthly_sales = float(input('Enter the monthlly sales: '))
    return monthly_sales


def get_advanced_pay():
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advanced pay was given.')
    advanced = float(input('Advanced pay: '))
    return advanced

def get_comm_rate(sales):
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <=17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    return rate

main()