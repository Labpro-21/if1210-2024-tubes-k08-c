def isnumeric(kata:str) -> bool:
    cond = True
    for i in range(len(kata)):
        if not(kata[i] == "1" or kata[i] == "2" or kata[i] == "3" or kata[i] == "4" or kata[i] == "5" or kata[i] == "6" or kata[i] == "7" or kata[i] == "8" or kata[i] == "9" or kata[i] == "0"):
            cond = False
            break
    return cond

def ext_dict(data: dict, keys_other: list[str]) -> dict:
    row_dict = {}
    for j in keys_other:
        row_dict[j] = data[j]
    return row_dict


def oc(user_id: int, user: list[dict]) -> int:
    oc = 0
    for i in range(len(user)):
        if int(user[i]['id']) == user_id:
            oc = user[i]['oc']
            break
    return oc


def item_inv(user_id: int, item_inventory: list[dict]) -> list[dict]:
    item = []
    for i in range(len(item_inventory)):
        if int(item_inventory[i]['user_id']) == user_id:
            item.append(ext_dict(item_inventory[i], ['type', 'quantity']))
    return item


def monster_inv(user_id: int, monster_inventory: list[dict], monster: list[dict]) -> list[
    dict]:  # memperoleh monster yang dipunyai user
    monster_id = []
    monster_level = []
    for i in range(len(monster_inventory)):
        if user_id == int(monster_inventory[i]['user_id']):
            monster_id.append(int(monster_inventory[i]['monster_id']))
            monster_level.append(int(monster_inventory[i]['level']))
    if len(monster_id) > 0:
        inv_monster = []
        for i in range(len(monster_id)):
            for j in range(len(monster)):
                if monster_id[i] == int(monster[j]['id']):
                    inv_monster.append(ext_dict(monster[j], ['type', 'atk_power', 'def_power', 'hp']))
        for i in range(len(monster_level)):
            inv_monster[i]['level'] = monster_level[i]
    else:
        inv_monster = []
    return inv_monster


def ui_main_inventory(user_id: int, oc: int, item: list[dict], monster: list[dict]):
    print(f"""
============ INVENTORY LIST (User ID: {user_id}) ============
Jumlah O.W.C.A. Coin-mu sekarang {oc}.""")
    if len(item) + len(monster) > 0:
        number = 0
        for i in range(len(monster)):
            number += 1
            print(
                f"{number}. Monster       (Name: {monster[i]['type']}, Lvl: {monster[i]['level']}, HP: {monster[i]['hp']})")
        for i in range(len(item)):
            number += 1
            print(f"{number}. Potion        (Type: {item[i]['type']}, Qty: {item[i]['quantity']})")
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Tidak ada barang di Inventory kamu. (┬┬﹏┬┬)")
    print()


def ui_monster_inventory(monster: dict):
    print(f"""
Monster
Name      : {monster['type']}
ATK Power : {monster['atk_power']}
DEF Power : {monster['def_power']}
HP        : {monster['hp']}
Level     : {monster['level']} 
""")


def ui_item_inventory(item: dict):
    print(f"""
Potion
Type      : {item['type']}
Quantity  : {item['quantity']} 
""")


def inventory(user_id: int, user: list[dict], item_inventory: list[dict], monster_inventory: list[dict],
              monster: list[dict]):
    user_oc = oc(user_id, user)
    user_item = item_inv(user_id, item_inventory)
    user_monster = monster_inv(user_id, monster_inventory, monster)
    ui_main_inventory(user_id, user_oc, user_item, user_monster)
    if len(user_item)+len(user_monster) == 0:
            return {'oc': user_oc, 'potion': user_item, 'monster': user_monster}
    else:
        while True:
            print("""Ketikkan id untuk menampilkan detail item:
(99:KELUAR, 0:INVENTORY)""")
            id_input = (input(">>> "))
            if isnumeric(id_input):
                id_input = int(id_input)
                if int(id_input) == 99:
                    print()
                    break
                elif int(id_input) == 0:
                    ui_main_inventory(user_id, user_oc, user_item, user_monster)
                elif int(id_input) > len(user_monster) + len(user_item) or int(id_input) <= 0:
                    print("Maaf id yang dimasukkan tidak ada dipilihan.")
                elif int(id_input) > len(user_monster):
                    ui_item_inventory(user_item[(int(id_input) - len(user_monster)) - 1])
                else:
                    ui_monster_inventory(user_monster[int(id_input) - 1])
            else:
                print("""Maaf input yang anda masukkan tidak sesuai !!
                    
Ketikkan id untuk menampilkan detail item:
(99:KELUAR, 0:INVENTORY)""")
                id_input = (input(">>> "))
    return {'oc': user_oc, 'potion': user_item, 'monster': user_monster}

# print(inventory(3,user_data,inv_item_data,inv_monster_data,monster_data))
# print(isnumeric("0"))