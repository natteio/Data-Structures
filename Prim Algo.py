# Prim's Algorithm

import random

class Vertex:

    def __init__(self):
        self.__value = None
        self.__neighbors = {}
        self.noDegree = 0 # no. connections <lai pulos XD>
        self.trav = False

    def setValue(self,value):
        self.__value = value

    def setNeighbors(self, neighbor, weight):
        self.__neighbors[neighbor] = weight
        self.noDegree += 1

    def getValue(self):
        return self.__value

    def getNeighbors(self):
        return self.__neighbors

    def getDegree(self):
        return self.noDegree - 1

    def isTraverse(self):
        return self.trav

class Graph:

    def __init__(self):
        self.__vertexes = []

    def conMe(self, vertex, conMeTo, weight):
        # connection
        # EVALUATE
        counter = 0
        for i in vertex.getNeighbors():
            if i.getValue() == conMeTo.getValue():
                counter += 1

        if counter == 0:
            vertex.setNeighbors(conMeTo, weight)
            conMeTo.setNeighbors(vertex, weight)
        pass

    def getVrtxes(self):
        return self.__vertexes

    def srchVertex(self, value):
        for i in self.__vertexes:
            if i.getValue() == value:
                return i

    def addVertex(self,value):
        vertex = Vertex()
        vertex.setValue(value)
        self.__vertexes.append(vertex)
        return vertex

    def prntVrtxes(self):
        for i in self.__vertexes:
            print('-------------------------------')
            print('Vertex: \n\tval: {}'.format(i.getValue()))
            print('Neighbor:')
            for neigh in i.getNeighbors():
                print('\tval: {} weight: {}'.format(neigh.getValue(), i.getNeighbors()[neigh]))

    def slctTraverse(self, value):
        for i in self.getVrtxes(): # starting point
            if i.getValue() == value:
                vertex = i
                break
        self.Traverse(vertex, vertex.getNeighbors())

    def resetTrav(self):
        for i in self.getVrtxes():
            i.trav = False

    def Traverse(self, vertex, neighbor):
            if not vertex.isTraverse():
                print(vertex.getValue())
                vertex.trav = True
            for i in neighbor:
                if not i.isTraverse():
                    self.Traverse(i,i.getNeighbors())

    def getGraph(self):
        return self

class RandomGraph:

    def __init__(self, values):
        self.__graph = Graph()

        self.__setValues = values


        ['4f','64','6f','45','41','68','6e','79','21','59',
        '74','55','6c','69','65','76','4c','40','52','49']


    def pickVertex(self):
        # pick randomly values
        while self.__setValues:
            No = random.choice(self.__setValues) # random value

            vertex = self.__graph.addVertex(No) # add vertex
            self.connectMeRandomly(vertex) # established connection

            self.__setValues.remove(No) # remove

        #self.__graph.prntVrtxes()
        pass

    def Traverse(self, value):
        print('Traverse')
        self.__graph.slctTraverse(value)

    def connectMeRandomly(self, vertex):
        # randoming thingy
        if len(self.__graph.getVrtxes()) > 1:
            noDegree = random.randint(1,len(self.__graph.getVrtxes())) # get no. of degrees will be connected
            weight = random.randint(1,10) # generate rnd no. between 1-10
            while noDegree > 0:
                conMeToThisVertex = random.choice(self.__graph.getVrtxes()) # pick random vertex in the graph
                # evaluate
                if not (conMeToThisVertex.getValue() == vertex.getValue()) and len(self.__graph.getVrtxes()) > 2:
                    self.__graph.conMe(vertex, conMeToThisVertex,weight)
                    noDegree -= 1
                elif not (conMeToThisVertex.getValue() == vertex.getValue()):
                    self.__graph.conMe(vertex, conMeToThisVertex,weight)
                    break
        pass

    def getGraph(self):
        return self.__graph.getGraph()

class MST:

    def __init__(self, graph):
        self.__theRndGraph = graph # Random Graph
        self.__theMST = Graph() # MST Graph
        self.__edge = []
        self.__totalWeight = 0
        self.__isCycle = False
        self.debug = False # for tracing
        pass

    def cpy(self, frm, to): # dapat static ni nga func. sa graph
        for i in frm.getVrtxes():
            to.addVertex(i.getValue())
        pass

    def getEdges(self, graph):
        # return the lst of edges in a graph (no repetition & sorted)
        vertex = random.choice(graph.getVrtxes())
        self.getAllEdge(vertex, vertex.getNeighbors())
        self.__theMST.resetTrav()
        self.__edge = list(set(self.__edge))
        self.__edge.sort()

        return self.__edge
        pass

    def getAllEdge(self, vertex, neighbor):
        if not vertex.isTraverse():
            for i in neighbor:
                self.__edge.append(neighbor[i])
            vertex.trav = True
        for i in neighbor:
            if not i.isTraverse():
                self.getAllEdge(i,i.getNeighbors())

    def getGraph(self):
        return self.__theMST.getGraph()

    def prntVrtxes(self):
        return self.__theMST.prntVrtxes()

    def check(self, lst, i, n):
        for z in lst:
            if z[0] == n and z[1] == i:
                return False
        return True

    def chckCycle(self, vertex, neighbor, conTo):
        if self.debug:
            print('\t\t', vertex.getValue(), end = " -:")
            for i in neighbor:
                print(i.getValue(), end = ":")
            print()

        if not self.__isCycle:
            if not vertex.isTraverse():
                if vertex.getValue() == conTo.getValue():
                    if self.debug:
                        print('Match: ',vertex.getValue(),':', conTo.getValue())
                    self.__isCycle = True
                vertex.trav = True
            for i in neighbor:
                if not i.isTraverse():
                    self.chckCycle(i, i.getNeighbors(), conTo)
    """
    Algo:
         e traverse nmo ang vertex
         while ga traverse ka.. evaluate if kana siya nga vertex kai equal
         ba siya sa e connect nga vertex. kung dili gani kai mo padayon siyang
         traverse hantod na visit na niya tanan ang mga naka connect(neighbor) ana nga vertex
         sa MST
    """
    def kruskal(self, edge, con = []):
        if edge:
            """
            Store the vertexes which has an edge of 'edge' in 'CON'
            Neglect repetition(e.g. [(x,y), (y,x)] )
            """
            for i in self.__theRndGraph.getVrtxes():
                for n in i.getNeighbors():
                    if i.getNeighbors()[n] == edge[0]:
                        if self.check(con, i.getValue(), n.getValue()):
                            con.append((i.getValue(), n.getValue()))

            if self.debug:
                print('Edge: W: {} pair/s: {}'.format(edge[0], con))


            for pair in con:
                # search the vertex has a value of 'pair[n]'
                v1 = self.__theMST.srchVertex(pair[0])
                v2 = self.__theMST.srchVertex(pair[1])

                if self.debug:
                    print('Evaluate: ',pair)
                    print('Traversal: ')

                self.chckCycle(v1, v1.getNeighbors(), v2)

                self.__theMST.resetTrav() # reset the 'vertex.trav' for nxt traversal

                if self.debug:
                    print('isConnect?', end = "  ")

                if not self.__isCycle:
                    if self.debug:
                        print('1\n---------------------------------')
                    self.__theMST.conMe(v1, v2, edge[0])
                    self.__totalWeight += edge[0]
                else:
                    if self.debug:
                        print('0\n---------------------------------')
                self.__isCycle = False

            edge.remove(edge[0]) # rmv the frst index for the nxt edge to evaluate

            self.kruskal(edge,[])

    def prim(self):
        pass

    def GreedIsGood(self, debug = False, prnt = False):
        self.cpy(self.__theRndGraph, self.__theMST)
        self.debug = debug
        if self.debug:
            print('Edge: Weight:<evaulated weight> Pair\s:<list of pair has weight of \'edge\'')
            print('Evaluate: <[0],[1]>')
            print('Traversal: [<vertex evaluated> -:<vertex neighbor/s>]')
            print('isConnect? 0 or 1')

        self.kruskal(self.getEdges(self.__theRndGraph))

        if prnt:
            self.prntVrtxes()

        rndV = random.choice(self.__theMST.getVrtxes())
        self.__theMST.slctTraverse(rndV.getValue())
        self.__theMST.resetTrav()
        print('Total Weight: {}'.format(self.__totalWeight))
