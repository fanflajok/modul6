class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            Animal.fed = True
        else:
            print(f"{self.name} не съел {food.name}")
            Animal.alive = False

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name



class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    edible = False

class Fruit(Plant):
    edible = True


a1 = Predator('Тигр')
a2 = Mammal('Жираф')
p1 = Flower('цветик семицветик')
p2 = Fruit('заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
