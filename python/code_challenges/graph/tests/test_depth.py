
from graph.graph import Graph
import pytest

@pytest.fixture
def graph():
    a_graph = Graph()
    n1 = a_graph.add_node("1")
    n2 = a_graph.add_node("2")
    n3 = a_graph.add_node("3")
    n4 = a_graph.add_node("4")
    return a_graph,n1,n2,n3,n4

def test_depth(graph):
    
    graph[0].add_edge(graph[1],graph[2])
    graph[0].add_edge(graph[2],graph[3])
    graph[0].add_edge(graph[3],graph[4])
    graph[0].add_edge(graph[4],graph[1])
    assert graph[0].depth_first(graph[1]) == ["4","3","2","1"]