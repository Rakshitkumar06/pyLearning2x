class person():
    name = None
    age = None
    id = None
    ph_no = None

    def talk(self):
        print("I can talk")

    def work(self):
        print("I can work")


def anotherfunction():
            print("I am function")

p1 = person()
p1.name = "MSD"
print(p1.name)
p1.talk()

