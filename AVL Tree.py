# AVL Tree

class Node:
    def __init__(self):
        self.V = None
        self.L = None
        self.R = None

    def getR(self):
        return self.R

    def getL(self):
        return self.L

    def setR(self,nod):
        self.R = nod

    def setL(self,nod):
        self.L = nod

    def getV(self):
        return self.value

    def setV(self,value):
        self.V = value

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        nod = Node()
        nod.setV(value)
        if self.root is None:
            self.__root = nod
        else:
            self.__insert(self.root(),nod)
        pass

    def __insert(self,root,nod):
        if root.getV() < nod.getV():
            if root.getR is None:
                root.setR(nod)
            else:
                self.__insert(root.getR(),nod)
        else:
            if root.getL is None:
                root.setL(nod)
            else:
                self.__insert(root.getL(),nod)
        root.height = 1 + max(self.getHeight(root.L),self.getHeight(root.R))

        balance = self.B(root)

        if balance > 1 and nod < root.L.V:
            return self.RRotate(root)
        if balance < -1 and nod > root.R.V:
            return self.LRotate(root)
        if balance > 1 and nod > root.L.V:
            root.L = self.LRotate(root.L)
            return self.RRotate(root)
        if balance < -1 and nod < root.R.V:
            root.R = self.RRotate(root.R)
            return self.LRotate(root)

    def LRotate(self, z):
        y = z.R
        T2 = y.L

        y.L = z
        z.R = T2

        z.height = 1 + max(self.getHeight(z.L), self.getHeight(z.R))
        y.height = 1+ max(self.getHeight(z.L), self.getHeight(z.R))
        return y

    def RRotate(self, z):
        y = z.L
        T3 = y.R

        y.R = z
        z.L = T3

        z.height = 1 + max(self.getHeight(z.L), self.getHeight(z.R))
        y.height = 1+ max(self.getHeight(z.L), self.getHeight(z.R))
        return y

    def getHeight(self,root):
        if not root:
            return 0
        return root.height

    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.L)-self.getHeight(root.R)

    def preOrder(self,root):
        if not root:
            return
        print("{0}".format(root.V), end="")
        self.preOrder(root.L)
        self.preOrder(root.R)
