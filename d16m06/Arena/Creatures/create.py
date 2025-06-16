class Creature:
    def __init__(self, name):
        self.__name = name
        self.dt = {}


    def get_name(self):
        return self.__name

    def set_d(self, key, value):
        self.dt[key] = value
        print(self.dt[key])

    def get_d(self):
        return self.dt