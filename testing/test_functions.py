import json
from Items import items as i
import os


def test_enemy_info():
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, '../Enemy/enemies_info.json')
    with open(file, "r") as f:
        test = json.load(f)
    for topic in test.keys():
        testbook = i.Book(topic)
        testbook.learn_info()