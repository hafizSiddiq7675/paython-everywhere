def main():
    prod_nums = ['BRO-6642', 'BRL-8788', 'MNA-3443', 'MNL-4444', 'MNL-3451']
    search = input('Enter prodction number(xxx-xxxx): ')
    if search in prod_nums:
        print(search, ' is in the list')
    else:
        print(search, ' was not in the list')

main()