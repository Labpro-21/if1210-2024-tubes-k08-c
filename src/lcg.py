seed_list = [0] # Lakukan pengambilan data dari save_load

# Fungsi Linear Congruential Generator
def lcg(modulus,a,c,seed):
    seed = (a * seed + c) % modulus
    seed_list.append(seed)
    # Menyimpan seed_list pada save_load
    return seed

# Fungsi nilai random berdasarkan jumlah digit
def random_n(n): # n merupakan jumlah digit
    hasil = ""
    for i in range(n):
        seed = lcg(2**64, 6364136223846793005, 1442695040888963407, seed_list[len(seed_list)-1])
        string_seed = str(seed)
        hasil += string_seed[len(string_seed)//2]

    return int(hasil)

# Fungsi random berdasarkan bilangan antara n1 dan n2
def randint1(n1,n2):
    digit = len(str(n2))
    while True:
        hasil = random_n(digit)
        if n1 <= hasil <= n2:
            return hasil