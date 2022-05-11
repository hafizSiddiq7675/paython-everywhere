a = 5
b = 0

try:
    print('Resource Open')
    print(a/b)

except ZeroDivisionError as e:
    print('You cannot divide a Number by Zero', e)
except Exception as e:
    print('Something went Wrong...')
finally:
    print('Resource Closed')
