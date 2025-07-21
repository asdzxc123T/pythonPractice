from weapon.weapon import Weapon
from ljw.ljwDBManager import ljwDBManager

class WeaponDAO:
    def getPlayerWeapon(player):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from weapon where w_no = %d" % player.w_no
            cur.execute(sql)
            for no, name, type, phyDmg, magDmg, strRes, dexRes, intRes, price in cur:
                return Weapon(no, name, type, phyDmg, magDmg, strRes, dexRes, intRes, price)
        except:
            return "검색 실패"
        finally:
            ljwDBManager.closeConCur(con, cur)
    
    def getAllWeapon():
        weapons = []
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from weapon"
            cur.execute(sql)
            for no, name, type, phyDmg, magDmg, strRes, dexRes, intRes, price in cur:
                w = Weapon(no, name, type, phyDmg, magDmg, strRes, dexRes, intRes, price)
                weapons.append(w)
        except:
            weapons = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return weapons