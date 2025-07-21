# 월요일 학원 올 때마다 지하철
# 월요일만 출근
# 가설 설정 -> 월요일에 지하철 이용객 수가 가장 많다
# 요일별 이용객수(탄+내린) 평균
# 월 12941930
# 화 12349132

#   2015,01,01,1호선,서울역,45000,30000

from datetime import datetime

sum = [0, 0, 0, 0, 0, 0, 0]
count = [0, 0, 0, 0, 0, 0, 0]

f = open("C:/ljw/subway.csv", "r", encoding="utf-8")
for line in f.readlines():
    line = line.replace("\n", "")
    data = line.split(",")
    wd = datetime(int(data[0]), int(data[1]), int(data[2])).weekday()
    count[wd] += 1
    sum[wd] += (int(data[5]) + int(data[6]))
f.close()

f = open("C:/ljw/subwayResult.csv", "w", encoding="utf-8")
wday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i in range(0, 7):
    print("%s : 평균 %d명, 총 %d명" % (wday[i], sum[i] / count[i], sum[i]))
    f.write("%s,%d\n" % (wday[i], sum[i] / count[i]))
f.close()

result = {}
f = open("C:/ljw/subwayResult.csv", "r", encoding="utf-8")
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    result[line[0]] = int(line[1])
f.close()
result = sorted(result.items(), key=lambda a: a[1], reverse=True)
print(result)