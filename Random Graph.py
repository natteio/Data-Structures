# Random Graph

import random

class Vertex:

    def __init__(self):
        self.__value = None
        self.__neighbors = []
        self.noDegree = 0 # no. connections
        self.trav = False

    def setValue(self,value):
        self.__value = value

    def setNeighbors(self, neighbor):
        self.__neighbors.append(neighbor)

        self.noDegree += 1

    def getValue(self):
        return self.__value

    def getNeighbors(self):
        return self.__neighbors

    def getDegree(self):
        return self.noDegree-1

    def isTraverse(self):
        return self.trav
class Graph:

    def __init__(self):
        self.__vertexes = []


    def connectMe(self, vertex, connectMeTo):
        # connection
        # EVALUATE
        counter = 0
        for i in vertex.getNeighbors():
            if i.getValue() == connectMeTo.getValue():
                counter += 1

        if counter == 0:
            vertex.setNeighbors(connectMeTo)
            connectMeTo.setNeighbors(vertex)
        pass

    def getAllVertexes(self):
        return self.__vertexes

    def addVertex(self,value):
        vertex = Vertex()
        vertex.setValue(value)
        self.__vertexes.append(vertex)
        return vertex

    def printVertexes(self):
        for i in self.__vertexes:
            print('Vertex: \n\tval: {}'.format(i.getValue()))
            print('Neighbor:')
            for z in i.getNeighbors():
                print('\t{}'.format(z.getValue()))

    def selectTraverse(self, value):
        for i in self.getAllVertexes(): # starting point
            if i.getValue() == value:
                vertex = i
                break
        self.Traverse(vertex, vertex.getNeighbors())

    def Traverse(self, vertex, neighbor):
            if not vertex.isTraverse():
                print(vertex.getValue())
                vertex.trav = True
            for i in neighbor:
                if not i.isTraverse():
                    self.Traverse(i,i.getNeighbors())


class RandomGraph:

    def __init__(self):
        self.__graph = Graph()
        self.__setValues = [5,10,15,20,30,11,100,31,52,62,18,18,29,45,32,51,82]

    def pickVertex(self):
        # pick randomly values
        while self.__setValues:
            No = random.choice(self.__setValues) # random value

            vertex = self.__graph.addVertex(No) # add vertex
            self.connectMeRandomly(vertex) # established connection

            self.__setValues.remove(No) # remove
            print(self.__setValues)
        self.__graph.printVertexes()
        pass

    def Traverse(self, value):
        print('Traverse')
        self.__graph.selectTraverse(value)

    def connectMeRandomly(self, vertex):
        # randoming thingy
        if len(self.__graph.getAllVertexes()) > 1:
            noDegree = random.randint(1,len(self.__graph.getAllVertexes())) # get no. of degrees will be connected
            while noDegree > 0:
                conMeToThisVertex = random.choice(self.__graph.getAllVertexes()) # pick random vertex in the graph
                # evaluate
                if not (conMeToThisVertex.getValue() == vertex.getValue()) and len(self.__graph.getAllVertexes()) > 2:
                    self.__graph.connectMe(vertex, conMeToThisVertex)
                    noDegree -= 1
                elif not (conMeToThisVertex.getValue() == vertex.getValue()):
                    self.__graph.connectMe(vertex, conMeToThisVertex)
                    break
        pass

    # traversal: BSF


x = RandomGraph()
x.pickVertex()
x.Traverse(15)
