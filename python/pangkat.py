def pangkat(x, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return x * pangkat(x, n-1)

# Contoh penggunaan
x = 4
n = 2
hasil = pangkat(x, n)
print(f"{x} pangkat {n} adalah {hasil}")
