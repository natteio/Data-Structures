# Threaded Queue

import threading as T
import time
import random

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.num_node = 0

    def enqwe(self, data):
        node = Node(data)
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

class Server:
    def __init__(self):
        self.qwe = Queue()

    def getQwe(self):
        return self.qwe

    def Rmvdata(self):
        while True:
            self.qwe.deqwe()
            print('Head: ',self.qwe.head())
            time.sleep(2)

class Client:
    def __init__(self, server, NumClient, t):
        self.s = server
        self.n = NumClient
        self.t = t

    def addData(self):
        while True:
            d = random.randint(0,15)
            if self.n == 3:
                chance = random.randint(0, 100)
                if (chance > 25):
                    self.s.getQwe().enqwe(d)
                    print('Client #{} data in : {}'.format(self.n,d))
                else:
                    print("Fail")
            else:
                self.s.getQwe().enqwe(d)
                print('Client #{} data in : {}'.format(self.n,d))
            time.sleep(self.t)

s = Server()
c1 = Client(s, 1, 3)
c2 = Client(s, 2, 2)
c3 = Client(s, 3, 1)

t1 = T.Thread(target=c1.addData, args=())
t2 = T.Thread(target=c2.addData, args=())
t3 = T.Thread(target=c3.addData, args=())
s1 = T.Thread(target=s.Rmvdata, args=())

t1.start()
t2.start()
t3.start()
s1.start()

t1.join()
t2.join()
t3.join()
s1.join()
