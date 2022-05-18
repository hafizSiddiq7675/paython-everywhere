def find_average_marks(marks):
    sum_of_grades = sum(marks)
    num_of_subjects = len(marks)
    average_marks = sum_of_grades / num_of_subjects
    return average_marks

def compute_grades(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade


marks = [55,64,75,80,65]

average_marks = find_average_marks(marks)
print('Average of marks is', average_marks)

my_grade = compute_grades(average_marks)
print('And grade is', my_grade)
