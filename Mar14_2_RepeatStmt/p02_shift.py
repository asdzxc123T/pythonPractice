value = 3

data = ["와이파이", "주차장", "흡연실", "24시간"]
for i in range(len(data)):
    if (value >> i) % 2:
        print(data[i])

print("-------------")

# data = ["24시간", "흡연실", "주차장", "와이파이"]
# t = 1 << len(data)
# for i in range(len(data)):
#     t = t >> 1
#     if value >= t:
#         print(data[i])
#         value -= t

data = ["와이파이", "주차장", "흡연실", "24시간"]
for i in range(len(data) - 1, -1, -1):
    if value >= (1 << i):
        print(data[i])
        value -= (1 << i)