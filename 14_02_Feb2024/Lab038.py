def make_pizza(*topings):
    print(topings)
    for toping in topings:
        print(toping)


person1 = make_pizza("mushroom","Sweetcron", "pineapple")
person2 = make_pizza("Apple","Onion","Cron","panner")
person3 = make_pizza("mushroom","pineapple","Onion","cheese")


def make_pizza_base(*topings,base):
    print(topings,base)
    for toping in topings:
        print(topings,base)
 

person1 = make_pizza_base("mushroom,cheese,""onion",base= "thin")
