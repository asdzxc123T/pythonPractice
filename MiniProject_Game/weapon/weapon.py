class Weapon:
    def __init__(self, no, name, type, phyDmg, magDmg, strRes, dexRes, intRes, price):
        self.no = int(no)
        self.name = name
        self.type = int(type)
        self.phyDmg = int(phyDmg)
        self.magDmg = int(magDmg)
        self.strRes = int(strRes)
        self.dexRes = int(dexRes)
        self.intRes = int(intRes)
        self.price = int(price)