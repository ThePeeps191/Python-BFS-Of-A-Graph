maze = [
	[" ", "#", "X", " "],
	["#", " ", " ", "#"],
	[" ", "#", " ", "#"],
	["O", " ", " ", " "],
	["#", "#", "#", " "],
	["#", " ", " ", "#"]
]

M, N = 6, 4 # dimensions
source = (0, 2) # starting point
target = (3, 0) # target point
parents = {}

def get_next(node):
	next_nodes = []
	dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	#dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
	for dir in dirs:
		row = node[0] + dir[0]
		col = node[1] + dir[1]
		if row >= 0 and row < M and col >= 0 and col < N and maze[row][col] != '#':
			next_nodes.append((row, col))
	return next_nodes

# BFS
def bfs():
	q = [source]
	parents[source] = None
	while q:
		curr = q.pop(0)
		for next in get_next(curr):
			if next == target:
				parents[next] = curr
				return
			elif next not in parents:
				q.append(next)
				parents[next] = curr

bfs()
if target not in parents:
	print("No path")
else:
	curr = target
	path = []
	while curr:
		path.append(curr)
		curr = parents[curr]
	for step in path:
		maze[step[0]][step[1]] = "+"
	print('\n'.join([''.join(k) for k in maze]))
	#print(*path[::-1])
