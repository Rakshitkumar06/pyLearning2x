# Find the max between 3 numbers

num1 = int(input("Enter the num1"))
num2 = int(input("Enter the num2"))
num3 = int(input("Enter the num3"))

max_num = max(num1, num2, num3)
print(max_num)

print("--------------")
# without using max using if condition
if num1 > num2 and num1 > num3:
    print("Max is ", num1)
elif num2 > num1 and num2 > num3:
    print("Max is ", num2)
else:
    print("Max is ", num3)
