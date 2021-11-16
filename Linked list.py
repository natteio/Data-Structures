# Linked List

class Node:
    def __init__(self, value):
        self.item = value
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def peek(self):
        if self.head is None:
            print("Linked List is Empty")
        n = self.head
        while n is not None:
            print(n.item, " ")
            n = n.ref

    def push(self, value):
        node1 = Node(value)
        node1.ref = self.head
        self.head = node1

    def pop_head(self):
        if self.head is not None:
            self.head = self.head.ref
        else:
            print("Nothing to delete")

    def pop_tail(self):
        if self.head is None:
            print("Nothing to delete")
            return
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def pop_body(self, x):
        if self.head is None:
            print("Nothing to delete")
            return
        if self.head.item == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("Error: number is not in Linked List")
        else:
            n.ref = n.ref.ref

    def search(self, x):
        n = self.head
        while n is not None:
            if n.item == x:
                print("Item Found")
                return
            n = n.ref
        print("Item not found")
        return

ll = LinkedList()
ll.push(5)
ll.push(10)
ll.push(15)
ll.push(5)
ll.push(10)
ll.push(15)
ll.push(5)
ll.push(10)
ll.push(15)
ll.pop_tail()
ll.peek()
