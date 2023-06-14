class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DLL:
    def __init__(self):
        self.head = None

    def insert_head(self):
        inp = int(input("Insert New Data :"))
        print("\n")
        new_node = Node(inp)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def delete_all(self):
        current = self.head
        while current:
            prev_node = current.prev
            next_node = current.next
            del current
            current = next_node
        self.head = None
        print(" All Data Deleted!")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        if self.head is None:
            print("NULL")

    def menu(self):
        choose = 'y'
        while( (choose== 'y') or (choose == 'y') ):
            print("\n")
            print("Choose Menu : ")
            print("1. Add Data")
            print("2. Delete Data")
            print("3. Show Data")
            inp = str(input("Enter the selected menu :"))

            if inp == '1':
                self.insert_head()
            elif inp == '2':
                self.delete_all()
            elif inp == '3':
                self.print_list()
            else:
                choose = 'n'

if __name__ == "__main__":
    dll = DLL()
    dll.menu()

