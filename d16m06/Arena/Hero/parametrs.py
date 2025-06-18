from time import sleep
from start.d16m06.Arena.Hero.create import Creature
from start.d16m06.Arena.tools.cteate_params import GetPar
from start.d16m06.Arena.game.index import game

def choice_param(hero):
    spec = ["Archer", "Swordman", "Assasin"]
    print("===============================")
    print(f"{hero.get_name()}, а ну посмотрим, какие у тебя боевые параметры")
    print("===============================")
    sleep(.6)
    d = {
        "power": GetPar.choice(),
        "health": GetPar.choice(),
        "agility": GetPar.choice(),
        "damage": GetPar.param(),
        "defense": GetPar.param(),
        "level": 1,
        "score": 0,
        "spec": "",
    }
    print("===============================")
    print(f"Ох, а ты хорош, почти... А сейчас выбери класс")
    print("===============================")

    for k, v in enumerate(spec):
        print(f"{k+1} - {v}")

    while True:

        c = input(f"Что выбераешь?\n"
                  f"Ответ: ")
        match c:
            case "1":
                d["spec"] = "Лучник"
                d["health"] = d["health"] - 1
                d["agility"] = d["agility"] + 1
                break
            case "2":
                d["spec"] = "Мечник"
                d["health"] = d["healths"] + 1
                d["agility"] = 2
                d["defense"] = d["defense"] + 2
                break
            case "3":
                d["spec"] = "Ассасин"
                d["agility"] = d["agility"] + 3
                d["damage"] = d["damage"] + 2
                d["defense"] = 1
                break
            case _:
                print("Не не, небылицы не рассказываей, что выберешь то?")

    print(f"Ух, ну и класс же ты взял, чтож, выглядишь ты на такие параметры:\n")
    for k, v in d.items():
        print(f"{k} - {v}")

    you_sure = input(f"Так, а ты уверен что твои параметры тебе подходят, или класс может не такой?\n"
                     f"Ответ y/n(any): ").lower()

    if you_sure == "y":
        for k, v in d.items():
            hero.set_d(k, v)
        game(hero)

    else:
        choice_param(hero)