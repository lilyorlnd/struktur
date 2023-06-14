#Buatlah program dengan fungsi rekursif yang menampilkan “10 9 8 7 6 5 4 3 2 1 0”!

def count_down(n): #count down:hitung mundur dengan 'n' sebgai angka awal
    if n >= 0:
        print(n, end=' ')
        count_down(n - 1)

count_down(10)

