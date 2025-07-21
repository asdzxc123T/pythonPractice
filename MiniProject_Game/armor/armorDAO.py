from armor.armor import Armor
from ljw.ljwDBManager import ljwDBManager

class ArmorDAO:
    def getPlayerArmor(player):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from armor where ar_no = %d" % player.ar_no
            cur.execute(sql)
            for no, name, phyDef, magDef, strRes, dexRes, intRes, price in cur:
                return Armor(no, name, phyDef, magDef, strRes, dexRes, intRes, price)
        except:
            return "검색 실패"
        finally:
            ljwDBManager.closeConCur(con, cur)

    def getAllArmor():
        armors = []
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from armor"
            cur.execute(sql)
            for no, name, phyDef, magDef, strRes, dexRes, intRes, price in cur:
                a = Armor(no, name, phyDef, magDef, strRes, dexRes, intRes, price)
                armors.append(a)
        except:
            armors = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return armors