from random import randint
from gameCharacter.gameCharacter import GameCharacter
from ljw.ljwDBManager import ljwDBManager
from GameOptions import reqExp, cType, sType

class GCDAO:
    def getCharacters():
        characters = []
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from gameCharacter"
            cur.execute(sql)
            for no, name, lv, exp, hp, mp, baseAttack, baseDefense, str, dex, inte, type, gold, w_no, ar_no in cur:
                c = GameCharacter(no, name, lv, exp, hp, mp, baseAttack, baseDefense, str, dex, inte, type, gold, w_no, ar_no)
                characters.append(c)
        except:
            characters = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return characters
        
    def buyWeapon(player, weaponList, weaponShopMenu):
        if weaponList[int(weaponShopMenu) - 1].price > player.gold:
            return "구매 불가, 골드가 %d 밖에 없음" % player.gold
        if weaponList[int(weaponShopMenu) - 1].strRes > player.str or weaponList[int(weaponShopMenu) - 1].dexRes > player.dex or weaponList[int(weaponShopMenu) - 1].intRes > player.int:
            return "구매 불가, 능력치가 부족함"
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "update gameCharacter set c_w_no = %s, c_gold = %d where c_no = %d" % (weaponShopMenu, player.gold - weaponList[int(weaponShopMenu) - 1].price, player.no)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                player.w_no = int(weaponShopMenu)
                player.gold -= weaponList[int(weaponShopMenu) - 1].price
                return "구매 성공"
        except:
            return "오류로 인해 구매 불가"
        finally:
            ljwDBManager.closeConCur(con, cur)

    def buyArmor(player, armorList, armorShopMenu):
        if armorList[int(armorShopMenu) - 1].price > player.gold:
            return "구매 불가, 골드가 %d 밖에 없음" % player.gold
        if armorList[int(armorShopMenu) - 1].strRes > player.str or armorList[int(armorShopMenu) - 1].dexRes > player.dex or armorList[int(armorShopMenu) - 1].intRes > player.int:
            return "구매 불가, 능력치가 부족함"
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "update gameCharacter set c_ar_no = %s, c_gold = %d where c_no = %d" % (armorShopMenu, player.gold - armorList[int(armorShopMenu) - 1].price, player.no)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                player.ar_no = int(armorShopMenu)
                player.gold -= armorList[int(armorShopMenu) - 1].price
                return "구매 성공"
        except:
            return "오류로 인해 구매 불가"
        finally:
            ljwDBManager.closeConCur(con, cur)

    def buySkill(player, skillList, shopMenu):
        if skillList[int(shopMenu) - 1].price > player.gold:
            return "구매 불가, 골드가 %d 밖에 없음" % player.gold
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "update gameCharacter set c_gold = %d where c_no = %d" % (player.gold - skillList[int(shopMenu) - 1].price, player.no)
            cur.execute(sql)
            player.gold -= skillList[int(shopMenu) - 1].price
            sql = "insert into rel_c_s values (%d, %d)" % (player.no, skillList[int(shopMenu) - 1].no)
            cur.execute(sql)
            con.commit()
            return "구매 성공"
        except:
            return "오류로 인해 구매 불가"
        finally:
            ljwDBManager.closeConCur(con, cur)

    def loseGold(player):
        amount = randint(1, player.gold // 10)
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "update gameCharacter set c_gold = %d where c_no = %d" % (player.gold - amount, player.no)
            cur.execute(sql)
            player.gold -= amount
            con.commit()
            return "도망쳐나오다 %dg를 잃음..." % amount
        except:
            return "오류"
        finally:
            ljwDBManager.closeConCur(con, cur)

    def getGoldAndExp(player, monster):
        player.gold += monster.gold
        if player.lv != 10:
            player.exp += monster.exp
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "update gameCharacter set c_gold = %d, c_exp = %d where c_no = %d" % (player.gold, player.exp, player.no)
            cur.execute(sql)
            con.commit()
        except:
            pass
        finally:
            ljwDBManager.closeConCur(con, cur)
    
    def levelUp(player):
        if player.type == 1:
            s = randint(1, 3)
            d = randint(1, 3)
            i = randint(1, 2)
        else:
            s = randint(1, 2)
            d = randint(1, 2)
            i = randint(1, 4)
        player.exp -= reqExp[player.lv]
        player.lv += 1
        if player.lv == 10:
            player.exp = 0
        player.str += s
        player.dex += d
        player.int += i
        player.hp += 5 * s
        player.currentHp = player.hp
        player.mp += i
        player.currentMp = player.mp
        player.baseAttack = player.str + player.dex // 2
        player.baseDefense = player.str // 3 + player.dex // 2
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "update gameCharacter set c_lv = %d, c_exp = %d, " % (player.lv, player.exp)
            sql += "c_str = %d, c_dex = %d, c_int = %d, " % (player.str, player.dex, player.int)
            sql += "c_hp = %d, c_mp = %d, c_baseAttack = %d, c_baseDefense = %d " % (player.hp, player.mp, player.baseAttack, player.baseDefense)
            sql += "where c_no = %d" % player.no
            cur.execute(sql)
            con.commit()
            return s, d, i
        except:
            pass
        finally:
            ljwDBManager.closeConCur(con, cur)

    def createCharacter(name, ntype):
        if ntype == "1":
            s = 5
            d = 4
            i = 3
            w_no = 1
        else:
            s = 2
            d = 3
            i = 7
            w_no = 10
        hp = s * 5
        mp = i
        baseAttack = s + d // 2
        baseDefense = s // 3 + d // 2
        ar_no = 1
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "insert into gameCharacter values (character_seq.nextval, '%s', 1, 0, %d, %d, %d, %d, %d, %d, %d, %s, 100, %d, %d)" % (name, hp, mp, baseAttack, baseDefense, s, d, i, ntype, w_no, ar_no)
            cur.execute(sql)
            con.commit()
            return "캐릭터 생성됨"
        except:
            return "캐릭터 생성 안 됨"
        finally:
            ljwDBManager.closeConCur(con, cur)

    def deleteCharacter(selected):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "delete from gameCharacter where c_no = %d" % selected.no
            cur.execute(sql)
            con.commit()
            return "캐릭터 삭제됨"
        except:
            return "캐릭터 삭제 안 됨"
        finally:
            ljwDBManager.closeConCur(con, cur)

    def updateCharacter(player, randomItem, i):
        iType = [None, "c_w_no", "c_a_no"]
        if randomItem.strRes > player.str or randomItem.dexRes > player.dex or randomItem.intRes > player.int:
            return "장착 불가, 능력치가 부족함"
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "update gameCharacter set %s = %d where c_no = %d" % (iType[i], randomItem.no, player.no)
            cur.execute(sql)
            con.commit()
            return "캐릭터 삭제됨"
        except:
            return "캐릭터 삭제 안 됨"
        finally:
            ljwDBManager.closeConCur(con, cur)

    def getGift(player):
        gold = randint(10, 200)
        player.gold += gold
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "update gameCharacter set c_gold = %d where c_no = %d" % (player.gold, player.no)
            cur.execute(sql)
            con.commit()
            return gold
        except:
            pass
        finally:
            ljwDBManager.closeConCur(con, cur)