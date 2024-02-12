year = int(input("Enter your year"))
if ((year % 4 == 0 ) and  (year % 400 != 0)):
   print("\nIts a leap year", year )
else:
    print("Not a leap year", year)