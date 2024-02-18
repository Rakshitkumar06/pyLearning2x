def make_pizza_base(*topings, base):
    print(topings, base)
    for toping in topings:
        print(topings)
    return topings,base


person1_t,person1_b = make_pizza_base("mushroom,cheese,""onion", base="thin")
print(person1_t)
print(person1_b)