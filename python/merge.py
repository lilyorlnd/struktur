def mergeSort(list_bilangan):
    jumblah_bilangan = len(list_bilangan)
    if jumblah_bilangan > 1:
        posisi_tengah = jumblah_bilangan//2
        potongan_kiri = list_bilangan[:posisi_tengah]
        potongan_kanan = list_bilangan[posisi_tengah:]
        mergeSort(potongan_kiri) #rekursif
        mergeSort(potongan_kanan)
        jumblah_bilangan_kiri = len(potongan_kiri)
        jumblah_bilangan_kanan = len(potongan_kanan)
        c_kiri,c_kanan,c_all = 0,0,0
        while c_kiri < jumblah_bilangan_kiri or c_kanan < jumblah_bilangan_kanan:
            if c_kiri == jumblah_bilangan_kiri: #potongan kiri sudah habis
                list_bilangan[c_all] = potongan_kanan[c_kanan]
                c_kanan += 1 
            elif c_kanan == jumblah_bilangan_kanan: #potongan kana habis
                list_bilangan[c_all] = potongan_kiri[c_kiri]
                c_kiri += 1
                #jika elemen kiri lwbih kecil
            elif list_bilangan[c_kiri] <= potongan_kanan[c_kanan]:
                list_bilangan[c_all] = potongan_kiri[c_kiri]
                c_kiri += 1
                #jika elemen kanan lebih kecil
            else:
                list_bilangan[c_all] = potongan_kanan[c_kanan]
                c_kanan += 1
            c_all += 1
            
list_bilangan = [1,5,7,9,4,2]
mergeSort(list_bilangan)
print(list_bilangan)

#uas : demonstrasi perkelompok,