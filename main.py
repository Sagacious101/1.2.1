from random import choice, randint


first_name = ("Жран", "Жмых", "Бром", "Дин", "Ван", "Грим")
last_name = ("Дикий", "Ужасный", "Яросный", "Угрюмый", "Вонючий", "Свирепый", "Старый")




def make_hero(
name=None,
hp_curret=None,
lvl=0,
xp_next=100,
xp_curret=0,
ATK_base=1,
ATK_weapon=None,
weapon=None,
defense_base=0,
defense_shield=0,
defense_armor=0,
shield=None,
armor=None,
luck=1,
inventory=None,
money=None
) -> list:

    """
    Герой - это список
    [0] name - имя персонажа
    [1] hp_max - максимальное здоровье
    [2] hp_curret - текущее здоровье, контролирует игру
    [3] lvl - текущий уровень игрока (изначально 1)
    [4] xp_next - кол-во опыта для след. lvl
    [5] xp_curret - опыт сейчас
    [6] ATK_base - сила атаки без оружия
    [7] ATK_now - сила атаки с оружием
    [9] weapon - оружие
    [10] defense_base - защита без снаряжения
    [11] defense_now - защита с снаряжением
    [12] shield - щит
    [13] armor - доспехи
    [14] luck - удача
    [15] inventory - инвентарь
    [16] money - монеты
    """
    if not name:
        name = choice(first_name) + " " + choice(last_name)
    if not hp_curret:
        hp_curret = 20 + (1 * lvl)
    hp_max = hp_curret
    if not money:
        money = randint(1, 5)
    if not ATK_weapon:
        ATK_curret = ATK_base
    if not defense_shield and not defense_armor:
        defense_curret = defense_base

    return [
        name,
        hp_max,
        hp_curret,
        lvl,
        xp_next,
        xp_curret,
        ATK_base,
        ATK_weapon,
        ATK_curret,
        weapon,
        defense_base,
        defense_shield,
        defense_armor,
        defense_curret,
        shield,
        armor,
        luck,
        inventory,
        money
    ]

p1 = make_hero()
p2 = make_hero()
p3 = make_hero()
p4 = make_hero()
p5 = make_hero()
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
