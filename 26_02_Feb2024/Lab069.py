class Person:
      def __init__(self,name):
          self.name = name

      def say_hi(self):
          print("My name is ",self.name)

p1 = Person("MSD")
p2 = Person("Harish")
p3 =Person("Mani")

p1.say_hi()
p2.say_hi()
p3.say_hi()