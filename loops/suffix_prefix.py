"""

Suffex is used to remove the end of a string
While prefix is used to remove the start of a string

"""

# my_text = 'Hi ThereRemovethis'
# print(my_text.removesuffix('Removethis'))
# print(my_text.removeprefix('Hi'))


file_names = ['index.html', 'nav.html', 'form.html', 'sign_up.html']
base_file_names = [name.removesuffix('.html') for name in file_names]
print(base_file_names)