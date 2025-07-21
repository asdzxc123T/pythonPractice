class GameCharacter:
    def __init__(self, no, name, lv, exp, hp, mp, baseAttack, baseDefense, str, dex, inte, type, gold, w_no, ar_no):
        self.no = int(no)
        self.name = name
        self.lv = int(lv)
        self.exp = int(exp)
        self.hp = int(hp)
        self.currentHp = int(hp)
        self.mp = int(mp)
        self.currentMp = int(mp)
        self.baseAttack = int(baseAttack)
        self.baseDefense = int(baseDefense)
        self.str = int(str)
        self.dex = int(dex)
        self.int = int(inte)
        self.type = int(type)
        self.gold = int(gold)
        self.w_no = int(w_no)
        self.ar_no = int(ar_no)