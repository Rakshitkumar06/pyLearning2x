# Method Overriding - Same name in the parent and child
# child always override the parent functions
# super means call my parent function

class Animal:

    def __init__(self):
        pass
    def sound(self):
        print("Animal Sound")

class Dog:
    def __init__(self):
        pass
    def sound(self):
        print("Dog sound")

A = Animal()
A.sound()

D = Dog()
D.sound()