def insertionSort(angka):
    for i in range(1,len(angka)):
        key = angka[i]
        j = i-1
        print(key, " < ", angka[j])
        while j >= 0 and key < angka[j]:
            angka[j+1] = angka[j]
            angka[j] = key
            j -= 1
            print("tukar")
            print("Output :", angka, "\n")

angka = [5,1,3,2,4]
# angka = ['B', 'A', 'C', 'D']
insertionSort(angka)