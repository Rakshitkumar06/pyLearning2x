# Single - 80%
# Multiple
# Multi level
# Hybrid
# Heri

# API, Web Automation - 80% -> Single

# Multilevel Inheritance
class Grandparent:

    def grandparent_method(self):
        return "Grandparent_method"

class Parent(Grandparent):
    def parent_method(self):
        return "parent_method"

class Child(Parent):
    def child_mehthod(self):
        return "child_method"

Ch = Child()
print(Ch.grandparent_method())
print(Ch.parent_method())
print(Ch.child_mehthod())

print("--------------")

P = Parent()
print(P.grandparent_method())
print(P.parent_method())

print("--------------")

G = Grandparent()
print(G.grandparent_method())
print(G.__class__)