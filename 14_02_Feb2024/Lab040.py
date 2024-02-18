# Reverse string

# str = "Dhoni"
# rev_str = ""
# for c in str:
#
#     rev_str = c + rev_str
#
#
# print(rev_str)

def reversed_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


name = reversed_string("Dhoni")
print(name)


