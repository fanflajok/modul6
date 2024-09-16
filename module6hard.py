import math
class Figure:
    sides_count = 0
    def __init__(self, r, g, b, *__sides, filled = False):
        self.filled = filled
        self.__sides = []
        if self.__is_valid_sides(*__sides):
            self.__sides = list(__sides)
        self.__color = []
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def get_color(self):
        list_of_colors = self.__color
        return list_of_colors
    def __is_valid_color(self, r, g, b):
        if 0 <= int(r) <= 255 and 0 <= int(g) <= 255 and 0 <= int(b) <= 255:
            return True
        else:
            return False
    def get_sides(self):
        list_of_sides = self.__sides
        return list_of_sides
    def __is_valid_sides(self, *sides):
        for i in sides:
            if not isinstance(i, int) or i <= 0 or len(sides) != self.sides_count:
                return False
        return True
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, r, g, b, length, filled = False):
        super().__init__(r, g, b, length, filled = filled)
        if isinstance(length, tuple):
            self.set_sides(1)
        self.__radius = self.get_sides()[0] / (2 * math.pi)
    def set_sides(self, *length):
        super().set_sides(*length)
        self.__radius = self.get_sides()[0]/(2*math.pi)
    def get_square(self):
        s = math.pi * self.__radius ** 2
        return s


class Triangle(Figure):
    sides_count = 3
    def __init__(self, r, g, b, *sides, filled=False):
        super().__init__(r, g, b, *sides, filled=filled)
        if len(sides) == self.sides_count:
            self.set_sides(sides)
        else:
            self.set_sides(1, 1, 1)
    def get_square(self):
        pp = (sum(self.get_sides()))*0.5
        st = math.sqrt(pp*(pp-self.get_sides()[0])*(pp-self.get_sides()[1])*(pp-self.get_sides()[2]))
        return st
    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.sides = sides


class Cube(Figure):
    sides_count = 12  # Куб имеет 12 ребер

    def __init__(self, r, g, b, one_side, filled=False):
        cube_sides = [one_side] * self.sides_count
        if isinstance(one_side, tuple):
            default_sides = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
            super().__init__(r, g, b, *default_sides, filled=filled)
            self.set_sides(*default_sides)
        else:
            super().__init__(r, g, b, *cube_sides, filled=filled)
            self.set_sides(*cube_sides)
    def get_volume(self):
        V = self.get_sides()[0] ** 3
        return V



circle1 = Circle(200, 200, 100,(6,9))
triangle1 = Triangle(3,4,5, 7,9,7,7)
cube1 = Cube(3,4,5,(7,9))
print(circle1.get_sides())
print(triangle1.get_sides())
print(cube1.get_volume())
cube1.set_sides(66,86,6)
print(cube1.get_volume())
cube1.set_sides(6,6,6,6,6,6,6,6,6,6,6,6)
print(cube1.get_volume())
triangle1.set_sides(10,10,10)
print(triangle1.get_sides())
print(circle1.get_sides())
print(circle1.get_square())
print(triangle1.get_square())