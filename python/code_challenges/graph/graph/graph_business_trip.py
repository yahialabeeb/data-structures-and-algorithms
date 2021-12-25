from .stack_and_queue import Queue, Stack
from .graph import Graph

def business_trip(city_graph,city_list:list):

    queue = Queue()
    city_idx = 1
    count = 0
    queue.enqueue(city_list[0])
    

    while queue.front:
        current_vertex = queue.dequeue()
        neighbors = city_graph.get_neighbors(current_vertex)

        for edge in neighbors:
            neighbor = edge.vertex
            w = edge.weight

            if city_idx < len(city_list):
                if neighbor == city_list[city_idx]:
                    queue.enqueue(neighbor)
                    city_idx +=1
                    count += w
            
    return count!=0, f"${count}"

# a_graph = Graph()
# n1 = a_graph.add_node("1")
# n2 = a_graph.add_node("2")
# n3 = a_graph.add_node("3")
# a_graph.add_edge(n1,n2)
# a_graph.add_edge(n2,n3)
# print(business_trip(a_graph,[n1,n2,n3]))
