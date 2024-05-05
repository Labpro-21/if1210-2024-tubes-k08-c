import src.load as load

users_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data = load.load_files()

def is_valid_username(username): # check the validity of characters in username
    validif = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-"
    for char in username:
        if char not in validif:
            return False
    return True

def is_new_user(username): # check if username input is a new user
    existing = ['x' for i in range(5)]
    for i in range(5):
        existing[i] = users_data[i]['username']
    if username in existing:
        return False
    return True

def choose_monster(username): # choose monster
    print("""
    Choose your first monster!
    1. Pikachow
    2. Bulba
    3. Zeze
    4. Zuko
    5. Chacha
    """)
    intchoice = int(input())
    print(f"Welcome Agent {username}. Let's beat Dr. Asep Spakbor with {monster_data[intchoice-1]['type']}!")

# MAIN PROGRAM
print(">>> REGISTER")
# input username and password
username = str(input("Enter username: "))
password = str(input("Enter password: "))

if is_new_user(username): # username entered is a new user
    if not is_valid_username(username): # invalid characters used in username
        print("Username must only contain letters, numbers, underscores, and dashes.")
    else: # username is valid
        choose_monster(username)
else: # username has been taken
    print(f"Username {username} has already been taken.")