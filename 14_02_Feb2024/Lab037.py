# def print_arguments(a,b,c,d,e):
#     return a + b + c + d + e
#
# result = print_arguments(10,10,20,40,50)
# print(result)

def print_arguments(*args):
    for i in args:
        print(i, end = " ")


print_arguments(12,12,2,4)
print_arguments(10,20,30,40,50,60)