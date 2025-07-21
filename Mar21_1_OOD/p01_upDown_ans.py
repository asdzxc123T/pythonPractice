from random import randint

class Enemy:
    def thinkAns(self):
        return randint(1, 10000)
    
    def ask(self, u):
        userAns = u.tell()
        if 0 < userAns < 10001:
            return userAns
        return self.ask(u)
    
    def gameStart(self, u):
        turn = 0
        gameAns = self.thinkAns()
        while True:
            turn += 1
            userAns = self.ask(u)
            end = self.judge(gameAns, userAns)
            if end:
                self.tellResult(turn)
                break
            
    def judge(self, gameAns, userAns):
        if gameAns == userAns:
            print("정답")
            return True
        elif gameAns > userAns:
            print("UP")
        else:
            print("DOWN")
        return False
        
    def tellResult(self, turn):
        print("%d번만에 정답" % turn)

class User:
    def tell(self):
        return int(input("뭐 : "))
##############################
e = Enemy()
u = User()
e.gameStart(u)