# 친구, 심판, 나
# 친구나 내가 끌고 가기에는 어색
# -> 심판을 추가
from random import randint

class Enemy:
    def fire(self):
        return randint(1, 3)

class User:
    def __init__(self):
        self.win = 0

    def fire(self):
        return int(input("뭐 : "))

class Referee:
    def __init__(self):
        self.ruleBook = [None, "가위", "바위", "보"]

    def start(self):
        blueCorner = self.callBlueCorner()
        redCorner = self.callRedCorner()
        self.tellRule()
        while True:
            bluePaper = self.enemyFire(blueCorner)
            redPaper = self.userFire(redCorner)
            self.tellHand(bluePaper, redPaper)
            if self.judge(bluePaper, redPaper, redCorner):
                break
        self.tellResult(redCorner)

    def callBlueCorner(self):
        return Enemy()

    def callRedCorner(self):
        return User()
    
    def tellRule(self):
        for i, v in enumerate(self.ruleBook):
            if i != 0:
                print("%d) %s" % (i, v))
        print("-----")

    def enemyFire(self, e):
        return e.fire()

    def userFire(self, u):
        redPaper = u.fire()
        if 0 < redPaper < 4:
            return redPaper
        return self.userFire(u)

    def tellHand(self, bluePaper, redPaper):
        print("유저 : %s" % self.ruleBook[redPaper])
        print("컴터 : %s" % self.ruleBook[bluePaper])

    def judge(self, bluePaper, redPaper, u):
        t = redPaper - bluePaper
        if t == 0:
            print("무")
        elif t == -1 or t == 2:
            print("패")
            return True
        else:
            print("승")
            u.win += 1
        return False

    def tellResult(self, u):
        print("%d연승" % u.win)

#####################
r = Referee()
r.start()