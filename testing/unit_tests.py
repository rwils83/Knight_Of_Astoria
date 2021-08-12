import pytest
from Enemy import enemies as e
from Items import items as i
from NPC import npc as n


def test_Enemy_function():
    werewolf = e.Werewolf(10, 1, 10)
    werewolf.take_damage("Silver Sword", 10)
    assert werewolf.health <= 0


def test_NPC_functions():
    pass


def test_Items_functions():
    pass


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

