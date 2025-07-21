# 0326.csv 읽어서
# 횟수기준 내림차순
class Word:
    def __init__(self, line):
        line = line.replace("\n", "").split("\t")
        self.word = line[0]
        self.count = int(line[1])
    def showInfo(self):
        print(self.word, ":", self.count)
    

f = open("C:/ljw/0326.txt", "r", encoding="utf-8")

words = []
for line in f.readlines():
    line = line.replace("\n", "")
    words.append(Word(line))
f.close()

words.sort(key=lambda w: w.count, reverse=True)
for i, w in enumerate(words):
    if i == 10:
        break
    w.showInfo()