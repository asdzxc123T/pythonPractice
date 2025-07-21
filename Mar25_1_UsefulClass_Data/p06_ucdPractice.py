f = open("C:/ljw/KakaoTalkChats.txt", "r", encoding="utf-8")
words = {}

for line in f.readlines():
    line = line.replace("\n", "")
    if line.find(" : ") != -1:
        line = line[line.find(" : ") + 3:]
        if not (
            line.startswith("http") or
            line.endswith("이모티콘") or
            line.endswith("jpg") or
            line.endswith("png") or
            line.endswith("mp4") or
            line.endswith("webp") or
            (line.startswith("[") and line.endswith("]"))
        ):
            line = line.strip().split(" ")
            for word in line:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1

f.close()

words = sorted(words.items(), key=lambda w: w[1], reverse=True)

f2 = open("C:/ljw/0326.txt", "w", encoding="utf-8")
for word, count in words:
    f2.write(f"{word}\t{count}\n")
f2.close()
