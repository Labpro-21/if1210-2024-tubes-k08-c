# Kamus
def isFind(x,array,key): #output tuple(bool,integer) -> (ada atau tidak,index jika ada jika tidak -9999 )
    cond = False
    index = -9999
    for i in range(len(array)):
        if x == array[i][key]:
            cond=True
            index = i
    return (cond,index)

# Algoritma Utama
def login(listUser):
    # List of dictionary -> [{'id':1,'username':aaaa,'password':bbbbbb,'role':agen,'oc':0}]
    # listUser : list of tuple -> [('id',[1,2,3,...]),('username',[...]),('password',[....]),('role',[...]),('oc',[...])]
    user = input("Username: ")
    pw = input("Password: ")

    id = -9999
    isLogin = False
    index= isFind(pw,listUser,'password')[1]

    if isFind(user,listUser,'username')[0]:
        if isFind(pw,listUser,'password')[0]:
            print("""
Selamat datang, Agent Purry!
Masukkan command “help” untuk daftar command yang dapat kamu panggil.""")
            id = listUser[index]['id']
            isLogin = True
        else:
            print("""
Password salah!""")
            
    else:
        print("""
Username tidak terdaftar!""")
    return(id,isLogin)
    # Aku gk tau id perlu apa tidak ntar kalau memang tidak perlu di fix kan nanti aja

# TESTING
# arr= [{'id': '1', 'username': 'Mr_Monogram', 'password': 'monogrammer77', 'role': 'admin'}, {'id': '2', 'username': 'Asep_Spakbor', 'password': 'asepwow123', 'role': 'agent'}, {'id': '3', 'username': 'Agen_P', 'password': 'platypus123', 'role': 'agent'}, {'id': '4', 'username': 'B4ngk1dd0ssss', 'password': 'bangkitganteng', 'role': 'agent'}, {'id': '5', 'username': 'Kenny_agen_rahasia', 'password': 'kribogeming55', 'role': 'agent'}]

# print(login(arr))