# def main():
#     num_emps = int(input("How many empolyes records"
#     + "do you want to create? : "))
#     emp_file = open("emp_data.txt", 'w')
#     for count in range(1, num_emps + 1):
#         print("Enter data for employe #", count, sep= '')
#         name = input("Name: ")
#         id_num = input("Id number: ")
#         dept = input("Department: ")
#         emp_file.write(name + '\n')
#         emp_file.write(id_num + '\n')
#         emp_file.write(dept + '\n')
#         print()
#     emp_file.close()
#     print('All data is saved to employee file')
# main()


# def main():
#     count = 0
#     my_string = input("Enter a string: ")
#     for ch in my_string:
#         if ch == 't' or ch == 'T':
#             count += 1

#     print("The letter 'T' appears ", count, 'times')
# main()


# my_name = 'Jack'
# for ch in my_name:
#     print(ch)

# my_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(my_string[0:26:2])

# my_list = ["Jack", "Emma", "Chloe", "Bruce", "Wayn"]
# if "Shelby" not in my_list:
#     print('The string "Shelby" was not found.')
# else:
#     print('The string "Shelby" was found.')


# string1 = 'ABCDEF'
# print(string1.lower())

# file_name = input('Enter a file name: ')
# if file_name.endswith('.txt'):
#     print('That is the name of a text file.')
# elif file_name.endswith('.py'):
#     print('That is the name of a python file.')
# elif filename.endswith('.doc'):
#     print('That is the name of a word processing document.')
# else:
#     print('Unknown file type.')

# string = "Linda is eighteen years old"
# new_string = string.replace("eighteen", "ninteen")
# print(new_string)

# phonebook = {
#     'Katie':'123-987654',
#     'Tom':'555-235327',
#     'Emma':'333-323232',
#     'Adam':'435-535348'
# }
# print(phonebook['Tom'])
# print(phonebook['Emma'])

# phonebook = {
#     'Chris':'555-1111', 
#     'Katie':'555-2222',
#     'Joanne':'555-3333'
# }
# if 'Emma' in phonebook:
#     print(phonebook['Emma'])
# else:
#     print('Emma is not in the list')

# phonebook = {
#     'Katie':'123-987654',
#     'Tom':'555-235327',
#     'Emma':'333-323232',
#     'Adam':'435-535348'
# }
# phonebook['Joe'] = '333-242443'
# phonebook['Chloe'] = '555-546457'
# print(phonebook)


phonebook = {
    'Chris':'555-1111',
    'Katie':'555-2222',
    'Joanne':'555-3333'
}
if 'Emma' in phonebook:
    del phonebook['chris']
print(phonebook)
