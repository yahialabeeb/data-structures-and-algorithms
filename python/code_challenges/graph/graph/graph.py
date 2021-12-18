# from stack_and_queue import Queue, Stack

class Vertex:
    def __init__(self, value):
        self.value = value



class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.__adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self.__adjacency_list[v] = []
        print(self.__adjacency_list[v])
        return v

    

    def add_edge(self, start_vertex, end_vertex, weight=1):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        result = []
        nodes = self.__adjacency_list.keys()
        for i in nodes:
            result.append(i.value)
        return result
    def get_neighbors(self, vertex):
        return self.__adjacency_list.get(vertex, [])

    def size(self):
        return len(self.__adjacency_list)

    def __str__(self):
        if self.__adjacency_list == {}:
            return 
        return self.__adjacency_list


a_graph = Graph()
n1 = a_graph.add_node("1")
n2 = a_graph.add_node("2")
n3 = a_graph.add_node("3")
a_graph.add_edge(n1,n2)