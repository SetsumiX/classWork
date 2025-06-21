from time import sleep
from d16m06.Arena.Hero.create import Hero
from d16m06.Arena.tools.cteate_params import GetPar
from d16m06.Arena.game.index import game
from d16m06.Arena.Dialogues.dialogues import dial

def choice_param(hero):
    spec = ["Archer", "Swordman", "Assasin"]
    print("===============================")
    print(f"{hero.get_name()}, {dial[9]}")
    print("===============================")
    sleep(.6)
    d = {
        "power": GetPar.choice(),
        "health": GetPar.choice_hp(),
        "agility": GetPar.choice(),
        "damage": GetPar.param(),
        "defense": GetPar.param(),
        "level": 1,
        "score": 0,
        "spec": "",
    }
    print(dial[4])

    for k, v in enumerate(spec):
        print(f"{k+1} - {v}")

    while True:

        c = input(dial[5])
        match c:
            case "1":
                d["spec"] = "Лучник"
                d["health"] = d["health"] - 10
                d["agility"] = d["agility"] + 1
                break
            case "2":
                d["spec"] = "Мечник"
                d["health"] = d["healths"] + 10
                d["agility"] = 2
                d["defense"] = d["defense"] + 2
                break
            case "3":
                d["spec"] = "Ассасин"
                d["health"] = d["health"] - 15
                d["agility"] = d["agility"] + 3
                d["damage"] = d["damage"] + 2
                d["defense"] = 1
                break
            case _:
                print(dial[6])

    print(dial[7])
    for k, v in d.items():
        print(f"{k} - {v}")

    you_sure = input(dial[8]).lower()

    if you_sure == "y":
        for k, v in d.items():
            hero.set_d(k, v)
        game(hero)

    else:
        choice_param(hero)