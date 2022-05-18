class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.cpu = 'i5'
            self.brand = 'Dell'
            self.ram = 6

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = student("Ali", 1)
s2 = student("Asad", 3)

s1.show()


