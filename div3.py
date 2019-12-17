# Print out all of the numbers in the following array that are divisible by 3:
# [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# You may use whatever programming language you wish.



# def divide3(arr):
#     divthrees = []

#     for num in arr:
#         if num % 3 == 0:
#             divthrees.append(num)
    
#     return divthrees

arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

# print(divide3(arr))

# divthrees = [num for num in arr if num % 3 == 0]
divthrees = filter(lambda x: x % 3 ==0, arr)
print(list(divthrees))

