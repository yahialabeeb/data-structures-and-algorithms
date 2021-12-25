import pytest
from graph.graph import Graph
from graph.graph_business_trip import business_trip
@pytest.fixture
def city_graph():
    a_graph = Graph()
    Pandora = a_graph.add_node("Pandora")
    Metroville = a_graph.add_node("Metroville")
    Arendelle = a_graph.add_node("Arendelle")
    Naboo = a_graph.add_node("Naboo")
    a_graph.add_edge(Pandora,Metroville,82)
    a_graph.add_edge(Pandora,Arendelle,150)

    a_graph.add_edge(Arendelle,Metroville,99)
    a_graph.add_edge(Arendelle,Pandora,150)

    a_graph.add_edge(Metroville,Arendelle,99)
    a_graph.add_edge(Metroville,Pandora,82)
    a_graph.add_edge(Metroville,Naboo,26)

    return [a_graph,
        Pandora ,
        Metroville ,
        Arendelle ,
        Naboo
        ]

def test_Metroville_Pandora(city_graph):
    assert business_trip(city_graph[0],[city_graph[2],city_graph[1]]) == (True, "$82")


def test_Arendelle_Metroville_Naboo(city_graph):
    assert business_trip(city_graph[0],[city_graph[3],city_graph[2],city_graph[4]]) == (True, "$125")


def test_Naboo_Pandora(city_graph):
    assert business_trip(city_graph[0],[city_graph[4],city_graph[1]]) == (False, "$0")
