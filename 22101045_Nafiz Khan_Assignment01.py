import heapq

read = open('input.txt', 'r').readlines()
heuristic_val = {}
cities_graph = {}
rev_map = {}

map_city = {
    'Arad': 'A', 'Bucharest': 'Z', 'Craiova': 'S', 'Eforie': 'T', 'Fagaras': 'O',
    'Dobreta': 'V', 'Hirsova': 'N', 'lasi': 'Q', 'Neamt': 'F', 'Oradea': 'B',
    'Pitesti': 'P', 'RimnicuVilcea': 'R', 'Timisoara': 'C', 'Urziceni': 'D',
    'Vaslui': 'H', 'Zerind': 'E', 'Lugoj': 'G', 'Mehadia': 'L', 'Sibiu': 'I', 'Giurgiu': 'M'}


for city,val in map_city.items(): #Result er shomoy full name show
    rev_map[val] = city


for line in read:
    parts = line.split()
    city, h_val = parts[0], parts[1]        # Arad:366
    if city in map_city and h_val.isdigit():
        city_short = map_city[city]         # Arad er A store kortese
        heuristic_val[city_short] = int(h_val)          # A:366

    neigh_nodes = {}
    for i in range(2, len(parts), 2):                 # Zerind, Timisoara, Sibiu
        if parts[i] in map_city and parts[i + 1].isdigit():     # 'E': 75, 'C': 118, 'I': 140
            neigh_nodes[map_city[parts[i]]] = int(parts[i + 1])
            cities_graph[city_short] = neigh_nodes    # {'A': {'E': 75, 'C': 118, 'I': 140}}


# Main Algo
def a_star_algorithm(start, goal, graph, heuristic):
    start_node = [(heuristic[start], start)]  #  (Arad,366)
    prev_node = {}  #prev nodes er track rakhtesi as graph
    g_value = {}
    for city in graph:
        g_value[city] = float('inf')  # Initially shob gulay infinity store korsi
    g_value[start] = 0  # Just start k 0 korsi; #{'A': 0, 'S': inf, 'T': inf, 'O': inf,.....

    while start_node:
        popped_item = heapq.heappop(start_node) #lowest k pop korbo
        priority, current = popped_item
        if current == goal:
            path = path_find(prev_node, current)
            return path, calculate_distance(path, graph)

        for neigh_node, value in graph[current].items():
            temp_val = g_value[current] + value
            if temp_val < g_value[neigh_node]:
                prev_node[neigh_node] = current
                g_value[neigh_node] = temp_val
                priority = temp_val + heuristic[neigh_node]
                heapq.heappush(start_node,(priority,neigh_node))


    return None, None


def path_find(prev_node, current):
    path = [current]
    while current in prev_node:
        current = prev_node[current]
        path.append(current)
    return path[::-1]

def calculate_distance(path, graph):
    sum = 0
    for i in range(len(path)-1):
        sum += graph[path[i]][path[i+1]]
    return sum

#------------------------------------------Driver Code------------------------------------------------

s_city = input("Start Node: ")
if s_city in map_city:
    start_city = map_city[s_city]
else:
    print("Invalid start city")


g_city = input("Start Node: ")
if g_city in map_city:
    goal_city = map_city[g_city]
else:
    print("Invalid goal city")

path, distance = a_star_algorithm(start_city, goal_city, cities_graph, heuristic_val)

if path:
    mapped_path = []
    for city in path:
        mapped_path.append(rev_map[city])
    path = " -> ".join(mapped_path)
    print(f"Path: {path}")
    # print(f"Path: {mapped_path}")
    print(f"Total distance: {distance} km")
else:
    print("No path found.")
