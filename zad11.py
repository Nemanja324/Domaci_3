from zad10 import Color


class AlphaColor(Color):
    def __init__(self, red, blue, green, alpha):
        super().__init__(red, blue, green)
        self.__alpha = alpha

    def get_alpha(self):
        return self.__alpha

    def set_alpha(self, new_alpha):
        if new_alpha > 1 or new_alpha < 0:
            print('Alpha mora biti u granicama od 0 do 1.')
        else:
            self.__alpha = new_alpha

    def __str__(self):
        print(f'red: {self.get_red()}, green: {self.get_green()} ,blue: {self.get_blue()}')

    def update_color_by_alpha(self, alpha):
        if 0 <= self.get_red() * alpha <= 225:
            if 0 <= self.get_blue() * alpha <= 225:
                if 0 <= self.get_green() * alpha <= 225:
                    self.set_red(self.get_red() - self.get_red() * alpha)
                    self.set_blue(self.get_blue() - self.get_blue() * alpha)
                    self.set_green(self.get_green() - self.get_green() * alpha)


obj1 = AlphaColor(220, 30, 40, 0.3)
print(obj1.__str__())
obj1.update_color_by_alpha(0.3)
print(obj1.__str__())
