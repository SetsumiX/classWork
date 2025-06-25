from d16m06.Arena.Hero.create import Hero
from d16m06.Arena.Hero.parametrs import choice_param
from d16m06.Arena.Dialogues.dialogues import dial

if __name__ == "__main__":
    inp = input(dial[1])
    hero = Hero(inp) if inp else Hero("Молчаливый")
    q = input(f"Слушай {Hero.get_name(hero)}, {dial[10]}").lower()

    match q:
        case "y":
            print(dial[2])
            choice_param(hero)

        case _:
            print(dial[3])
