# 1) snack.csv 읽어서 한줄씩 출력
# 2) 이름
#   가격
#   중량
# 3) 과자객체로 만들고 정보 출력
# 4) g당 가격순 정렬
class Snack:
    def __init__(self, line):
        line = line.replace("\n", "").split(",")
        self.name = line[0]
        self.price = int(line[1])
        self.weight = float(line[2])
        self.a = self.price / self.weight

    def showInfo(self):
        print(self.name)
        print(self.price)
        print(self.weight)
        print("-----")
################################
f = open("C:/ljw/snack.csv", "r", encoding="utf-8")
snacks = []
for line in f.readlines():
    snack = Snack(line)
    snacks.append(snack)
f.close()

snacks.sort(key=lambda s:s.price / s.weight)
for i in snacks:
    i.showInfo()

# .csv(Comma Separated Value)
#   엑셀에서 열면 이쁘게
#       전세계적 주력 : utf-8
#       win : euc-kr -> 이제는 utf-8
#       MS Office가 utf-8 감당 못함
#   메모장에서도 열리고
