#Print the table of 2 by using commandprint()
#first approach
print ("Value of 2 * 1 =", 2*1)   
print ("Value of 2 * 2 =", 2*2)
print ("Value of 2 * 3 =", 2*3)
print ("Value of 2 * 4 =", 2*4)
print ("Value of 2 * 5 =", 2*5)
print ("Value of 2 * 6 =", 2*6)
print ("Value of 2 * 7 =", 2*7)
print ("Value of 2 * 8 =", 2*8)
print ("Value of 2 * 9 =", 2*9)
print ("Value of 2 * 10 =", 2*10)

#second approach
# Multiplication table (from 1 to 10) in Python
num = 2
# To take input from the  user
# num = int(input("Display multiplication table of? "))
# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)