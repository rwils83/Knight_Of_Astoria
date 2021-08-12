from Enemy import enemies as e
from Items import items as i
from NPC import npc as n
from Missions import missions as m
from gameplay import menus as menus
from gameplay import gameactions as g
from gameplay import locations as l
from gameplay import player as p
from testing.test_functions import *
import json

if __name__ == "__main__":
    intro_menu = menus.MainMenu()
    gamemenu = intro_menu.create_menu()
    print(gamemenu)
    gamestart = intro_menu.return_menu()
    while gamestart == "loop":
        gamestart = intro_menu.get_menu_selection()
    player = p.Player(gamestart.player.name, gamestart.player.player_class)
    if player.name == "Jumpstart":
        player._mission_passed("Intro_Mission")
        silver_dagger = i.Weapon(2, 1, 10, 10, True, "Silver Dagger")
        player.add_to_inventory(silver_dagger.name, "Weapon", {"Damage":silver_dagger.damage,
                                                               "Quality":silver_dagger.quality,
                                                               "Equipped":silver_dagger.equipped,
                                                               "Cost": silver_dagger.cost})
    if player.missions_passed[-1] == "0":
        current_mission = m.Mission("Intro_Mission")
        current_mission._get_story()
        player.missions_passed.append("Intro_Mission")
    else:
        current_mission = m.Mission("Main_Mission_1")
        current_mission._get_story()

    test = l.Town()
    test.armory.print_menu()
    test.armory.clerk.sell_items()
    silver_sword = test.armory.clerk.items['Silver Sword']
    player.get_inventory()
    player.buy_item(silver_sword.name, "Weapon", {"Damage": silver_sword.damage,
                                                          "Quality": silver_sword.quality,
                                                          "Equipped": False,
                                                          "Cost": silver_sword.cost})
    player.get_inventory()
    player.equip_item("Weapon", "Silver Sword")
    player.get_inventory()
    player.equip_item("Weapon", "Silver Sword")
    player.get_inventory()
    player.equip_item("Weapon", "Silver Dagger")
    player.get_inventory()
    test_enemy_info()