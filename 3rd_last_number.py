# list1 = [12,42,35,23,43]
# list1.sort()
# print(list1[2])
# import random

# for count in range(5):
#     number = random.randrange(0, 101, 10)
#     print(number)


# def leastnumber(numbers):
#     smallest_num = numbers[0]
#     count = 0
#     for num in numbers:
#         if num < smallest_num:
#             smallest_num = num
#     return smallest_num

# print(leastnumber([10,20,30,40,50,60]))

# def leastnumber(numbers):
#     smallest_num = numbers[0]
#     sec_smallest = numbers[1]
#     for num in numbers:
#         if num < smallest_num:
#             smallest_num = num
#     return smallest_num
#     for num in numbers:
#         if num < sec_smallest:
#             num != smallest_num
#     return sec_smallest
    
# print(leastnumber([10,20,30,40,50,60]))


numbers = [23,43,1,12,43]
numbers.sort()
print(numbers[2])