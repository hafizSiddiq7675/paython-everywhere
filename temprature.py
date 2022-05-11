MAX_TEMP = 102.5

temp = float(input("Enter the substance's Celsius temperature: "))
while temp > MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait 5 minutes.')
    print('Then take the temperature again and enter it.')
    temp = float(input('Enter temperature again: '))
print('Temperature is acceptable')
print('Check temperature again in 15 minutes.')

