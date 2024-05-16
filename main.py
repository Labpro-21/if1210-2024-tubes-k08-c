import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data"))


import src.load as load
import src.save as save
import src.ascii_art as art
import src.jackpot as gacha
import src.register as register
import src.login as login
import src.exit_kill as exit_kill

# data loading
user_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data = load.load_files()

# login phase
print("Before entering system, please Login/Register")
logged_in = False
while not logged_in:
    login_choice = input("LOGIN / REGISTER : ").upper()
    if login_choice == "LOGIN":
        logged_id, logged_in = login.login(user_data)
    elif login_choice == "REGISTER":
        logged_id, logged_in, inv_monster_data = register.register_ui(user_data, monster_data, inv_monster_data)
    else:
        print("choose a valid option")

# main game phase
while True:
    choice = input("next action (SAVE/GACHA/EXIT) testing : ").upper()
    if choice == "SAVE":
        save.save(user_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data)
    elif choice == "GACHA":
        gacha.gacha(1, 250, monster_data, inv_monster_data)
    elif choice == "EXIT":
        exit_kill.exit_kill(user_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data)
        break
