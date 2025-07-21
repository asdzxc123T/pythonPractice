class Monster:
    def __init__(self, no, name, type, hp, mp, baseAttack, baseDefense, reqDex, exp, gold, floor):
        self.no = int(no)
        self.name = name
        self.type = int(type)
        self.hp = int(hp)
        self.currentHp = int(hp)
        self.mp = int(mp)
        self.baseAttack = int(baseAttack)
        self.baseDefense = int(baseDefense)
        self.reqDex = int(reqDex)
        self.exp = int(exp)
        self.gold = int(gold)
        self.floor = int(floor)