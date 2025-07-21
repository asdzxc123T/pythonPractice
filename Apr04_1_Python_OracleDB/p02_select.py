from oracledb import connect

# 연결
con = connect("ljw100/91270290@195.168.9.124:1521/xe")
# 데이터 확보

# sql
sql = "select * from apr03_product"
# 총괄 매니저 겸 결과
cur = con.cursor() # DB 작업매니저 겸 결과
# 실행
cur.execute(sql)
for n, p in cur:
    print(n, p)
# 총괄매니저겸 결과 닫기
cur.close()
# 연결 닫기
con.close()