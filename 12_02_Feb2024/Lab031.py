# Match case
# Switch
numbers = int(input("Enter your number 1-6\n"))
match numbers:  #BREAK IS NOT NEEDED in case of Match and CASE
    case 1:
        print("you have entered 1")
    case 2:
        print("you have entered 2")
    case 3:
        print("you have entered 3")
    case 4:
        print("you have entered 4")
    case 5:
        print("you have entered 5")
    case 6:
        print("you have entered 6")
    case _:
        print("No idea")