from start.d16m06.Arena.Enemys.card import show_enemies
from start.d16m06.Arena.Enemys.data import data
from start.d16m06.Arena.tools.show_card import show
from start.d16m06.Arena.game.figth import fight

def game(hero):
    print("===============================")
    print(f"И так, если хочешь знать заранее, вот с кем ты будешь сражаться\n"
          f"На выбор конечно, так вот, есть 1, 2, 3-ий")
    print("===============================")
    show_enemies()
    print("===============================")
    bot = data.get("b_" + input(f"Выбери одного из трёх:\n"
                                f"Ответ: "))
    show(hero, bot)
    fight(hero, bot)
    restart = fight(hero, bot)
    if restart: game(hero)