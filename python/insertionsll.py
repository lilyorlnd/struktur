class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_data(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_data(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current is not None and current.data != data:
                prev = current
                current = current.next

            if current is None:
                return

            prev.next = current.next

    def show_data(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()

    def sort_data(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head

        while current is not None:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node

        current = sorted_list
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_list


# Fungsi untuk menampilkan menu dan menerima input dari pengguna
def show_menu():
    print("1. Add Data")
    print("2. Delete Data")
    print("3. Show Data")
    print("4. Sort Data")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

# Membuat objek linked list
linked_list = LinkedList()

while True:
    choice = show_menu()

    if choice == 1:
        data = int(input("Enter the data: "))
        linked_list.add_data(data)
    elif choice == 2:
        data = int(input("Enter the data to delete: "))
        linked_list.delete_data(data)
    elif choice == 3:
        linked_list.show_data()
    elif choice == 4:
        linked_list.sort_data()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")

