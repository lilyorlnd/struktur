class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def show(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            curr = self.head
            while curr:
                print(curr.data, end=" ")
                curr = curr.next
            print()

    def delete(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr is None:
            return
        prev.next = curr.next

    def insertionSort(self):
        if self.head is None:
            return
        sorted_list = None
        curr = self.head
        while curr:
            next_node = curr.next
            sorted_list = self.sortedInsert(sorted_list, curr)
            curr = next_node
        self.head = sorted_list

    def sortedInsert(self, sorted_list, new_node):
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node
        curr = sorted_list
        while curr.next and curr.next.data < new_node.data:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        return sorted_list

    def menu(self):
        while True:
            print("Pilih menu : ")
            print("1. Add Data")
            print("2. Show Data ")
            print("3. Delete Data")
            print("4. Sorting Linked List")
            print("5. Exit")
            pilihan = input("Masukkan pilihan : ")

            if pilihan == "1":
                data = int(input("Masukkan data: "))
                self.add(data)
            elif pilihan == "2":
                self.show()
            elif pilihan == "3":
                data = int(input("Masukkan data yang ingin dihapus : "))
                self.delete(data)
                print("Data berhasil dihapus!")
            elif pilihan == "4":
                self.insertionSort()
                print("Linked List telah diurutkan.")
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

            print()

if __name__ == '__main__':
    sl = LinkedList()
    sl.menu()