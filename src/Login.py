# Kamus

# search function
def is_find(searched: str, user_array: list[dict], key: str) -> (bool, int):
    # output tuple(bool,integer) -> (ada atau tidak,index jika ada jika tidak -9999 )
    cond = False
    index = -9999
    for i in range(len(user_array)):
        if searched == user_array[i][key]:
            cond = True
            index = i
    return cond, index


# Algoritma Utama
def login(list_user: list[dict]):
    # List of dictionary -> [{'id':1,'username':aaaa,'password':bbbbbb,'role':agen,'oc':0}]
    # listUser : list of tuple -> [('id',[1,2,3,...]),
    # ('username',[...]),('password',[....]),('role',[...]),('oc',[...])]
    while True:
        print("Login into the system !!!")
        user = input("Username: ")
        pw = input("Password: ")

        user_id = -9999
        is_login = False
        user_exists, index = is_find(user, list_user, 'username')

        if user_exists:
            if list_user[index]['password'] == pw:
                print(f"""
    Welcome back, Agent {user}!
    Enter “HELP” command to show all available actions.""")
                user_id = list_user[index]['id']
                is_login = True
                return user_id, is_login
            else:
                print("Wrong password!")

        else:
            print("Username is not registered!")
            while True:
                register_move = input("Do you want to register instead? Y/N : ").upper()
                if register_move == "Y":
                    return -999, False
                elif register_move == "N":
                    break
                else:
                    print("Enter a valid option")


# TESTING
# arr= [{'id': '1', 'username': 'Mr_Monogram', 'password': 'monogrammer77', 'role': 'admin'}, {'id': '2', 'username': 'Asep_Spakbor', 'password': 'asepwow123', 'role': 'agent'}, {'id': '3', 'username': 'Agen_P', 'password': 'platypus123', 'role': 'agent'}, {'id': '4', 'username': 'B4ngk1dd0ssss', 'password': 'bangkitganteng', 'role': 'agent'}, {'id': '5', 'username': 'Kenny_agen_rahasia', 'password': 'kribogeming55', 'role': 'agent'}]

# print(login(arr))