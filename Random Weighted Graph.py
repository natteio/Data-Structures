# Random Weighted Graph

import random
class Vertex:
    def __init__(self,value):
        self.value=value
        self.neighbors={}
        self.degree=0
        self.trav=False
    def set_neighbor(self, val,key):
        self.neighbors[val]= key
        self.degree+=1
    def get_neighbors(self):
        return self.neighbors
    def get_value(self):
        return self.value
    def getDegree(self):
        return self.degree
    def isTraverse(self):
        return self.trav

class Graph:
    def __init__(self):
        self.vertices =[]
    def add_vertex(self,val):
        vertex =Vertex(val)
        self.vertices.append(vertex)
        return vertex
    def vertex_connect(self,val,val2):
        counter =0
        for i in val.get_neighbors():
            if i.get_value()== val2.get_value():
                counter+=1
        if counter ==0:
            key = random.randint(1,11)
            val.set_neighbor(val2,key)
            val2.set_neighbor(val,key)
    def getAllvertex(self):
        return self.vertices
    def selectTraverse(self,value):
        for i in self.getAllvertex():
            if i.get_value()==value:
                vertex=i
                break
        self.Traverse(vertex,vertex.get_neighbors())
    def Traverse(self,vertex,neighbor):
        if not vertex.isTraverse():
            print(vertex.get_value())
            print("neighbors:")
            for i in vertex.get_neighbors().keys():
                print(i.get_value(), ' Weight: ', vertex.get_neighbors()[i] )
            vertex.trav=True
        for i in neighbor:
            if not i.isTraverse():
                self.Traverse(i,i.get_neighbors())
class Rwg:
    def __init__(self):
        self.graph=Graph()
        self.values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.graph2=Graph()
    def setvertex(self):
        while self.values:
            no = random.choice(self.values)
            vertex = self.graph.add_vertex(no)
            self.connectrandomly(vertex)
            self.values.remove(no)

    def Traverse(self,value):
        print("traverse")
        self.graph.selectTraverse(value)

    def connectrandomly(self, vertex):
        if len(self.graph.getAllvertex())>1:
            noDegree = random.randint(1,len(self.graph.getAllvertex()))
            while noDegree>0:
                connecttothisvertex = random.choice(self.graph.getAllvertex())
                if not(connecttothisvertex.get_value()== vertex.get_value()) and len(self.graph.getAllvertex())>2:
                    self.graph.vertex_connect(vertex, connecttothisvertex)
                    noDegree-=1
                elif not(connecttothisvertex.get_value()==vertex.get_value()):
                    self.graph.vertex_connect(vertex,connecttothisvertex)
                    break
