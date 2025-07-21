# 1
# 2
# 3

# for i in range(1, 4):
#     print(i)
print("1")
print("2")
print("3")
print("-----")

# 1
# 2
# ...
# 10
for i in range(1, 11):
    print(i)
print(range(1, 11), type(range(1, 11)))
print("-----")

# 1
# 3
# 5
# 7
# 9

# l = range(1, 10, 2)
# l = list(l)
# for i in l:
#   ...
for i in range(1, 10, 2):
    print(i)
print("-----")

# 9
# 7
# 5
# 3
# 1
for i in range(9, 0, -2):
    print(i)
print("-----")  # 규칙적인 숫자 만들기

# 1 + 2 + 3 + 4 + 5 = ?
sum = 0
for i in range(1, 6):
    sum += i
print(sum)
print("-----")

# 1 + 3 + 5 + ... + 19 = ?
sum = 0
for i in range(1, 20, 2):
    sum += i
print(sum)
print("-----")

# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 9 = 18
for i in range(1, 10):
    print("2 x %d = %d" % (i, 2 * i))
print("-----")

# 2 x 1 = 2
# ...
# 9 x 9 = 81
for i in range(2, 10):
    for j in range(1, 10):
        print("%d x %d = %d" % (i, j, i * j))
print("-----")

# 2 x 1 = 2     3 x 1 = 3   ...     9 x 1 = 9
# ...
# ...                               9 x 9 = 81
for i in range(1, 10):
    for j in range(2, 10):
        print("%d x %d = %d" % (j, i, i * j), end="\t")
    print()
print("-----")
# ㅋㅋㅋㅋㅋ
# ㅋㅋㅋㅋㅋ
# ㅋㅋㅋㅋㅋ
# ㅋㅋㅋㅋㅋ
# ㅋㅋㅋㅋㅋ
for i in range(5):
    for j in range(5):
        print("ㅋ", end="")
    print()
print("-----")
# ㅋ
# ㅋㅋ
# ㅋㅋㅋ
# ㅋㅋㅋㅋ
# ㅋㅋㅋㅋㅋ
for i in range(5):
    for j in range(i + 1):
        print("ㅋ", end="")
    print()
print("-----")
# ㅋㅋㅋㅋㅋ
# ㅋㅋㅋㅋ
# ㅋㅋㅋ
# ㅋㅋ
# ㅋ
for i in range(5):
    for j in range(5 - i):
        print("ㅋ", end="")
    print()
print("-----")
# ㅋ
#   ㅋ
#     ㅋ
#       ㅋ
#         ㅋ

# for i in range(5):
#     for j in range(i + 1):
#         if i == j:
#             print("ㅋ", end="")
#         else: 
#             print("  ", end="")
#     print()
for i in range(5):
    for j in range(i):
        print("  ", end="")
    print("ㅋ")
print("-----")

# ㅋ
# ㅎㅎㅎ
# ㅋㅋㅋㅋㅋ
# ㅎㅎㅎㅎㅎㅎㅎ
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋ

# for i in range(5):
#     for j in range(2 * i + 1):
#         if i % 2 == 0:
#             print("ㅋ", end="")
#         else:
#             print("ㅎ", end="")
#     print()
for i in range(5):
    if i % 2 == 0:
        s = "ㅋ"
    else:
        s = "ㅎ"
    for j in range(i * 2 + 1):
        print(s, end="")
    print()