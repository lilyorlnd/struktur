#hash function =k % m= 
#cal/callusion = m % k
#h = index k = nilai m = ukuran

hash_table = [None] * 10 #buat array len 10
def hash_func(value) : #
    return value % len (hash_table)

#method insert
def insert(hash_table,value):
    hash_key = hash_func(value)
    hash_table[hash_key] = value #simpan di hash table
    
def search(value):
    return hash_func(value)

insert(hash_table,5)
insert(hash_table,17)
insert(hash_table,13)
insert(hash_table,21)
#insert(hash_table,15) #INI MASUK CALLLUSION JADI CARI YES :)
print(hash_table) #hasil none diprint = data kosong di array yang len nya 10
print(search(5)) 

#5 % 10 = 5 (masuk ke idex 5)
#17 % 10 = 7
#13 % 10 = 3
#21 % 10 = 1


#tugas : buat if kondisin jika array terisi buat linear probbing/ rumus terbalik ex #insert(hash_table,15) dibagian insert dan search
#cuz if search #5 % 10 = 5 (masuk ke idex 5) harusnya 15 as i note it, so i have to do the callusion with the formula i wrote up there


