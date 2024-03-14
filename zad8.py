class Player:
    def __init__(self, x, y, width, height, health):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__health = health

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        if new_health > 100 or new_health < 0:
            print('Pogresan unos zivota.')
        else:
            self.__health = new_health

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def set_height(self, new_height):
        self.__height = new_height

    def set_width(self, new_width):
        self.__width = new_width

    def decrate_health(self, other):
        if check_collision(self, other):
            new_health = self.get_health - other.get_damage
            self.set_health(new_health)


class Enemy:

    def __init__(self, x, y, width, height, damage):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__damage = damage

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_damage(self):
        return self.__damage

    def set_damage(self, new_damage):
        if new_damage > 100 or new_damage < 0:
            print('Pogresan unos zivota.')
        else:
            self.__damage = new_damage

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def set_height(self, new_height):
        self.__height = new_height

    def set_width(self, new_width):
        self.__width = new_width


def check_collision(player, enemy):
    if player.get_x == enemy.get_x and player.get_y == enemy.get_y:
        return True
    return False


obj1 = Player(3, 4, 3, 10, 100)
obj2 = Enemy(5, 1, 9, 10, 40)

print(obj1.get_x())
