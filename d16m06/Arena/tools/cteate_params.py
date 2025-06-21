from random import randint

class GetPar:
    @staticmethod
    def choice_hp():
        return randint(25, 50)

    @staticmethod
    def choice():
        return randint(4, 9)

    @staticmethod
    def param():
        return randint(1, 5)