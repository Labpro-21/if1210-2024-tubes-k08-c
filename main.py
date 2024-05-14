import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data"))


import src.load as load
import src.save as save
import src.ascii_art as art
import src.jackpot as gacha



users_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data = load.load_files()


print(monster_data)
while True:
    choice = input("next action (save/gacha) testing : ")
    if choice == "save":
        save.save(users_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data)
    elif choice == "gacha":
        gacha.gacha(1, 250, monster_data, inv_monster_data)
