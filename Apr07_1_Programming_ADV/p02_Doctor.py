# M, DAO
from ljw.ljwDBManager import ljwDBManager


class Doctor:
    def calculate(guest):
        con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")

        guest.bmi = guest.weight / (guest.height / 100) ** 2
        if guest.bmi >= 39:
            guest.bmiRes = "고도 비만"
        elif guest.bmi >= 32:
            guest.bmiRes = "중도 비만"
        elif guest.bmi >= 30:
            guest.bmiRes = "경도 비만"
        elif guest.bmi >= 24:
            guest.bmiRes = "과체중"
        elif guest.bmi >= 10:
            guest.bmiRes = "정상 체중"
        else:
            guest.bmiRes = "저체중"
        
        sql = "insert into apr07_bmi "
        sql += "values('%s', %f, %f, %f, '%s')" % (guest.name, guest.height, guest.weight, guest.bmi, guest.bmiRes)
        cur.execute(sql)
        if cur.rowcount == 1:
            print("Success")
            con.commit()
        ljwDBManager.closeConCur(con, cur)