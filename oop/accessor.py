class Students:
    def __init__(self, name, grade, marks):
        self.name = name
        self.grade = grade
        self.marks = 1048

student1 = Students("Ali", "12", "1048")

student1.marks = "900"
print(student1.marks)
