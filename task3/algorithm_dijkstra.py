import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))
        self.nodes.add(from_node)
        self.nodes.add(to_node)

def dijkstra(graph, start_node):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start_node] = 0

    priority_queue = [(0, start_node)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)
    g.add_edge('D', 'E', 3)

    start_node = 'A'
    distances = dijkstra(g, start_node)
    print(f"Відстані від {start_node}:")
    for node in distances:
        print(f"Відстань до {node} = {distances[node]}")

if __name__ == "__main__":
    main()
