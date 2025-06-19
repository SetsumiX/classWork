from d16m06.Arena.Enemys.card import show_enemies
from d16m06.Arena.Enemys.data import data
from d16m06.Arena.tools.show_card import show
from d16m06.Arena.game.figth import fight
from d16m06.Arena.Dialogues.dialogues import dial

def game(hero):
    print(dial[11])
    show_enemies()
    print("===============================")
    bot = data.get("b_" + input(dial[12]))
    show(hero, bot)
    restart = fight(hero, bot)
    if restart: game(hero)