from random import choice, randint


first_name = ("Жран", "Жмых", "Бром", "Дин", "Ван", "Грим")
last_name = ("Дикий", "Ужасный", "Яросный", "Угрюмый", "Вонючий", "Свирепый", "Старый")




def make_hero(
name=None,
hp_curret=None,
lvl=0,
xp_next=None,
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
        hp_curret = 20
    hp_max = hp_curret
    if not money:
        money = randint(1, 5)
    if not ATK_weapon:
        ATK_curret = ATK_base
    if not defense_shield and not defense_armor:
        defense_curret = defense_base
    if not inventory:
        inventory = []
    if not xp_next:
        xp_next = 234 + 234 * (lvl * 2)

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
def show_hero(hero):
    name = hero[0]
    hp_max = hero[1]
    hp_curret = hero[2]
    lvl = hero[3]
    xp_next = hero[4]
    xp_curret = hero[5]
    ATK_base = hero[6]
    ATK_weapon = hero[7]
    ATK_curret = hero[8]
    weapon = hero[9]
    defense_base = hero[10]
    defense_shield = hero[11]
    defense_armor = hero[12]
    defense_curret = hero[13]
    shield = hero[14]
    armor = hero[15]
    luck = hero[16]
    inventory = hero[17]
    money = hero[18]

    print("Персонаж:\n")
    print(f"Имя: {name}")
    print(f"HP: {hp_curret}/{hp_max}")
    print(f"Уровень: {lvl}")
    print(f"XP: {xp_curret}/{xp_next}")
    print(f"ATK: {ATK_curret}")
    print(f"Оружие: {weapon}")
    print(f"Защита: {defense_curret}")
    print(f"Щит: {shield}")
    print(f"Броня: {armor}")
    print(f"Удача: {luck}")
    print(f"Монеты: {money}\n")

def levelup(hero: list) -> None:
    if hero[5] >= hero[4]:
        hero[3] += 1
        hero[4] = 234 + 234 * (hero[3])
        print(f"Поздравляем! Вы достигли {hero[3]} уровня.\n")
        print("Распределите характеристики:\n")
        print("Увеличить HP : 1")
        print("Увеличить ATK: 2")
        print("Увеличить Защиту: 3\n")
        plus = input("Введите номер выбора и нажмите ENTER: ")
        if plus == "1":
            hero[1] += 5
            hero[2] += 5
        elif plus == "2":
            hero[6] += 1
        elif plus == "3":
            hero[10] += 1
        if not hero[7]:
            hero[8] = hero[6]


hero = make_hero()
hero[5] += 234
levelup(hero)
hero2 = make_hero()
show_hero(hero)
show_hero(hero2)
