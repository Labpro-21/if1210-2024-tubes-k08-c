def help(status):
    if status == "non-agent":
        print("""
=========== HELP ===========
Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

1. Login
2. Register

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid

""")
        input_help = input()
        # fungsi selanjutnya
    
    elif status == "agent":
        print("""
=========== HELP ===========

Halo Agent Purry. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:

1. Logout
2. Monster: Melihat owca-dex yang dimiliki oleh Agent
# ...dan seterusnya

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid
        
""")
        input_help = input()
        # fungsi selanjutnya
    
    elif status == "admin":
        print("""
=========== HELP ===========

Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:

1. Logout: Keluar dari akun yang sedang digunakan
2. Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent
# ...dan seterusnya

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid
""")
        input_help = input()
        # fungsi selanjutnya