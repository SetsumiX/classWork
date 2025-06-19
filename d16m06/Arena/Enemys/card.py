from d16m06.Arena.Enemys.data import data
from d16m06.Arena.tools.create_card import create_card

arr = []

for k, v in data.items():
    arr.append(create_card(v.get_enemy(), k))

def show_enemies():
    for lines in zip(*arr):
        print("     ".join(lines))