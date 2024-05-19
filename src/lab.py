    # fungsi untuk mengecek keberadaan suatu elemen dalam list of dictionaries
def exist(list_of_dict,n,category):
    for i in range(len(list_of_dict)):
        if list_of_dict[i][category] == n:
            return True
    return False

# fungsi untuk mengembalikan indeks dari suatu elemen yang dicari dalam list of dictionaries
def index(list_of_dict,n,category):
    for i in range(len(list_of_dict)):
        if list_of_dict[i][category] == n:
            return i

# fungsi untuk membuat textbox (hiasan)
def textbox(text):
    print("╔" + "═"*(len(text)+2) + "╗")
    print("║" + " " + text + " " + "║")
    print("╚" + "═"*(len(text)+2) + "╝")


def laboratory(inv_monster_data, monster_data,users_data,user_id):
    upgrade_price = [100,200,300,500]
    print("""
███████████████████████▓▓▓▓▓██████████████████████
████████████████████▓▓▓▓▓▓▓▓▓▓▓███████████████████
███████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████
███████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████
███████████████████▓▓█▓▓▓▓▓▓▓█▓▓██████████████████
███████████████████▓▓▒▒▒▓▓▓▒▒▓▓▓██████████████████
████████████████████▓▒░░░░░░░▒▓███████████████████
████████████████████▓▓░░░░░░░▓▓███████████████████
████████████████████▓█▓▒░░▒▒██▓███████████████████
███████████████████████▓▒▓▓▒██████████████████████
████████████████████▓▓▓▒▒█▓▒▓▓████████████████████
████████████████▓▒▒░░▒▒░░▓▒░▒▓▓█▓▒▓███████████████
███████████████▓░░░░░░▒░░▓▒░▒▓█▒░░░▒██████████████
███████████████▒░░░░░░░░▒▓▒▒▒█▒░░▒░░██████████████
╔══════════════════════╗
║ Makise The Scientist ║
╚══════════════════════╝       
          """)
    textbox("welcome to MAKISE'S LAB! i can make your monster to be stronger than ever! choose the one you'd like to upgrade by typing its [number] or leave the lab by typing [exit]")
    while True:
        current_user_monsters = []
        no = 1
        for i in range(len(inv_monster_data)):
            if inv_monster_data[i]["user_id"] == user_id:
                monster_index = index(monster_data,inv_monster_data[i]["monster_id"],"id")
                print(f"{no}. {monster_data[monster_index]["type"]} (level {inv_monster_data[i]["level"]})")
                current_user_monsters.append({"current_monster_id" : monster_data[monster_index]["id"]})
                current_user_monsters[no-1]["number"] = str(no)
                no += 1
        choice = input("➤ ")
        if choice.upper() == "EXIT":
            break
        elif exist(current_user_monsters,choice,"number"):
            monster_upgrade_index = index(inv_monster_data,current_user_monsters[int(choice)-1]["current_monster_id"],"monster_id")
            if int(inv_monster_data[monster_upgrade_index]["level"]) < 5:
                cost = upgrade_price[int(inv_monster_data[monster_upgrade_index]["level"])-1]
                user_money = int(users_data[index(users_data,user_id,'id')]["oc"])
                if user_money >= cost:
                    while True:
                        textbox(f"currently you have {user_money} OC. its going to cost you {cost} OC, are you sure you want to upgrade this monster?")
                        confirm = input("➤ ")
                        if confirm.upper() == "Y":
                            inv_monster_data[monster_upgrade_index]["level"] = str(int(inv_monster_data[monster_upgrade_index]["level"]) + 1)
                            users_data[index(users_data,user_id,'id')]["oc"] = str(user_money-cost)
                            textbox("Your monster has gotten stronger! El Psy Congroo!")
                            break
                        elif confirm.upper() == "N":
                            break
                else:
                    textbox(f"you only have {user_money} oc in your wallet... you need {cost} oc to upgrade that monster. just [exit] if you don't have money...")
            else: 
                textbox("it seems that your monster is at its maximum level")
        else:
            textbox("again, please type one of the [numbers] for the monster you wish to upgrade")
