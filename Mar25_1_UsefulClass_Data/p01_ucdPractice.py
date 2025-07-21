data = input("숫자(a,b,c,...) : ")
data = data.split(",")
sum = 0
normal = len(data)
for i in range(len(data)):
    data[i] = data[i].strip()
    try:
        data[i] = int(data[i])
        sum += data[i]
    except:
        normal -= 1
avg = sum / normal
print(sum, avg)