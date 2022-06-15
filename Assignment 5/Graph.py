from copy import deepcopy

class Edge:
    def __init__(self, origin, dest, weight):
       self.origin = origin
       self.dest = dest
       self.weight = weight

class Graph:
    def __init__(self, filename, flag):
        """
        Graph constructor
        You will implement your graph here either using adjacency list or adjacency matrix
        True flag -> directed graph, False flag -> undirected graph 
        filename will be the .txt file from which you will be loading your graph
        Format of .txt file is as given in the manual
        Construct this class as you deem fit 
        """
        self.graph = dict()
        is_directed = flag


        # reading the lines of the file
        file = open(filename, 'r')
        lines = file.readlines()
        lines = lines[2:] # the first two lines are not needed for AL Implementation

        for line in lines:
            # the format of a line is S E W, W can be multichar
            start = line[0]
            end = line[2]
            weight = int(line[4:-1])

            self.add_edge(start, end, weight, is_directed)
    
    def add_edge(self, start, end, weight, flag):
        """
        inserts edge connecting start and end with weight to the graph
        does not require a return value 
        """

        # if the graph is undirected, add two edges to the graph, otherwise add one
        if flag:
            new_edge = Edge(start, end, weight)
            
            # if the vertice exists in the dict, 
            # append to the list of edges, otherwise create the list of edges with the new edge

            if start in self.graph: 
                self.graph[start].append(new_edge)
                return 
            
            self.graph[start] = [new_edge]
            return
        
        self.add_edge(start, end, weight, True)
        self.add_edge(end, start, weight, True)
        
    
        return
    
    def display(self):
        """
        displays the graph in a certain format (given in Manual)
        returns a string 
        """
        result = []

        for _ , edges in sorted(self.graph.items()):
            for edge in edges:
                result += [(f"({edge.origin},{edge.dest},{edge.weight})")]

        result.sort()
        result = " ".join(result)
        return result

    def dfs(self, start, end, visited):
        
        if start == end:
            return True

        if start in visited:
            return False
        
        visited.append(start)

        for edge in self.graph[start]:
            result = self.dfs(edge.dest, end, visited)

            if result:
                return True
    
        return False

    def reachable(self, start, end):
        """
        determines if node end is reachable by node start
        returns a boolean
        """

        if not start in self.graph:
            return False
        

        return self.dfs(start, end, [])

    

    def dijkstra(self, start, end):
        """
        determines shortest path between start and end
        returns an int
        """

        if not self.reachable(start, end):
            return -1

        # make a list of unvisited vertices
        unvisited_vertex = [vertex for vertex in self.graph]

        # make a list of visited vertices
        visited_vertex = []

        # make a distance table to store distances
        distance_table = {vertex : float("inf") for vertex in self.graph}

        # set the distance from the starting node = 0
        distance_table[start] = 0

        unvisited_vertex.remove(start)

        for edge in self.graph[start]:
            # print(f'{edge = }')
            if edge.weight < distance_table[edge.dest]:
                distance_table[edge.dest] = edge.weight

        temp_list = list(distance_table.items())
        temp_list.sort(key= lambda i:i[1])

        next_vertex = None

        for vertex, _ in temp_list:
            if vertex in unvisited_vertex:
                next_vertex = vertex
                break

        # print(f'{next_vertex = }')


        while unvisited_vertex:
            # find the vertex with the smallest distance
            # visit that vertex in a similar fashion

            temp_list = list(distance_table.items())
            temp_list.sort(key= lambda i:i[1])

            next_vertex = None

            for vertex, _ in temp_list:
                if vertex in unvisited_vertex:
                    next_vertex = vertex
                    break

            # print(f'{next_vertex = }')

            own_dist = distance_table[next_vertex]

            for edge in self.graph[next_vertex]:
                if own_dist + edge.weight < distance_table[edge.dest]:
                    distance_table[edge.dest] = own_dist + edge.weight

            unvisited_vertex.remove(next_vertex)

        

        # print(f'{temp_list = }')
        # print(f'{unvisited_vertex = }')

        return distance_table[end]

    
    def topo_sort(self):
        """
        sorts the graph using the toposort algorithm
        returns a string. Format: ABCDEF
        """

        # compute the in-degree of each node
        # choose the vertex with in = 0 and put it in the sorted sequence
        # remove in = 0 node and recompute in degree

        res = []
        temp = []

        tree_copy = deepcopy(self.graph)

        nodes = {key : 0 for key in tree_copy}

        for node in self.graph:
            for edge in self.graph[node]:
                if edge.dest in nodes:
                    nodes[edge.dest] += 1
                else:
                    nodes[edge.dest] = 1

        
        for key, val in nodes.items():
            if val == 0:
                temp.append(key)

        for key in temp:
            nodes.pop(key)

        while temp:
            
            node = temp.pop(0)
            res.append(node)
            
            if node in self.graph:
                for edge in self.graph[node]:
                    if edge.dest in nodes:
                        nodes[edge.dest] -= 1

            for key, val in nodes.items():
                if val == 0:
                    temp.append(key)

            for key in temp:
                if key in nodes:
                    nodes.pop(key)  



        return "".join(res)
        


  

if __name__ == "__main__":

    # You can make your own graph to test here

    my_graph = Graph("graph1.txt", True)

    # print(my_graph.topo_sort())
    # print(my_graph.graph)

    print(my_graph.topo_sort())

    

    pass

# main()