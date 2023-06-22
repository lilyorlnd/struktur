#linerar iteraktif
def searchIter(arr,x):
    for i in range(len(arr)):
        if x == arr[i]:
            return i
    return -1 #data not found return -1, can change the -1 to false, means the same :')
def searchRec(arr,curr_idx, x): #rekursif
    if curr_idx == -1 : #perulangan mundur
        return -1
    elif arr[curr_idx] == x:
        return curr_idx
    return searchRec(arr,curr_idx-1,x)   #kalau maju idx+1   
arr = [5,1,7,3,9,2]
x = 1
print(searchIter(arr,x))
print(searchRec(arr,len(arr)-1,x)) #kalau maju ganti -1 dengan 0
    