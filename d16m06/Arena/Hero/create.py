class Hero:

    def __init__(self, name):
        self.__name = name
        self.dt = {}

    def get_name(self):
        return self.__name

    def set_d(self, key, value):
        self.dt[key] = value

    def get_d(self):
        return self.dt

    def check_lvlup(self, xp):
        if xp >= 100:
            self.dt['level'] += 1
            self.dt['score'] -= 100
        return xp >= 100