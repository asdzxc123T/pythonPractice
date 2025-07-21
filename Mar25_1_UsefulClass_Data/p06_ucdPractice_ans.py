f = open("C:/ljw/KakaoTalkChats.txt", "r", encoding="utf-8")
words = {}
for i, line in enumerate(f.readlines()):
    msg = None
    if i > 4:
        line = line.replace("\n", "")
        if (not line.startswith("20")) and (line != ""):
            msg = line
        else:
            try:
                line = line.split(" : ")
                msg = line[1]
                for ii, word in enumerate(line):
                    if ii > 1:
                        msg += " " + line[ii]
            except:
                pass
        if msg != None:
            msg = msg.strip().split(" ")
            for word in msg:
                if word in words: # 그런 키값이 dict에 있냐
                    words[word] += 1
                else:
                    words[word] = 1
f.close()

# f = open("C:/ljw/0326.csv", "a", encoding="utf-8")
f = open("C:/ljw/0326.txt", "w", encoding="utf-8")
# words라는 dict에 있는 거를
# 0326.csv에 기록
for word, count in words.items():
    f.write("%s\t%d\n" % (word, count))
f.close()