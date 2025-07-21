from pymongo import MongoClient
# OracleDB
#   SQL이라는 별개의 언어로 제어
#   table
#   data(record)

# MongoDB
#   JavaScript라는 PL로 제어 : Python과 비슷
#   JavaScript의 배열 : [] : Python의 list
#   JavaScript의 객체 : {} : Python의 dict
#   => pymongo : mongoDB 명령어 거의 그대로 쓰게 해줌

# Objective-C   -> [d bark]
# JavaScript    -> d.bark()
# Python
#   Dog.bark(d) -> d.bark()

# 연결
con = MongoClient("195.168.9.68")
db = con.ljw

# 데이터 확보
name = input("이름 : ")
price = int(input("가격 : "))

# 명령어 서버로 전송 + 원격실행 + 결과받기
result = db.apr14_snack.insert_one({"s_name" : name, "s_price" : price})

if result.acknowledged:
    print("성공")

# 정리
con.close()