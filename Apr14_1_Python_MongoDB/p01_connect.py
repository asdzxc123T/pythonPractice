# Python + OracleDB : cx_Oracle.py -> oracledb.py
# Python + MongoDB : pymongo.py

# 시작 - cmd
#   pip install pymongo

from pymongo import MongoClient


con = MongoClient("195.168.9.68") # 서버 주소[:포트번호]
print(con)
db = con.ljw
print(db)
con.close()
