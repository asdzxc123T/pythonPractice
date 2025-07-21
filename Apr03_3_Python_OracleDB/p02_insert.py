from oracledb import connect

# 연결
con = connect("ljw100/91270290@195.168.9.124:1521/xe")

# 데이터 확보
name = input("상품명 : ")
price = int(input("가격 : "))

# SQL을 str로 (; 빼고)
sql = "INSERT INTO apr03_product values ('%s', %d)" % (name, price)

# DB 관련 작업을 다 해주는 매니저 겸 결과
cur = con.cursor()

# SQL을 DB 서버로 전송
# 전송한 SQL을 원격실행
# 실행 결과를 받아오고
cur.execute(sql)

# 실행결과
#   CUD : 데이터 몇개가 영향 받았나
#   R : 데이터

if cur.rowcount == 1:
    print("성공")
    con.commit()

# 바로 DB 서버에 반영 x
# 체크해보고 다 맞다 : commit
# 체크해봤는데 아닌 게 존재 : rollback

cur.close()
con.close()