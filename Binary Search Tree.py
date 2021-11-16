# Binary Search Tree

import random


class Node:
    def __init__(self):
        self.__value = None
        self.__right = None
        self.__left = None

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def setRight(self,nod):
        self.__right = nod

    def setLeft(self,nod):
        self.__left = nod

    def getValue(self):
        return self.__value

    def setValue(self,value):
        self.__value = value

class Tree:
    def __init__(self):
        self.__root = None

    def insert(self,value):
        # to-do insertion
        nod = Node()
        nod.setValue(value)
        if self.__root is None:
            self.__root = nod
        else:
            # do left-right
            self.__insert(self.__root,nod)
        pass

    def __insert(self,root,nod):
        if root.getValue() < nod.getValue():
            # right
            if root.getRight() is None:
                root.setRight(nod)
            else:
                self.__insert(root.getRight(),nod)
        else:
            # left
            if root.getLeft() is None:
                root.setLeft(nod)
            else:
                self.__insert(root.getLeft(),nod)
        pass

    def delete(self,value):
        # to-do deletion
        if self.searchNode(value) is not None:
            self.__delete(self.__root,value)
        else:
            return print('No Node containing value: {}'.format(value))
        pass

    def __delete(self,root,value):
            if root.getValue() <= value: # right or equal

                if root.getValue() == value:

                    if root.getRight() is not None:
                        rtrvMinNode = self.__getMinNode(root.getRight()) # get minimum node from the right

                        rootNode = self.getRootNode(root.getValue()) # get root of the root
                        # connecting the right branch of minNode to it's rootNode branch
                        rootMinNode = self.getRootNode(rtrvMinNode.getValue())

                        if rtrvMinNode.getRight() is not None and rtrvMinNode.getRight().getValue() >= rootMinNode.getValue():
                            rootMinNode.setRight(rtrvMinNode.getRight())
                        else:
                            rootMinNode.setLeft(rtrvMinNode.getRight())

                        rtrvMinNode.setRight(root.getRight() if root.getRight() is not rtrvMinNode else None)
                        rtrvMinNode.setLeft(root.getLeft() if root.getLeft() is not rtrvMinNode else None)

                        if not (rootNode.getValue() == self.__root.getValue()):
                            rootNode.setRight(rtrvMinNode)
                        else:
                            self.__root = rtrvMinNode


                    else:
                        # leaf
                        rootNode = self.getRootNode(root.getValue())
                        rootNode.setRight(root.getLeft())
                        root = None

                else:
                    return self.__delete(root.getRight(), value)
            else:
                if root.getLeft().getValue() == value:

                    if root.getLeft().getRight() is not None:

                        rtrvMinNode = self.__getMinNode(root.getLeft().getRight()) # get MinNode from the right
                        rootNode = self.getRootNode(rtrvMinNode.getValue()) # get root node of minNode

                        if rtrvMinNode.getRight() is not None:
                            rootNode.setLeft(rtrvMinNode.getRight())
                        else:
                            rootNode.setLeft(None)
                        rtrvMinNode.setLeft(root.getLeft().getLeft() if root.getLeft().getLeft() is not rtrvMinNode else None)
                        rtrvMinNode.setRight(root.getLeft().getRight() if root.getLeft().getRight() is not rtrvMinNode else None)
                        root.setLeft(rtrvMinNode)

                    else:
                        root.setLeft(root.getLeft().getLeft())

                else:
                    return self.__delete(root.getLeft(), value)

    def searchNode(self, value):
        node = self.__searchNode(self.__root, value)
        if node is not None:
            return node
        else:
            return None

    def getRootNode(self, value):
        return self.__getRootNode(self.__root, value)

    def __searchNode(self,root, value): # return node
        if root is not None:
            if root.getValue() <= value:
                if root.getValue() == value:
                    return root
                else:
                    return self.__searchNode(root.getRight(),value)
            else:
                if root.getLeft().getValue() == value:
                    return root.getLeft()
                else:
                    return self.__searchNode(root.getLeft(),value)
        else:
            return None

    def __getRootNode(self,root, value): # return root of the node
        if root.getValue() <= value :
            if root.getValue() == value:
                return root
            elif (root.getRight() is not None and root.getRight().getValue() == value):
                return root
            else:
                return self.__getRootNode(root.getRight(),value)
        else:
            if (root.getLeft() is not None and root.getLeft().getValue() == value):
                return root
            else:
                return self.__getRootNode(root.getLeft(),value)


    def __getMinNode(self,root):
        # getting lowest value from the right
        if root.getLeft() is not None:
            return self.__getMinNode(root.getLeft())
        else:
            return root

    def __inOrderRecur(self,root):
        if root is not None:
            self.__inOrderRecur(root.getLeft())
            print(root.getValue(), end = " ")
            self.__inOrderRecur(root.getRight())

    def inOrder(self):
        self.__inOrderRecur(self.__root)
        print()


    def getRoot(self):
        return self.__root

    def prntTree(self):
        pass

def getNodeDetail(value,tree):
    print('Node \n\tValue: {} '.format(tree.searchNode(value).getValue()))
    if t.searchNode(value).getLeft() is not None:
        print('\tL: ',tree.searchNode(value).getLeft().getValue())
    if t.searchNode(value).getRight() is not None:
        print('\tR: ',tree.searchNode(value).getRight().getValue())

def delete(delValue,tree):
    rootVal = tree.getRootNode(delValue).getValue()
    if delValue == tree.getRoot().getValue():
        root = True
    print('Deleted',end = " ")
    getNodeDetail(rootVal,tree)
    tree.delete(delValue)
    print('New',end = " ")
    getNodeDetail(tree.getRoot().getValue() if root else rootVal,tree)

t = Tree()
t.insert(10)
t.insert(5)
t.insert(20)
t.insert(3)
t.insert(1)
t.insert(25)
t.insert(15)
t.insert(18)
t.insert(4)
t.insert(8)
t.insert(7)
t.insert(9)
t.insert(12)
t.insert(14)
t.insert(16)
t.insert(19)
t.insert(17)
t.insert(28)
#t.insert(27)
#t.insert(26)
#print(t.getRoot().getValue())
t.inOrder()

delete(10,t)

t.inOrder()
