from start.d16m06.Arena.tools.create_card import create_card

def show(hero, bot):
    hero_card = create_card(hero.get_d(), "YOU")
    bot_card = create_card(bot.get_enemy(), "ENEMY")
    for line1, line2 in zip(hero_card, bot_card):
        print(line1 + "    " + line2)