def main():
    cups_needed = int(input('Enter number of cpus: '))
    cups_to_ounces(cups_needed)

def cups_to_ounces(cups):
    ounces = 8 * cups
    print('That converts to', ounces, 'ounces.')

main()
