from oracledb import connect
con = connect("ljw100/91270290@195.168.9.124:1521/xe")
name = input("상품명 : ")
price = input("바꿀 가격 : ")
sql = "update apr03_product set p_price = %s where p_name = '%s'" % (price, name)
# print(sql)
cur = con.cursor()
cur.execute(sql)
if cur.rowcount >= 1:
    print("성공")
    con.commit()
cur.close()
con.close()
