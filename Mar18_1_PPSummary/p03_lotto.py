from random import randint

def check(result, t):
    for i in range(len(result)):
        if result[i] == t:
            return False
    return True

result = []
number = 0
while number < 6:
    t = randint(1, 45)
    if check(result, t):
        result.append(t)
        number += 1
print(result)