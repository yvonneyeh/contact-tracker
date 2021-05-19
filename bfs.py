from data import users
from collections import deque
import crud


def find_distance_between_users(user_id_1, user_id_2):
    """ Find shortest path between 2 user objects."""

    user1 = crud.get_user_by_id(user_id_1)
    user2 = crud.get_user_by_id(user_id_2)

    u1_connects = crud.get_connect_by_user_id(user_id_1)
    u2_connects = crud.get_connect_by_user_id(user_id_2)

    explored = []
    queue = deque([[user1]])
     
    if user1 == user2:
        return 0
     
    while queue:
        path = queue.popleft()
        node = path[-1]
         
        if node not in explored:
            neighbors = u1_connects[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == user2:
                    print("Shortest path:", *new_path) 
                    return len(new_path) # Degrees of separation
            explored.append(node)
    return -1


# Sample BFS function
# same logic as above but able to be tested without a seeded database
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