def searchIter(arr, x):
    awal = 0
    tengah = 0
    akhir = len(arr)-1
    while awal <= akhir:
        tengah = (awal+akhir)//2
        if arr[tengah] <x:
            awal = tengah+1
        elif arr[tengah] > x:
            akhir = tengah-1
        else:
            return tengah
    return -1 #iter end disini next rekursif same as linear

def searchRec(arr,awal,akhir,x):
    if akhir >= awal:
        tengah = (awal+akhir)//2
        if arr[tengah] == x:
            return tengah
        elif arr[tengah] >x:
            return searchRec(arr,awal, tengah-1,x)
        else:
            return searchRec(arr,tengah+1,akhir,x)
    else:
        return -1 #if not found
arr = [2,4,5,7,9,11] #di binary data harus sudah terurut, sorting 1st then binary
x = 9

print("Iter search index - ", end="")
print(searchIter(arr,x))
print("Rekursif search index -", end="")
print(searchRec(arr,0,len(arr)-1,x))
