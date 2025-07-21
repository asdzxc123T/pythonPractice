# 월요일 학원 올 때마다 지하철
# 월요일만 출근
# 가설 설정 -> 월요일에 지하철 이용객 수가 가장 많다
# 요일별 이용객수(탄+내린) 평균
# 월 12941930
# 화 12349132

#   2015,01,01,1호선,서울역,45000,30000

# 요일별로 일단 다 더하고
# 다 더한거 데이터 수로 나눠야
# => dict


from datetime import datetime


f = open("C:/ljw/subway.csv", "r", encoding="utf-8")
subwaySum = {"Sun": 0, "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0}
subwayCnt = {"Sun": 0, "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0}
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    # if line[1] == "02":
    #     break
    when = line[0] + "-" + line[1] + "-" + line[2]
    when = datetime.strptime(when, "%Y-%m-%d")
    wd = datetime.strftime(when, "%a")
    subwaySum[wd] += int(line[5]) + int(line[6])
    subwayCnt[wd] += 1
f.close()

# 짝 맞춰서 나눈 평균
# subwayResult.csv로 저장
f = open("C:/ljw/subwayResult.csv", "w", encoding="utf-8")
for wd, sum in subwaySum.items():
    f.write("%s,%.2f\n" % (wd, sum / subwayCnt[wd]))
f.close()
