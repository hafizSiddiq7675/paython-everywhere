def string_reverse(str1):
    new_str = ''
    index = len(str1)
    while index > 0:
        new_str += str1[index -1]
        index = index - 1
    return new_str
print(string_reverse('1234abcd'))

