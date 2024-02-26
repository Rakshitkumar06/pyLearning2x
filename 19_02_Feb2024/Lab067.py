class person():
    name = None
    age =  None

    def work(self):
        print("I can work")

    def sleep(self):
        print("I can sleep")


P1 = person()
P1.name = "Deepak"
print(P1.name)
P1.age = 45
print(P1.age)
P1.work()
P1.sleep()
