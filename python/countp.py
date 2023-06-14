#hitung pangkat dengan program rekursif

def pangkat(x,y):
   if y == 0:
      return 1
   else:
      return x * pangkat(x,y-1)

bil = int(input("Masukan Nilai  : "))
n = int(input("Masukan Nilai pangkat : "))

print("%d dipangkatkan %d = %d" % (bil,n,pangkat(bil,n)))