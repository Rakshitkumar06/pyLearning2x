# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif, else
#  Step 1: Figure out the input
#  Input ? int
scale = int(input("Enter the number you got!\n"))
print(type(scale))
#  Step 2: Logic
if scale <= 100 and scale >= 90:
    print("Grade A")
elif scale <= 89 and scale >= 80:
    print("Grade B")
elif scale <= 79 and scale >= 70:
    print("Grade C")
elif scale <= 69 and scale >= 60:
    print("Grade D")
elif scale <= 59 and scale >= 0:
    print("Grade F")
else:
    print("Invalid Input")
