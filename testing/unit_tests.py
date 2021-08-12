import pytest
from Enemy import enemies as e
from Items import items as i
from NPC import npc as n
from gameplay import player as p


def test_Enemy_function():
    werewolf = e.Werewolf(10, 1, 10)
    werewolf.take_damage("Silver Sword", 10)
    assert werewolf.health <= 0


def test_npc_functions():
    pass


def test_items_functions():
    silver_sword = i.Weapon(10, 5, 5, 2, True, 'Silver Sword')
    assert silver_sword.name == 'Silver Sword'
    assert silver_sword.damage == 10
    assert silver_sword.weight == 5
    assert silver_sword.cost == 5
    assert silver_sword.quality == 2
    assert silver_sword.equipped == True
    player = p.Player('Test', 'blah')
    player.add_to_inventory(silver_sword.name, 'Weapon', {"Damage": silver_sword.damage,
                                                          "Quality": silver_sword.quality,
                                                          "Equipped": False,
                                                          "Cost": silver_sword.cost})


def test_weapon_outputs():
    test_sword = i.Weapon(10, 5, 5, 2, True, "Silver Sword")
    assert test_sword.name == "Silver Sword"
    assert test_sword.equipped == True
    assert test_sword.quality == 2
    assert test_sword.damage == 10
    assert test_sword.type == "Weapon"
    assert "Silver" in test_sword.name


def test_armor_outputs():
    pass


def test_spells_outputs():
    pass

