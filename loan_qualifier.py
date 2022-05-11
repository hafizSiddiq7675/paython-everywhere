min_salary = 30000
min_years = 2

user_year = int(input("Enter year/years of service: "))
user_salary = int(input("Enter your salary: "))

if user_year >= min_years and user_salary >= min_salary:
    print("You are qualified for loan.")
else:
    print("You are not qualified for loan.")
