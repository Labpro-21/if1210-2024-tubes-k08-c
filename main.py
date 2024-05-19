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
import src.menu_help as menu
import src.logout as logout
import src.management_shop as shop_mng
import src.inventory as inv
import src.battle as bat
import src.monster_manage as mons_mng
import src.shop as shop
import src.arena as arena

# data loading

user_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data = load.load_files()

# login phase
while True:
    print("Before entering system, please Login/Register/Exit")
    logged_in = False
    logged_id = -999
    logged_username = ""
    while not logged_in:
        login_choice = input("LOGIN / REGISTER / EXIT: ").upper()
        if login_choice == "LOGIN":
            logged_username, logged_id, logged_in, = login.login(user_data)
        elif login_choice == "REGISTER":
            logged_username, logged_id, logged_in, inv_monster_data \
                = register.register_ui(user_data, monster_data, inv_monster_data)
        elif login_choice == "EXIT":
            exit_kill.exit_kill(user_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data)
        else:
            print("choose a valid option")
    logged_status = user_data[logged_id - 1]['role']
    # main game phase
    while logged_in:
        # coin refresher
        logged_coin = user_data[logged_id - 1]['oc']
        print("Use the command 'HELP' to see available actions")
        game_choice = input("").upper()
        if logged_status == "admin":
            if game_choice == "MONSTER":
                mons_mng.ui_monster(monster_data)
        if game_choice == "HELP":
            menu.help_ui(logged_status, logged_username)
        elif game_choice == "LOGOUT":
            logout.logout()
            break
        elif game_choice == "SHOP":
            if logged_status == "agent":
                shop.shop(shop_monster_data, monster_data, inv_monster_data, shop_item_data, inv_item_data, user_data,
                          logged_id)
            elif logged_status == "admin":
                shop_item_data, shop_monster_data = shop_mng.shop_management(monster_data, shop_item_data,
                                                                             shop_monster_data)
        elif game_choice == "INVENTORY":
            inv.inventory(logged_id, user_data, inv_item_data, inv_monster_data, monster_data)
        elif game_choice == "LAB":
            pass  # lab
        elif game_choice == "BATTLE":
            bat.battle(logged_id, user_data, inv_item_data, inv_monster_data, monster_data)
        elif game_choice == "ARENA":
            arena.arena(logged_id, user_data, inv_item_data, inv_monster_data, monster_data)
        elif game_choice == "GACHA":
            user_data, inv_monster_data = gacha.gacha(logged_id, logged_coin, user_data, monster_data, inv_monster_data)
        elif game_choice == "SAVE":
            save.save(user_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data)
        elif game_choice == "EXIT":
            exit_kill.exit_kill(user_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data)
        else:
            print("Enter a valid command")
