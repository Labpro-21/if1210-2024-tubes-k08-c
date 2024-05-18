def tabel_monster(monster_dict):
    list_len = [[2],[4],[9],[9],[2]]
    max_len = []
    for i in range(len(monster_dict)):
        list_len[0].append(len(str(monster_dict[i]["id"])))
        list_len[1].append(len(monster_dict[i]["type"]))
        list_len[2].append(len(str(monster_dict[i]["atk_power"])))
        list_len[3].append(len(str(monster_dict[i]["def_power"])))
        list_len[4].append(len(str(monster_dict[i]["hp"])))

    for i in list_len:
        max_len.append(max(i))

    print(f"ID{' '*(max_len[0] - 2)} | Type{' '*(max_len[1] - 4)} | ATK Power{' '*(max_len[2] - 9)} | DEF Power{' '*(max_len[3] - 9)} | HP{' '*(max_len[4] - 2)}" )
    for i in range(len(monster_dict)):
        print(f"{monster_dict[i]["id"]}{" "*(max_len[0] - list_len[0][i+1])} | {monster_dict[i]["type"]}{" "*(max_len[1] - list_len[1][i+1])} | {monster_dict[i]["atk_power"]}{" "*(max_len[2] - list_len[2][i+1])} | {monster_dict[i]["def_power"]}{" "*(max_len[3] - list_len[3][i+1])} | {monster_dict[i]["hp"]}{" "*(max_len[4] - list_len[4][i+1])}")
    print("\n")

def ui_monster(monster_dict):
    min_def,max_def = 0,50
    while True:
        list_name = [monster_dict[i]['type'] for i in range(len(monster_dict))]
        print("""WELCOME TO THE MONSTER DATABASE!!!
1. Display all Monsters in the database
2. Add new Monsters
3. Exit
""")
        pilihan = input("Select a command: ")
        if pilihan == "1":
            tabel_monster(monster_dict)
        elif pilihan == "2":
            id = str(int(monster_dict[len(monster_dict)-1]["id"])+1)
            while True:
                type_name = input("Enter Type / Name: ")
                if type_name not in list_name:
                    break
                else:
                    print("Name has been registered, try again!\n")
            while True:
                atk_power = input("Enter ATK Power : ")
                if atk_power.isdigit():
                    break
                else:
                    print("Enter input in the form of an Integer, try again!\n")
            while True:
                def_power = input("Enter DEF Power: ")
                if def_power.isdigit():
                    if min_def <= int(def_power) <= max_def:
                        break
                    else:
                        print(f"DEF Power must be {min_def}-{max_def}, try again!\n")
                else:
                    print("Enter input in the form of an Integer, try again!\n")
            while True:
                hp = input("Enter HP: ")
                if hp.isdigit():
                    break
                else:
                    print("Enter input in the form of an Integer, try again!\n")

            print(f"""
New monster successfully created!
Type : {type_name}
ATK Power : {atk_power}
DEF Power : {def_power}
HP : {hp}
""")
            while True:
                pilihan2 = input("Add Monster to Database (Y/N): ")
                if pilihan2 == "Y" or pilihan2 == "y":
                    monster_dict.append({'id':id,'type':type_name,'atk_power':atk_power,'def_power':def_power,'hp':hp})
                    print("Monster added successfully!\n")
                    break
                elif pilihan2 == "N" or pilihan2 == "n":
                    print("Monster failed to add!\n")
                    break
                else:
                    print("Invalid command")
        elif pilihan == "3":
            print("You are logged out of the DATABASE")
            break

        else:
            print("invalid command")