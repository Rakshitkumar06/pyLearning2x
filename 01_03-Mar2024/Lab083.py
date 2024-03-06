a = int(input("Enter num 1 \n"))
b = int(input("Enter num2 \n"))

try:
    c = a / b  # ZeroDivisionError: division by zero
    print("Div is ", c)
except Exception as e:
    print(e)
    print("Zero Division, Please dont use B as zero!")

print("This is Important message that we need show to user!")


