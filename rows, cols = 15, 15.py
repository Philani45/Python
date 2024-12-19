# Create a 3x3 grid filled with zeros
rows, cols = 15, 15
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Modify elements
grid[1][2] = 42

# Print the grid
for row in grid:
    print(row)
