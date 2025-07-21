from dungeon import Dungeon
from skill.skillDAO import SkillDAO
from armor.armorDAO import ArmorDAO
from weapon.weaponDAO import WeaponDAO
from gameCharacter.gcDAO import GCDAO
from consoleScreen import ConsoleScreen


if __name__ == "__main__":
    weaponList = WeaponDAO.getAllWeapon()
    armorList = ArmorDAO.getAllArmor()
    skillList = SkillDAO.getAllSkill()
    while True:
        menu = ConsoleScreen.showMainMenu()
        if menu == "1":
            player = ConsoleScreen.selectCharacter(GCDAO.getCharacters())
            equipWeapon = WeaponDAO.getPlayerWeapon(player)
            equipArmor = ArmorDAO.getPlayerArmor(player)
            equipSkill = SkillDAO.getPlayerSkill(player)
            while True:
                playerMenu = ConsoleScreen.showPlayerMenu(player)
                if playerMenu == "1":
                    dungeon = Dungeon()
                    dungeon.dungeon(player, equipWeapon, equipArmor, equipSkill)
                elif playerMenu == "2":
                    while True:
                        ConsoleScreen.showPlayerGold(player)
                        shopMenu = ConsoleScreen.showShopMenu()
                        if shopMenu == "1":
                            weaponShopMenu = ConsoleScreen.showBuyMenu(weaponList)
                            if weaponShopMenu == "0":
                                break
                            if ConsoleScreen.showCertainWeapon(weaponList, weaponShopMenu) == 1:
                                ConsoleScreen.showResult(GCDAO.buyWeapon(player, weaponList, weaponShopMenu))
                                equipWeapon = WeaponDAO.getPlayerWeapon(player)
                        elif shopMenu == "2":
                            armorShopMenu = ConsoleScreen.showBuyMenu(armorList)
                            if armorShopMenu == "0":
                                break
                            if ConsoleScreen.showCertainArmor(armorList, armorShopMenu) == 1:
                                ConsoleScreen.showResult(GCDAO.buyArmor(player, armorList, armorShopMenu))
                                equipArmor = ArmorDAO.getPlayerArmor(player)
                        elif shopMenu == "3":
                            break
                elif playerMenu == "3":
                    while True:
                        ConsoleScreen.showPlayerGold(player)
                        shopMenu = ConsoleScreen.showBuyMenu(skillList)
                        if shopMenu == "0":
                            break
                        ConsoleScreen.showResult(GCDAO.buySkill(player, skillList, shopMenu))
                        equipSkill = SkillDAO.getPlayerSkill(player)
                elif playerMenu == "4":
                    ConsoleScreen.showPlayerStat(player, equipWeapon, equipArmor, equipSkill)
                elif playerMenu == "5":
                    break
        elif menu == "2":
            name, ntype = ConsoleScreen.inputCharacterInfo()
            ConsoleScreen.showResult(GCDAO.createCharacter(name, ntype))
        elif menu == "3":
            selected = ConsoleScreen.selectCharacter(GCDAO.getCharacters())
            ConsoleScreen.showResult(GCDAO.deleteCharacter(selected))
        elif menu == "4":
            break
    