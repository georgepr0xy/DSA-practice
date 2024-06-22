class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data , end = " -> ")
            current= current.next
        print("None")
        
def construct_list(arr):
    linked_list = linkedlist()
    for data in arr:
        linked_list.append(data)

    return linked_list

arr = [1, 2, 3, 4, 5]
linked_list = construct_list(arr)
linked_list.print_list()
  