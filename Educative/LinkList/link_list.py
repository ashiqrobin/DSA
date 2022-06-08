from operator import ne


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self, head=None):
        self.head = head


    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def print_linklist(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_after(self, pre_node, data):
        new_node = Node(data)
        if pre_node:
            new_node.next = pre_node.next
            pre_node.next = new_node
        else:
            print("No previous node")





    