str = input("Enter your string: ")
result = (str[::-1])
# For negative indexing, to display the 1st element to last element in
# steps of 1 in reverse order, we use the [::-1]

if str == result:
    print("Given string is a palindrome")
else:
    print("Not an palindrome")


# num = 121
# result = int(str(num)[:: -1])
#
# if num == result:
#     print("Number is palindrome")
# else:
#     print("Not an palindrome")



