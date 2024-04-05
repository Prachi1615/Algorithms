from collections import deque

def hasPath(maze, start, destination):
    queue = deque([start])
    visited = set()
    while queue:
        x, y = queue.popleft()
        if [x, y] == destination:
            return True
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newX, newY = x, y
            while 0 <= newX + dx < len(maze) and 0 <= newY + dy < len(maze[0]) and maze[newX + dx][newY + dy] == 0:
                newX += dx
                newY += dy
            if (newX, newY) not in visited:
                queue.append([newX, newY])

    return False

print("Test Cases : ")
print("Test case 1")
maze = [[0,0,1,0,0], [0,0,0,0,0], [0,0,0,1,0], [1,1,0,1,1], [0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print("Maze \n",maze,"\nStart \n",start,"\nDestination \n",destination)
print("Output")
print(hasPath(maze, start, destination))  # Output: true
print("Test case 2")
maze = [[0,0,1,0,0], [0,0,0,0,0], [0,0,0,1,0], [1,1,0,1,1], [0,0,0,0,0]]
start = [0,4]
destination = [3,2]
print("Maze \n",maze,"\nStart \n",start,"\nDestination \n",destination)
print("Output")
print(hasPath(maze, start, destination)) 
print("Test case 3")
maze = [[0,0,0,0,0], [1,1,0,0,1], [0,0,0,0,0], [0,1,0,0,1], [0,1,0,0,0]]
start = [4,3]
destination = [0,1]
print("Maze \n",maze,"\nStart \n",start,"\nDestination \n",destination)
print("Output")
print(hasPath(maze, start, destination)) 