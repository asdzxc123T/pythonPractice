from random import randint

class Computer:
    def __init__(self):
        self.handTable = ["가위", "바위", "보"]

    def gameStart(self, u, e):
        self.printRule()
        win = 0
        while True:
            enemyHand = e.enemyFire()
            userHand = u.userFire()
            self.printHand(userHand, enemyHand)
            result = self.judge(userHand, enemyHand)
            if result == -1:
                print("%d연승" % win)
                break
            win += result
    
    def printRule(self):
        for i in range(len(self.handTable)):
            print("%d) %s" % (i + 1, self.handTable[i]))
        print("-----")
    
    def printHand(self, userHand, enemyHand):
        print("나 : %s" % self.handTable[userHand])
        print("컴 : %s" % self.handTable[enemyHand])

    def judge(self, userHand, enemyHand):
        t = userHand - enemyHand
        if t == 0:
            print("무")
            return 0
        elif t == 1 or t == -2:
            print("승")
            return 1
        else:
            print("패")
            return -1

class Enemy:
    def enemyFire(self):
        return randint(0, 2)

class User:
    def userFire(self):
        userHand = int(input("뭐 : "))
        if 0 < userHand < 4:
            return userHand - 1
        return self.userFire()

#########################################
c = Computer()
u = User()
e = Enemy()
c.gameStart(c, u, e)