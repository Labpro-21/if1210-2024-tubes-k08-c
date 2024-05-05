def logout(isLogin: bool):
    if isLogin:
        print() #line kosong
    else:
        print("""Logout gagal!
Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout""")    
    # user : (id,islogin)
    # default sebelum login -> (-9999,False)
    return(-9999,False) 
    # Baik sudah login atau pun tidak bakal balik ke default awal

# TESTING
# user1 = (3,True)
# user2 = (-9999,False)

# print(logout(user1[1]))
# print(logout(user2[1]))