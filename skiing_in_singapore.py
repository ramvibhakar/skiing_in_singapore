__author__ = 'ramvibhakar'
import networkx as nx
from datetime import datetime

startTime = datetime.now()
FILE_NAME = 'map.txt'
f = open(FILE_NAME, 'r')
rows, columns = [int(x) for x in f.readline().split()]
G = nx.DiGraph()

#TODO: Write an efficient neighbour calculation function
neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x < rows and
                                   -1 < y < columns and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 < rows) and
                                   (0 <= y2 < columns) and
                                   (x2 == x or y2 == y))]
def unique_id(x,y):
    return x*rows + y

def input_into_graph():

    elevation = []
    for i in xrange(0,rows):
        elevation.append([int(x) for x in f.readline().split()])
    for i in xrange(0,rows):
        for j in xrange(0,columns):
            G.add_node(unique_id(i,j),{'elevation':elevation[i][j]})
    for i in xrange(0,rows):
        for j in xrange(0,columns):
            edges = []
            for neighbor_x, neighbor_y in neighbors(i,j):
                neighbor_elev = elevation[neighbor_x][neighbor_y]
                my_elev = elevation[i][j]
                if neighbor_elev < my_elev:
                    edges.append((unique_id(i,j),unique_id(neighbor_x,neighbor_y), my_elev-neighbor_elev))
            G.add_weighted_edges_from(edges)

def longest_path(G):
    dist = {} # stores [node, distance] pair
    for node in nx.topological_sort(G):
        # pairs of dist,node for all incoming edges
        pairs = [(dist[v][0]+1,v) for v in G.pred[node]]
        if pairs:
            dist[node] = max(pairs)
        else:
            dist[node] = (0, node)
    node,(length,_) = max(dist.items(), key=lambda x:x[1])
    max_length = length
    all_max = [(x,dist[x][0]) for x in dist if dist[x][0] == max_length]
    path = []
    final_paths = []
    for node, length in all_max:
        while length > 0:
            path.append(node)
            length,node = dist[node]
        possible_path = list(reversed(path))
        final_paths.append(possible_path)
    return final_paths, max_length
def main():
    input_into_graph()
    paths,max_length = longest_path(G)
    max_slope = 0
    for path in paths:
        highest_point = G.nodes(data=True)[path[0]][1]['elevation']
        lowest_point = G.nodes(data=True)[path[len(path)-1]][1]['elevation']
        slope = highest_point - lowest_point
        if slope > max_slope:
            max_slope = slope
    print('The longest path is : '+ str(max_length))
    print('The slope of the path is : '+ str(max_slope))

if __name__ == "__main__":
    main()
    total_time_taken = datetime.now() - startTime
    print ('The program was excecuted in ' + str(total_time_taken))