from graph import __version__
from graph.graph import Graph,Vertex
import pytest
def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def a_graph():
    a_graph = Graph()
    n1 = a_graph.add_node("1")
    n2 = a_graph.add_node("2")
    n3 = a_graph.add_node("3")
    a_graph.add_edge(n1,n2)
    a_graph.add_edge(n1,n3)
    return a_graph,n1,n2,n3

# Node can be successfully added to the graph

def test_adding_node():
    a_graph = Graph()
    a_graph.add_node("yahia")
    assert ["yahia"] == a_graph.get_nodes()


# An edge can be successfully added to the graph
# A collection of all nodes can be properly retrieved from the graph
# All appropriate neighbors can be retrieved from the graph
def test_edge_adding(a_graph):

    x = a_graph[0].get_neighbors(a_graph[1])
    assert [a_graph[2],a_graph[3]] == [x[0].vertex,x[1].vertex]

# Neighbors are returned with the weight between nodes included

def test_edge_weight(a_graph):

    x = a_graph[0].get_neighbors(a_graph[1])
    assert 1 == x[0].weight
# The proper size is returned, representing the number of nodes in the graph
def test_size(a_graph):
    assert 3 == a_graph[0].size()
# A graph with only one node and edge can be properly returned
def test_one_node():    
    a_graph = Graph()
    n1 = a_graph.add_node("1")
    a_graph.add_edge(n1,n1)
    
    assert n1 == a_graph.get_neighbors(n1)[0].vertex

# An empty graph properly returns null
def test_empty_graph():
    a_graph = Graph()
    assert not a_graph.__str__()

@pytest.fixture
def graph():
    a_graph = Graph()
    n1 = a_graph.add_node("1")
    n2 = a_graph.add_node("2")
    n3 = a_graph.add_node("3")
    n4 = a_graph.add_node("4")
    return a_graph,n1,n2,n3,n4

def test_breadth1(graph):
    
    graph[0].add_edge(graph[1],graph[2])
    graph[0].add_edge(graph[2],graph[3])
    graph[0].add_edge(graph[3],graph[4])
    graph[0].add_edge(graph[4],graph[1])
    assert graph[0].breadth_first_search(graph[1]) == ["1","2","3","4"] 

def test_breadth2(graph):
    graph[0].add_edge(graph[4],graph[2])
    graph[0].add_edge(graph[2],graph[1])
    graph[0].add_edge(graph[1],graph[3])
    graph[0].add_edge(graph[4],graph[1])
    assert graph[0].breadth_first_search(graph[4]) == ['4', '2', '1', '3'] 

def test_breadth3(graph):
    graph[0].add_edge(graph[1],graph[2])
    graph[0].add_edge(graph[1],graph[3])
    graph[0].add_edge(graph[1],graph[4])
    assert graph[0].breadth_first_search(graph[1]) == ["1","2","3","4"] 