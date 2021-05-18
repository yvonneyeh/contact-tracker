from data import users
from collections import deque

def BFS(graph, user1, user2):
    """ Find shortest path between 2 user nodes in a graph"""
    explored = []
     
    # Queue for traversing the graph in the BFS
    queue = deque([[user1]])
     
    # If the desired user is already found
    if user1 == user2:
        print("Same User")
        return 0
     
    # Loop to traverse the graph with the help of the queue
    while queue:
        path = queue.popleft()
        node = path[-1]
         
        # Condition to check if the current node is not visited
        if node not in explored:
            neighbors = graph[node]
             
            # Loop to iterate over the neighbors of the node to find mutual connections
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                # print(new_path)
                # print(len(new_path))
                 
                # Condition to check if the neighbor node is the target
                if neighbor == user2:
                    print("Shortest path:", *new_path) 
                    return len(new_path) # Degrees of separation
            explored.append(node)
 
    # Condition when the nodes are not connected
    print("A connection between these users does not exist.")
    return -1
 

# Driver Code
if __name__ == "__main__":

    # Function Call
    BFS(users, 'Alex', 'Danny')