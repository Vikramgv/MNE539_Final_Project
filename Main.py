import heapq  # Data structure that allows us to quickly access the smallest (min-heap) or largest (max-heap) element

# Step 1: Define the graph 
graph = {
    # Buildings  (A to H)
    'A': [('B', 400), ('F', 400), ('C', 800), ('G', 800), ('Lot 1', 400), ('Lot 17', 300), ('Lot 16', 400), ('Lot 15', 500), ('Lot 14', 500), ('Lot 13', 500)],  # A -> Dion, CCB, Library, SENG, Textiles, Violette
    'B': [('D', 300), ('F', 100), ('A', 400), ('Lot 1', 500), ('Lot 2', 400), ('Lot 3', 400), ('Lot 4', 400), ('Lot 5', 400), ('Lot 6', 400), ('Lot 8', 500)],  # B -> LARTS, Auditorium, CVPA
    'C': [('F', 900), ('A', 800), ('G', 500)],  # C -> Cedar Dell
    'D': [('F', 100), ('E', 600), ('B', 300), ('H', 600), ('Lot 21', 500)],  # D -> Balsam, Spruce, Grove
    'E': [('D', 600), ('Lot 5', 400), ('Lot 19', 100), ('Lot 20', 50), ('Lot 21', 50)],  # E -> Oak Glen, Pine Dale, Health Service
    'F': [('D', 100), ('A', 400), ('B', 100), ('G', 700), ('H', 300), ('C', 900), ('Lot 8', 100)],  # F -> Foster, CVPA
    'G': [('C', 500), ('H', 100), ('A', 800), ('F', 700), ('Lot 9', 200), ('Lot 10', 200), ('Lot 11', 200), ('Lot 12', 200), ('Lot 13', 300), ('Lot 14', 300), ('Lot 23', 100), ('Lot 24', 100)],  # G -> Woodland Apartments
    'H': [('D', 600), ('G', 100), ('F', 300), ('Lot 21', 700), ('Lot 22', 100)],  # H -> Athletic Center

    # Parking Lots (numbered from Lot 1 to Lot 24) 
    'Lot 1': [('A', 400), ('B', 500)],  
    'Lot 2': [('B', 400)],  
    'Lot 3': [('B', 400)],
    'Lot 4': [('B', 400), ('Lot 18', 700)],  
    'Lot 5': [('B', 400), ('E', 400)],  
    'Lot 6': [('B', 400)],  
    'Lot 8': [('B', 500), ('F', 100)],  
    'Lot 9': [('G', 200)],  
    'Lot 10': [('G', 200)],  
    'Lot 11': [('G', 200)],  
    'Lot 12': [('G', 200)],  
    'Lot 13': [('A', 500), ('G', 300)],  
    'Lot 14': [('A', 500), ('G', 300)],  
    'Lot 15': [('A', 500)],  
    'Lot 16': [('A', 400)],  
    'Lot 17': [('A', 300)],  
    'Lot 18': [('Lot 4', 700), ('Lot 19', 100)],  
    'Lot 19': [('E', 100), ('Lot 18', 100), ('Lot 20', 50)],  
    'Lot 20': [('E', 50), ('Lot 19', 200), ('Lot 21', 50)],  
    'Lot 21': [('D', 500), ('E', 50), ('H', 700), ('Lot 20', 50)],  
    'Lot 22': [('H', 100)],  
    'Lot 23': [('G', 100)],  
    'Lot 24': [('G', 100)],  
}

# Step 2: Dijkstra's Algorithm
def dijkstra(graph, start, end):
    queue = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}  # Initialize all distances to infinity
    distances[start] = 0
    parent = {start: None}  # To store the path
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Get the node with the smallest distance
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))
    
    # Reconstruct the path from the destination node to the start node
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = parent[current_node]

    path.reverse()  # Reverse the path to get it from start to end
    return distances[end], path

# Step 3: Function to display the path between two nodes
def display_path(path):
    print(" -> ".join(path))

# Step 4: User Input and Program Options
def main():
    print("Select an option:")
    print("1. Distance between two nodes")
    print("2. Nearest parking lot to a building")
    
    choice = int(input("Enter choice (1 or 2): "))
    
    if choice == 1:
        # Option 1: Distance between two nodes
        print("Available buildings and parking lots:")
        print("Buildings: A - Dion, CCB, Library, SENG, Textiles, Violette; B - LARTS, Auditorium, Campus Center; C - Cedar Dell, D - Balsam, Spruce, Grove; E - Oak Glen, Pine Dale, Health Services; F - Foster, CVPS; G - Woodland Apartments, H - Athletic Center")
        print("Parking Lots: Lot 1 - Lot 24")
        
        # Get the start and end nodes (convert input to uppercase to handle case insensitivity)
        start = input("Enter the starting point (A-H or Lot 1-24): ").strip().upper()
        end = input("Enter the destination (A-H or Lot 1-24): ").strip().upper()

        # Convert parking lot number to "Lot X" format if it's just a number
        if start.isdigit():
            start = f"Lot {start}"
        if end.isdigit():
            end = f"Lot {end}"
        
        # Case-insensitive validation for building names and parking lots
        if start not in graph or end not in graph:
            print("Invalid input. Please enter valid nodes.")
            return

        distance, path = dijkstra(graph, start, end)
        if distance == float('inf'):
            print(f"No path exists from {start} to {end}.")
        else:
            print(f"The shortest path from {start} to {end} is:")
            display_path(path)  # Display the path from start to end
            print(f"Total distance: {distance} meters")

    elif choice == 2:
        # Option 2: Nearest parking lot to a building
        print("Available buildings: A - Science and Engineering, B - Liberal Arts, C - Cedar Dell, D - Balsam and Spruce, E - Oak Glen, F - Foster, G - Woodland Apartments, H - Athletic Center")
        building = input("Enter the building name (A-H): ").strip().upper()

        # Case-insensitive validation for building names
        if building not in graph:
            print("Invalid building name. Please enter a valid building.")
            return

        nearest_lot = None
        min_distance = float('inf')
        
        # Loop through all parking lots to find the nearest one
        for lot, edges in graph.items():
            if lot.startswith("Lot"):  # Check if it's a parking lot
                for neighbor, distance in edges:
                    if neighbor == building and distance < min_distance:
                        nearest_lot = lot
                        min_distance = distance

        if nearest_lot:
            print(f"The nearest parking lot to {building} is {nearest_lot}, located {min_distance} meters away.")
        else:
            print(f"No parking lot found near {building}.")

if __name__ == "__main__":
    main()
