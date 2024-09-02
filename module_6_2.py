class Vehicle:
    __COLOR_VARIANTS = ["красный", "оранжевый", "жёлтый", "зелёный", "голубой", "синий", "фиолетовый"]
    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)
    def get_model(self):
        print(f"Модель: {self.__model}")
    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power} лошадиных сил")
    def get_color(self):
        print(f"Цвет: {self.__color}")
    def print_info(self):
        self.get_model(), self.get_horsepower(), self.get_color(), print(f"Владелец: {self.owner}")
    def set_color(self, new_color):
        lower_list = [x.lower() for x in self.__COLOR_VARIANTS]
        if new_color.lower() in lower_list:
            self.__color = new_color.lower()
        else:
            print(f"Нельзя сменить цвет на {new_color}")



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
p1 = Sedan("Виктор", "Skoda Octavia", 110, "чёрный")
p2 = Sedan("Юлия", "Porsche Macan", 350, "белый")
p1.print_info()
print(" ")
p1.set_color("бурый")
p1.set_color("фиОлеТовыЙ")
p1.owner = "Anna"
print("")
p1.print_info()

