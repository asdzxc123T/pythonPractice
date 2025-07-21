from random import randint

class Respondent:
    def start(self, q):
        gameAns = self.pickGameAns()
        self.gameStart(gameAns, q)

    def pickGameAns(self):
        gameAns = randint(1, 10000)
        print("정답은 %d" % gameAns)
        return gameAns

    def gameStart(self, gameAns, q):
        cnt = 0
        while True:
            userAns = self.ask(q)
            cnt += 1
            if self.judge(gameAns, userAns):
                break
        print("%d번만에 정답" % cnt)
    
    def ask(self, q):
        userAns = q.guess()
        if 0 < userAns < 10001:
            return userAns
        return self.ask(q)

    def judge(self, gameAns, userAns):
        if userAns > gameAns:
            print("DOWN")
        elif userAns < gameAns:
            print("UP")
        else:
            return True
        return False
    
class Questioner:
    def guess(self):
        return int(input("뭐 : "))
#########################
r = Respondent()
q = Questioner()
r.start(q)