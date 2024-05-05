def help(status,username):
    if status == "non-agent":
        print("""=========== HELP ===========
Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

1. LOGIN: Masuk ke akun yang sudah ada
2. REGISTER: Buat akun baru
3. EXIT: Keluar dari game
""")
        input_help = input()
        # fungsi selanjutnya
        # buat fungsi ketika input invalid
    
    elif status == "agent":
        print(f"""=========== HELP ===========

Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:

1. LOGOUT: Keluar dari akun
2. SHOP: Melakukan pembelian di toko
3. MONSTER: Melihat owca-dex yang dimiliki oleh Agent
4. LABORATORY: Melakukan upgrade monster yang dimiliki di inventory 
5. BATTLE: Melakukan pertarungan dengan musuh 
6. SAVE: Melakukan penyimpanan data
7. EXIT: Keluar dari game 
""")
        input_help = input()
        # fungsi selanjutnya
        # buat fungsi ketika input invalid
    
    elif status == "admin":
        print("""=========== HELP ===========

Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:

1. LOGOUT: Keluar dari akun yang sedang digunakan
2. SHOP: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent
3. MONSTER: Melakukan manajemen penambahan/pengurangan monster
4. SAVE: Melakukan penyimpanan data
5. EXIT: Keluar dari game
""")
        input_help = input()
        # fungsi selanjutnya
        # buat fungsi ketika input invalid

help("agent")