import sys

class Graph:
    def __init__(self, vertices):
        """Initializes a graph with a specified number of vertices.

        Args:
            vertices (int): Number of vertices in the graph.
        """
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def print_mst(self, parent):
        """Prints the edges and weights of the constructed Minimum Spanning Tree (MST).

        Args:
            parent (list): List containing the parent of each vertex in the MST.
        """
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")

    def min_key(self, key, in_mst):
        """Finds the vertex with the minimum key value that is not yet included in the MST.

        Args:
            key (list): List of key values for each vertex.
            in_mst (list): List indicating whether a vertex is included in the MST.

        Returns:
            int: Index of the vertex with the minimum key value.
        """
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_value and not in_mst[v]:
                min_value = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        """Constructs and prints the MST for the graph using Prim's algorithm."""
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        in_mst = [False] * self.V

        key[0] = 0  # Start from the first vertex
        parent[0] = -1  # First node is the root of the MST

        for _ in range(self.V):
            u = self.min_key(key, in_mst)
            in_mst[u] = True  # Include vertex u in the MST

            for v in range(self.V):
                # Update the key and parent if an edge is found that is less than the current key
                if self.graph[u][v] > 0 and not in_mst[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

def main():
    """Main function to execute the Prim's MST algorithm."""
    try:
        # Input the number of vertices
        num_vertices = int(input("Enter the number of vertices: "))
        g = Graph(num_vertices)

        # Input the adjacency matrix
        print("Enter the adjacency matrix (use 0 for no edge):")
        for i in range(num_vertices):
            row = list(map(int, input().split()))
            g.graph[i] = row

        # Execute Prim's algorithm
        g.prim_mst()

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == '__main__':
    main()
