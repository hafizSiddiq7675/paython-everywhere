b = 2
c = 23
print(b)
print(id(b))
def main():
    x = globals()['b']
    print(x)
    print(id(x))
main()