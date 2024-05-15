import src.load as load
import src.additionals.code_functions as code

users_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data = load.load_files()

upgrade_price = [100,200,300,500]

id = "2"

def laboratory():
    print("intro")
    while True:
        print("Guide")
        print(inv_monster_data)
        current_user_monsters = []
        no = 1
        for i in range(len(inv_monster_data)):
            if inv_monster_data[i]["user_id"] == id:
                monster_index = code.index(monster_data,inv_monster_data[i]["monster_id"],"id")
                print(f"{no}. {monster_data[monster_index]["type"]} ({inv_monster_data[i]["level"]})")
                current_user_monsters.append({"current_monster_id" : monster_data[monster_index]["id"]})
                current_user_monsters[i]["number"] = str(no)
                no += 1
        choice = input("")
        if choice.upper() == "EXIT":
            break
        elif code.exist(current_user_monsters,choice,"number"):
            monster_upgrade_index = code.index(inv_monster_data,current_user_monsters[int(choice)-1]["current_monster_id"],"monster_id")
            if int(inv_monster_data[monster_upgrade_index]["level"]) < 5:
                cost = upgrade_price[int(inv_monster_data[monster_upgrade_index]["level"])-1]
                user_money = int(users_data[code.index(users_data,id,'id')]["oc"])
                if user_money >= cost:
                    while True:
                        confirm = input(f"currently you have {user_money} owca coin. its going to cost you {cost} owca coins, are you sure you want to upgrade this monster?")
                        if confirm.upper() == "Y":
                            inv_monster_data[monster_upgrade_index]["level"] = str(int(inv_monster_data[monster_upgrade_index]["level"]) + 1)
                            users_data[code.index(users_data,id,'id')]["oc"] = str(user_money-cost)
                            break
                        elif confirm.upper() == "N":
                            break
                else:
                    print("um sorry we don't serve poor people here. come again when you have da bag.")
            else: print("it seems that your monster is at its maximum level")
        else:
            print("again, please type one of the numbers for the monster you wish to upgrade.")

print("""

      """)

