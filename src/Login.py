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
        # check if username exists
        user_exists, index = is_find(user, list_user, 'username')

        if user_exists:
            if list_user[index]['password'] == pw:
                print(f"""
    Welcome back, Agent {user}!
    Enter “HELP” command to show all available actions.""")
                user_id = list_user[index]['id']
                return user_id, True
            # wrong password
            else:
                print("Wrong password!")
        # user doesn't exist
        else:
            print("Username is not registered!")
            # prompt to retry/exit
            while True:
                register_move = input("Do you want to register instead? Y/N : ").upper()
                if register_move == "Y":
                    return -999, False
                elif register_move == "N":
                    break
                else:
                    print("Enter a valid option")
