def sum_of_num(a, b):
    return a + b


result = sum_of_num(4 , 4)
print(result)

result = sum_of_num(2.0 , 2.0)
print(result)

result = sum_of_num("MS"  , " Dhoni" )
print(result)

# TypeError: can only concatenate str (not "int") to str
# result = sum_of_num("Pramod", 123)
# print(result)