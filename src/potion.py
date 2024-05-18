def user_id_potion(potion_inventory: list[dict[int,str,str]], id: int) -> list: # fungsi untuk mengambil potion bergantung pada user_id
    list_potion = []
    for i in potion_inventory:
        if i["user_id"] == id:
            list_potion.append(i)

    return list_potion

def up_ability(monster_status: list, base_hp: int, max_hp: int, up: int) -> None:
    if up == 1:
        monster_status[0] = (monster_status[0]*105)//100
    elif up == 2:
        monster_status[1] = (monster_status[1]*105)//100
    elif up == 3:
        monster_status[2] += (base_hp*25)//100
        if monster_status[2] >= max_hp:
            monster_status[2] = max_hp

def find_index(potion_inventory: list[dict[int,str,str]], user_id: int, type_up: str) -> int:
    index = 0
    for i in potion_inventory:
        if i['user_id'] == user_id and i['type'] == type_up:
            return index
        index += 1

def ui_potion(potion_inventory: list[dict[int,str,str]], monster_name: str, monster_status: list, base_hp: int, max_hp: int, id: int, num_potion: list) -> None:
    while True:
        user_potion = user_id_potion(potion_inventory,id)
        dict_potion = {'strength' : 0,
                    'resilience' : 0,
                    'healing' : 0}
        
        for i in user_potion:
            dict_potion[i['type']] = int(i['quantity'])

        print(f"""
============ POTION LIST ============
1. Strength Potion (Qty: {dict_potion['strength']}) - Increases ATK Power
2. Resilience Potion (Qty: {dict_potion['resilience']}) - Increases DEF Power
3. Healing Potion (Qty: {dict_potion['healing']}) - Restores Health
4. Cancel
""")
        pilihan_3 = input("Select a command: ")
        if pilihan_3 == '1':
            if dict_potion['strength'] == 0:
                print("Wah, you don't have this potion, please choose another potion!")
            elif num_potion[0] >= 1:
                print(f"You try to give this potion to {monster_name}, but the monster refuses it as if monster understands the potion is no longer useful.")
            else:
                num_potion[0] += 1
                up_ability(monster_status,base_hp,max_hp,int(pilihan_3))
                potion_inventory[find_index(potion_inventory,id,'strength')]['quantity'] = str(int(potion_inventory[find_index(potion_inventory,id,'strength')]['quantity']) - 1)
                print(f"After drinking this potion, an aura of power is seen surrounding {monster_name} and its movements become faster and more deadly.")
                aktivate = True
                return aktivate

        elif pilihan_3 == '2':
            if dict_potion['resilience'] == 0:
                print("Wah, you don't have this potion, please choose another potion!")
            elif num_potion[1] >= 1:
                print(f"You try to give this potion to {monster_name}, but the monster refuses it as if monster understands the potion is no longer useful.")
            else:
                num_potion[1] += 1
                up_ability(monster_status,base_hp,max_hp,int(pilihan_3))
                potion_inventory[find_index(potion_inventory,id,'resilience')]['quantity'] = str(int(potion_inventory[find_index(potion_inventory,id,'resilience')]['quantity']) - 1)
                print(f"After drinking this potion, a protective energy appears around {monster_name} which makes it look tougher and harder to hurt.")
                aktivate = True
                return aktivate

        elif pilihan_3 == '3':
            if dict_potion['healing'] == 0:
                print("Wah, you don't have this potion, please choose another potion!")
            elif num_potion[2] >= 1:
                print(f"You try to give this potion to {monster_name}, but the monster refuses it as if monster understands the potion is no longer useful.")
            else:
                num_potion[2] += 1
                up_ability(monster_status,base_hp,max_hp,int(pilihan_3))
                potion_inventory[find_index(potion_inventory,id,'healing')]['quantity'] = str(int(potion_inventory[find_index(potion_inventory,id,'healing')]['quantity']) - 1)
                print(f"After drinking this potion, the wounds in {monster_name}'s body healed quickly. In an instant, {monster_name} looked fit again and ready to continue fighting.")
                aktivate = True
                return aktivate

        elif pilihan_3 == '4':
            aktivate = False
            return aktivate

        else:
            print("The command is not in the options")