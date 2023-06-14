#mencari nilai max & min

def cari_nilai(array, n):
    if n == 0 :
       return (array[0], array[0])
    
    min_max = cari_nilai(array, n-1)
    minimum = min(min_max[0], array[n-1])
    maximum = max(min_max[1], array[n-1])

    return (minimum,maximum)
arr = [1,5,7,9,14]
print("array:", arr)
print("Nilai terkecil dan terbesar:", cari_nilai(arr, len(arr)))

