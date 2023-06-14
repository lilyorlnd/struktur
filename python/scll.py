class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SCLL:
    def __init__(self):
        self.head = None
    def add_data(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next = self.head
        if self.head is not None :
            while (current.next != self.head):
                current = current.next
            current.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
    def print(self):
        current = self.head
        if self.head is not None :
            while(True):
                print("Data : "+str(current.data)+" Next : "+str(current.next.data))
                current = current.next
                if current == self.head:
                    break
                
list = SCLL()
list.add_data(1)
list.add_data(2)
list.add_data(3)
list.print()