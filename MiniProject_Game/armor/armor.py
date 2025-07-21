class Armor:
    def __init__(self, no, name, phyDef, magDef, strRes, dexRes, intRes, price):
        self.no = int(no)
        self.name = name
        self.phyDef = int(phyDef)
        self.magDef = int(magDef)
        self.strRes = int(strRes)
        self.dexRes = int(dexRes)
        self.intRes = int(intRes)
        self.price = int(price)