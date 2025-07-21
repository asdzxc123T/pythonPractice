from GameOptions import reqExp, cType, sType

class ConsoleScreen:
    def showMainMenu():
        print("-----")
        print("1) 캐릭터 선택")
        print("2) 캐릭터 생성")
        print("3) 캐릭터 삭제")
        print("4) 종료")
        return input("뭐 : ")
    
    def selectCharacter(characters):
        print("-----")
        for n, c in enumerate(characters):
            print("%d) 이름 : %s\tLevel %d" % (n + 1, c.name, c.lv))
        print("-----")
        i = int(input("어떤 캐릭? : "))
        return characters[i - 1]
    
    def showPlayerMenu(player):
        print("-----")
        print("%s(lv %d)" % (player.name, player.lv))
        print("-----")
        print("1) 던전 가기")
        print("2) 상점 가기")
        print("3) 스킬 배우기")
        print("4) 캐릭터 상태 보기")
        print("5) 종료")
        return input("뭐 : ")
    
    def showPlayerStat(player, equipWeapon, equipArmor, equipSkill):
        print("-----")
        print("이름: %s" % player.name)
        print("Level : %d, exp : %d / %d" % (player.lv, player.exp, reqExp[player.lv]))
        print("HP : %d / %d, MP : %d / %d" % (player.currentHp, player.hp, player.currentMp, player.mp))
        print("물리 공격력 : %d + %d" % (player.baseAttack, equipWeapon.phyDmg))
        print("마법 공격력 : %d + %d" % (player.int, equipWeapon.magDmg))
        print("물리 방어력: %d + %d" % (player.baseDefense, equipArmor.phyDef))
        print("마법 방어력: %d + %d" % (player.int, equipArmor.magDef))
        print("힘 : %d, 민첩 : %d, 지능 : %d" % (player.str, player.dex, player.int))
        print("직업 : %s" % cType[player.type])
        print("보유 골드 : %dg" % player.gold)
        print("무기 : %s" % equipWeapon.name)
        print("방어구 : %s" % equipArmor.name)
        print("보유 스킬 : ")
        for s in equipSkill:
            print("\t%s : (%s) %.1f배율로 공격, HP %d/MP %d 소모" % (s.name, sType[s.type], s.mul, s.costHP, s.costMP))
        print("-----")

    def showShopMenu():
        print("-----")
        print("1) 무기")
        print("2) 방어구")
        print("3) 나가기")
        return input("뭐 : ")     
    
    def showPlayerGold(player):
        print("-----")
        print("현재 보유 골드 : %d" % player.gold)
        print("-----")
        
    def showBuyMenu(items):
        print("-----")
        for i in items:
            print("%d) %s: %dg" % (i.no, i.name, i.price))
        return input("뭐(0 입력 시 되돌아가기) : ")

    def showResult(result):
        print("-----")
        print(result)
        print("-----")

    def showDungeonMenu(floor, allFloors, player):
        print("-----")
        print("현재 상태")
        print("Level : %d, exp : %d / %d" % (player.lv, player.exp, reqExp[player.lv]))
        print("HP : %d / %d, MP : %d / %d" % (player.currentHp, player.hp, player.currentMp, player.mp))
        print("gold : %d" % player.gold)
        print("-----")
        print("%d/%d층에 진입" % (floor, allFloors))
        print("1) 전진")
        print("2) 돌아가기")
        return input("뭐 : ")
    
    def showEncounter(monster, num):
        if num == 1:
            print("-----")
            print("%s와(과) 마주쳤다!" % monster.name)
            print("-----")

    def playerChoice(player, monster, equipWeapon, equipArmor):
        print("-----")
        print("플레이어 정보")
        print("HP : %d / %d, MP : %d / %d" % (player.currentHp, player.hp, player.currentMp, player.mp))
        print("물리 공격력 : %d + %d" % (player.baseAttack, equipWeapon.phyDmg))
        print("마법 공격력 : %d + %d" % (player.int, equipWeapon.magDmg))
        print("물리 방어력: %d + %d" % (player.baseDefense, equipArmor.phyDef))
        print("마법 방어력: %d + %d" % (player.int, equipArmor.magDef))
        print("-----")
        print("적 정보")
        print("이름 : %s, HP : %d / %d, %s 공격력 : %d" % (monster.name, monster.currentHp, monster.hp, sType[monster.type], monster.baseAttack))
        print("-----")
        print("1) 공격")
        print("2) 스킬 사용")
        print("3) 도망")
        return input("뭐 : ")
    
    def printDamage(a, b, d):
        print("-----")
        print("%s의 공격" % a)
        print("%s이(가) %s에게 %d의 데미지를 입힘" % (a, b, d))
        print("-----")

    def printNotEnoughCost():
        print("스킬을 사용하기에 HP나 MP가 부족함")

    def showGoldAndExp(monster):
        print("-----")
        print("%s를 잡고 돈 %dg와 경험치 %d를 얻음" % (monster.name, monster.gold, monster.exp))
        print("-----")
    
    def showLevelUp(player, s, d, i):
        print("-----")
        print("레벨 업")
        print("레벨이 %d로 오르면서 힘이 %d, 민첩이 %d, 지능이 %d만큼 오름" % (player.lv, s, d, i))
        print("-----")

    def playerSkillChoice(equipSkill):
        print("-----")
        for n, s in enumerate(equipSkill):
            print("%d) %s : (%s) %.1f배율로 공격, HP %d/MP %d 소모" % (n + 1, s.name, sType[s.type], s.mul, s.costHP, s.costMP))
        i = int(input("뭐 : "))
        return equipSkill[i - 1]

    def showCertainWeapon(weaponList, weaponShopMenu):
        print("-----")
        print("%s" % weaponList[int(weaponShopMenu) - 1].name)
        print("\t물리 공격력 : %d" % weaponList[int(weaponShopMenu) - 1].phyDmg)
        print("\t마법 공격력 : %d" % weaponList[int(weaponShopMenu) - 1].magDmg)
        print("\t힘 제한 : %d" % weaponList[int(weaponShopMenu) - 1].strRes)
        print("\t민첩 제한 : %d" % weaponList[int(weaponShopMenu) - 1].dexRes)
        print("\t지능 제한 : %d" % weaponList[int(weaponShopMenu) - 1].intRes)
        print("\t가격 : %d" % weaponList[int(weaponShopMenu) - 1].price)
        print("-----")
        print("1) 구매")
        print("2) 돌아가기")
        i = "3"
        while i != "1" and i != "2":
            i = input("뭐 : ")
        return i
    
    def showCertainArmor(armorList, armorShopMenu):
        print("-----")
        print("%s" % armorList[int(armorShopMenu) - 1].name)
        print("\t물리 방어력 : %d" % armorList[int(armorShopMenu) - 1].phyDef)
        print("\t마법 방어력 : %d" % armorList[int(armorShopMenu) - 1].magDef)
        print("\t힘 제한 : %d" % armorList[int(armorShopMenu) - 1].strRes)
        print("\t민첩 제한 : %d" % armorList[int(armorShopMenu) - 1].dexRes)
        print("\t지능 제한 : %d" % armorList[int(armorShopMenu) - 1].intRes)
        print("\t가격 : %d" % armorList[int(armorShopMenu) - 1].price)
        print("-----")
        print("1) 구매")
        print("2) 돌아가기")
        i = "3"
        while i != "1" and i != "2":
            i = input("뭐 : ")
        return i
    
    def inputCharacterInfo():
        print("-----")
        print("캐릭터 생성")
        name = input("이름 : ")
        print("1) 전사")
        print("2) 마법사")
        ntype = "3"
        while ntype != "1" and ntype != "2":
            ntype = input("직업 : ")
        return name, ntype

    def foundWeapon(player, randomItem, equipWeapon):
        print("-----")
        print("보물상자 발견, 그 안에 무기가 있음")
        print("-----")
        print("%s" % randomItem.name)
        print("\t물리 공격력 : %d" % randomItem.phyDmg)
        print("\t마법 공격력 : %d" % randomItem.magDmg)
        print("\t힘 제한 : %d" % randomItem.strRes)
        print("\t민첩 제한 : %d" % randomItem.dexRes)
        print("\t지능 제한 : %d" % randomItem.intRes)
        print("\t가격 : %d" % randomItem.price)
        print("-----")
        print("현재 장착 무기")
        print("%s" % equipWeapon.name)
        print("\t물리 공격력 : %d" % equipWeapon.phyDmg)
        print("\t마법 공격력 : %d" % equipWeapon.magDmg)
        print("-----")
        print("1) 장착")
        print("2) 버리기")
        return input("뭐 : ")
    
    def foundArmor(player, randomItem, equipArmor):
        print("-----")
        print("보물상자 발견, 그 안에 갑옷이 있음")
        print("-----")
        print("%s" % randomItem.name)
        print("\t물리 방어력 : %d" % randomItem.phyDef)
        print("\t마법 방어력 : %d" % randomItem.magDef)
        print("\t힘 제한 : %d" % randomItem.strRes)
        print("\t민첩 제한 : %d" % randomItem.dexRes)
        print("\t지능 제한 : %d" % randomItem.intRes)
        print("\t가격 : %d" % randomItem.price)
        print("-----")
        print("현재 장착 갑옷")
        print("%s" % equipArmor.name)
        print("\t물리 방어력 : %d" % equipArmor.phyDef)
        print("\t마법 방어력 : %d" % equipArmor.magDef)
        print("-----")
        print("1) 장착")
        print("2) 버리기")
        return input("뭐 : ")
    
    def foundSomeone(monster):
        print("-----")
        print("%s가 누군가를 공격하는 것을 봄" % monster.name)
        print("-----")
        print("1) 돕기")
        print("2) 못 본 척하기")
        return input("뭐 : ")

    def getGift(g):
        print("-----")
        print("구해준 사람에게 사례로 %dg를 받음" % g)