def lcg(modulus: int, a: int, c: int, seed: int):
    while True:
        seed = (a * seed + c) % modulus
        yield seed

VALUE = lcg(2**128, 6364136223846793005, 1442695040888963407, 0)

def random_1(value):
    value = next(VALUE)
    return str(value)[len(str(value))//2]

def random_n(value,n):
    hasil = ""
    for i in range(n):
        hasil += random_1(value)

    return int(hasil)

def randint1(n1,n):
    digit = len(str(n))
    while True:
        hasil = random_n(VALUE, digit)
        if n1 <= hasil <= n:
            return hasil