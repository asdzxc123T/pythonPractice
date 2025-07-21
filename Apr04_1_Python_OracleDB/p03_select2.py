# 평균가
from oracledb import connect
con = connect("ljw100/91270290@195.168.9.124:1521/xe")
sql = "select avg(p_price) from apr03_product"
cur = con.cursor()
cur.execute(sql)
for p in cur:
    for i in p:
        print(i)
cur.close()
con.close()
