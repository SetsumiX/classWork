from random import randint
from d16m06.Arena.Dialogues.dialogues import dial
from d16m06.Arena.Hero.create import Hero

params = {
    "1": "power",
    "2": "health",
    "3": "agility",
    "4": "damage",
    "5": "defense",
}

def calc_damage(attack, deff):
    base_damage = attack['damage'] + (attack['agility'] // 2)
    hit_chance = 70 + (attack['agility'] - deff.get('agility', 0))
    hit_chance = max(30, min(95, hit_chance))
    if randint(1, 100) > hit_chance:
        return 0
    crit_chance = attack['power'] // 3
    is_crit = randint(1, 10) <= crit_chance
    damage = base_damage * 1.5 if is_crit else base_damage
    final_damage = max(1, damage - deff.get('defence', 0))
    return int(final_damage)

def fight(hero, bot):
    hero_data = hero.get_d()
    bot_data = bot.get_enemy()
    print("Начало боя")
    count_fight = 0
    print(f"{hero_data['spec']} {hero_data['health']} vs Враг ({bot_data['health']})")

    while True:
        count_fight += 1
        print(f"Стадия боя №{count_fight}")
        damage = calc_damage(hero_data, bot_data)

        if damage == 0:
            print("Вы: *Промах*")
        else:
            bot_data['health'] -= damage
            print(f"Нанесено {damage} урона, у врага осталось {bot_data['health']}")

        if bot_data['health'] <= 0:
            hero_data['score'] += 20 * 1.2 / hero_data['level']
            print(f"Враг повержен\n"
                  f"{hero_data['level']} уровень персонажа: Получен опыт ({hero_data['score']} / 100)")

            if Hero.check_lvlup(hero, hero_data['score']) == True:
                print(f"{dial[16]} Теперь у вас {hero_data['level']} уровень.")
                for _ in range(3):
                    grade = input(dial[17])
                    Hero.set_d(hero, params[grade], hero_data[params[grade]] + 2)
            break

        damage = calc_damage(bot_data, hero_data)
        if damage == 0:
            print("Враг: *Промах*")
        else:
            hero_data['health'] -= damage
            print(f"Враг нанёс вам {damage} урона, у вас осталось {hero_data['health']}")

        if hero_data['health'] <= 0:
            print(dial[13])
            break
        print(dial[14])

    restart = input(dial[15])
    if restart == "y":
        return True