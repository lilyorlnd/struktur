import queue
class myQueue:
    def __init__(self):
        self.item = queue.Queue()
    def isEmpty(self):
        return self.item.empty()
    def qPut(self,data):
        self.item.put(data)
    def qGet(self):
        if not self.item.empty():
            return self.item.get()
        else:
            return "empty"
    def size(self):
        return self.item.qsize()
    def print(self):
        return self.item.queue
    def menu(self):
        pilih = "y"
        while pilih == "y":
            print("1. Menambah Queue")
            print("2. Mengeluarkan Queue")
            print("3. Cek Queue kosong")
            print("4. Cek size")
            print("5. Cetak Queue")
            pilihan = str(input("Pilih Menu:"))
            if pilihan == "1":
                obj = str(input("Masukkan Menu:")) #first in first out
                self.qPut(obj)
                print("Data "+obj+" Sudah ditambah")
                print("\n")
            elif pilihan == "2":
                temp = self.qGet()
                if temp != "empty":
                    print("Data "+temp+" dihapus")
                    print("\n")
                else:
                    print("empty")
                    print("\n")
            elif pilihan == "3":
                print(self.isEmpty())
                print("\n")
            elif pilihan == "4":
                print("ukuran : "+str(self.size()))
                print("\n")
            elif pilihan == "5":
                print(self.print())
                print("\n")
            else:
                pilih == "n"
if __name__ == "__main__":
    q = myQueue()
    q.menu()