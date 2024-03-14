class Color:
    def __init__(self, red, blue, green):
        self.__red = red
        self.__blue = blue
        self.__green = green

    def get_red(self):
        return self.__red

    def get_blue(self):
        return self.__blue

    def get_green(self):
        return self.__green

    def set_red(self, new_red):
        if 0 <= new_red <= 255:
            self.__red = new_red
        else:
            print('Unijeli ste pogresnu vrijednost!')

    def set_blue(self, new_blue):
        if 0 <= new_blue <= 255:
            self.__blue = new_blue
        else:
            print('Unijeli ste pogresnu vrijednost!')

    def set_green(self, new_green):
        if 0 <= new_green <= 255:
            self.__green = new_green
        else:
            print('Unijeli ste pogresnu vrijednost!')

    def add_red(self, change):
        if self.__red + change > 255 or self.__red + change < 0:
            print('Previse ste unijeli.')
        else:
            self.__red += change

    def add_blue(self, change):
        if self.__blue + change > 255 or self.__blue + change < 0:
            print('Previse ste unijeli.')
        else:
            self.__blue += change

    def add_green(self, change):
        if self.__green + change > 255 or self.__green + change < 0:
            print('Previse ste unijeli.')
        else:
            self.__green += change

    def __str__(self):
        print(f'"red":{self.__red},"green":{self.__green}, "blue":{self.__blue} ')

    def __eq__(self, other):
        if self.__red == other.get_red():
            if self.__blue == other.get_blue():
                if self.__green == other.get_green():
                    return True
        return False

    def __it__(self, other):
        if self.__red < other.get_red() and self.__blue < other.get_blue() and self.__green < other.get_green():
            return True
        return False


colour1 = Color(124, 34, 200)
colour2 = Color(122, 34, 200)

print(colour1.__eq__(colour2))
colour1.add_blue(255)
