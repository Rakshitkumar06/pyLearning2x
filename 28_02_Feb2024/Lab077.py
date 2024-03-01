class Father:
    def father_money(self):
        return "5"
    def home(self):
        return "This is your Father home"

class Mother:
    def mother_money(self):
        return "2"
    def home(self):
        return "This is your Mother home"

class Son(Father,Mother):
    pass

class Son(Mother,Father):
    def home(self):
        return "This is your home"

S = Son()
# print(S.father_money())
# print(S.mother_money())
print(S.home())
# MRO - Method Resolution Order