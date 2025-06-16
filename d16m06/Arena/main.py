from start.d16m06.Arena.Creatures.create import Creature
from start.d16m06.Arena.Creatures.parametrs import choice_param

if __name__ == "__main__":
    inp = input("Приветствую путник, не проходи мимо, и назовись\n"
                "Ответ: ")
    hero = Creature(inp) if inp else Creature("Молчаливый")
    print(f"Ещё раз здравствуй {Creature.get_name(hero)}")
    q = input(f"Слушай {Creature.get_name(hero)}, ...а не хочешь ли заработать?\n"
              f"Ответ y/n(any): ").lower()

    match q:
        case "y":
            print("Окак, тогда...")
            choice_param(hero)

        case _:
            print("Ладненько, тогда, если нужны будут деньги, ты знаеш где меня искать")
