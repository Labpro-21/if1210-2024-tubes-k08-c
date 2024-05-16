from login import is_find


def is_valid_username(username):  # check the validity of characters in username
    validif = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-"
    for char in username:
        if char not in validif:
            return False
    return True


def choose_monster(user_id: int, username: str, monster_data: list[dict], inv_monster_data: list[dict]):  # choose monster
    print(" Choose your first monster!")
    for row in monster_data:
        print(f"{row['id']}. {row['type']}")
    while True:
        monster_choice = input("Enter entry number: ")
        if monster_choice.isnumeric():
            monster_choice = int(monster_choice)
            if 0 < monster_choice < len(monster_data)+1:
                break
            else:
                print("Enter a valid number")
        else:
            print("Enter a valid number")

    inv_monster_data.append({'id': user_id, 'monster_id': monster_choice, 'level': 1})
    print(f"Welcome Agent {username}. Let's beat Dr. Asep Spakbor with {monster_data[monster_choice-1]['type']}!")
    return inv_monster_data


# MAIN PROGRAM
def register_ui(user_data: list[dict], monster_data: list[dict], inv_monster_data: list[dict]):
    print("Register as a new user !!!")
    # input username and password
    while True:
        username = str(input("Enter username: "))
        if not is_valid_username(username):  # invalid characters used in username
            print("Username must only contain letters, numbers, underscores, and dashes.")
        # username is valid
        else:
            if not is_find(username, user_data, 'username')[0]:  # username entered is a new user
                password = str(input("Enter password: "))
                user_id = len(user_data)+1
                new_user = {'id': user_id, 'username': username, 'password': password, 'role': 'agent', 'oc': 0}
                user_data.append(new_user)
                new_inv_monster = choose_monster(user_id, username, monster_data, inv_monster_data)
                return user_id, True, new_inv_monster
            else:  # username has been taken
                print(f"Username {username} has already been taken.")
                while True:
                    login_move = input("Do you want to login instead? Y/N : ").upper()
                    if login_move == "Y":
                        return -999, False, inv_monster_data
                    elif login_move == "N":
                        break
                    else:
                        print("Enter a valid option")
