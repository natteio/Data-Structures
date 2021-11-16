# Queue

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.num_node = 0

    def enqwe(self,value):
        node = Node(value)
        if (self.num_node == 0):
            self.first = node
            self.last = node
            self.num_node += 1
        else:
            node.set_nxt(self.last)
            self.last.set_prev(node)
            self.last = node
            self.num_node +=1

    def deqwe(self):
        if (self.num_node != 0):
            self.temp_node = self.first.get_prev()
            self.first = self.temp_node

    def tail(self):
        return self.last.get_value()

    def head(self):
        return self.first.get_value()

 class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None
        self.prev = None

    def get_nxt(self):
        return self.nxt

    def get_prev(self):
        return self.prev

    def set_nxt(self,nxt):
        self.nxt = nxt

    def set_prev(self, prev):
        self.prev = prev

    def get_value(self):
        return self.value

node1 = Node(2)
node2 = Node(25)
node3 = Node(6)
node4 = Node(19)
qwe = Queue()
qwe.enqwe(node1)
qwe.enqwe(node2)
qwe.enqwe(node3)
qwe.enqwe(node4)
qwe.deqwe()
qwe.head()
