#Stack 

class Stack:
    def __init__(self):
        self.num_node = 0

    def push(self, node):
        if (self.num_node == 0):
            self.node = node
        else:
            self.new_node = node
            self.prev_node = self.node

            self.new_node.set_next(self.node)
            self.prev_node.set_prev(node)

            self.node = self.new_node
        self.num_node += 1

    def pop(self):
        if (self.num_node != 0):
            self.temp_node = self.node.get_next()
            self.temp_node.set_prev(None)
            self.node = self.temp_node
            self.num_node -= 1

    def peek(self):
        return self.node.get_value()

 class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self,next):
        self.next = next

    def set_prev(self,prev):
         self.prev = prev

    def get_value(self):
        return self.value

node1 = Node(2)
node2 = Node(25)
node3 = Node(6)
node4 = Node(19)
stack = Stack()
stack.push(node1)
stack.push(node2)
stack.push(node3)
stack.push(node4)
stack.pop()
stack.peek()
