from random import randint

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
    print(f"{hero_data['spec']} {hero_data['health']} vs Враг ({bot_data['health']})")

    while True:
        damage = calc_damage(hero_data, bot_data)
        if damage == 0:
            print("Вы: *Промах*")
        else:
            bot_data['health'] -= damage
            print(f"Нанесено {damage} урона, у врага осталось {bot_data['health']}")

        if bot_data['health'] <= 0:
            hero_data['score'] += 20 * 1.2 / hero_data['level']
            print(f"Враг повержен\n"
                  f"{hero_data['level']} уровень персонажа: Получен опыт ({hero_data['score']})")
            break

        damage = calc_damage(bot_data, hero_data)
        if damage == 0:
            print("Враг: *Промах*")
        else:
            hero_data['health'] -= damage
            print(f"Враг нанёс вам {damage} урона, у вас осталось {hero_data['health']}")

        if hero_data['health'] <= 0:
            print("Вы не смогли заработать, увы...")
            break
        print("Бой продолжается")

    restart = input(f"Хотите играть заного?\n"
                    f"Ответ y/n(any): ")
    if restart == "y":
        return True