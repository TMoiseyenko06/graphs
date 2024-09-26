import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}
        
    #With large graphs the thing that holds this back the most is the priority queue so the time complexity is usually O((V+E) log V) where V is veerticies and E is edges and the space complexity is simply O(V)
    def dijkstras(self,start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            cd, cv = heapq.heappop(pq)
            if cd > distances[cv]:
                continue
            for neighbor, weight in self.vertices[cv].items():
                d = cd + weight
                if d < distances[neighbor]:
                    distances[neighbor] = d
                    heapq.heappush(pq,(d,neighbor))

        return distances

# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 3)
graph.add_edge('A', 'C', 10)


print(graph.dijkstras('A'))