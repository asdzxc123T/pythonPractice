for i in range(5):
    for j in range(5):
        for k in range(5):
            if k == 2:
                break # 가까운 거 : k for
            print(i, j, k)
print("-----")

# k가 2 되면 i 깨지게
a = False
for i in range(5):
    for j in range(5):
        for k in range(5):
            if k == 2:
                a = True
                break
            print(i, j, k)
        if a:
            break
    if a:
        break
# == True는 생략 가능
# == False는 not
print("-----")

for i in range(5):
    a = False
    for j in range(5):
        for k in range(5):
            if k == 2:
                a = True
                break
            print(i, j, k)
        if a:
            break