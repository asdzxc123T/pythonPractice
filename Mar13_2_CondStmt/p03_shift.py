value = 3

# 1이면 와이파이
# 2면 주차장
# 4면 흡연실
# 8이면 24시간

# 3이면 와이파이 주차장
# 12면 흡연실 24시간

# if value % 2:
#     print("와이파이")
# if (value >> 1) % 2:
#     print("주차장")
# if (value >> 2) % 2:
#     print("흡연실")
# if (value >> 3) % 2:
#     print("24시간")

data = ["와이파이", "주차장", "흡연실", "24시간"]
for i in range(len(data)):
    if (value >> i) % 2:
        print(data[i])

print("-------------")

# if value >= (1 << 3):
#     print("24시간")
#     value -= (1 << 3)
# if value >= (1 << 2):
#     print("흡연실")
#     value -= (1 << 2)
# if value >= (1 << 1):
#     print("주차장")
#     value -= (1 << 1)
# if value >= 1:
#     print("와이파이")

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