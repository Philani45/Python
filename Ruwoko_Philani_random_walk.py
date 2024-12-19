import random


random.seed(43543)

grid, row = [],[]
grid_size = 15
grid = [[0] * grid_size for _ in range(grid_size)]
start_x, start_y = grid_size // 2, grid_size // 2
grid[start_x][start_y] = 1


UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4


agent_x, agent_y = start_x, start_y
moves = 100
move_count = 0


def print_grid(grid):
    for row in grid:
        for cell in row:
            print(f'{cell:2}', end=' ')
        print()


while move_count < moves:
    rand_int = random.randint(1, 20)

  
    if 1 <= rand_int <= 7:
        move_direction = UP
    elif 8 <= rand_int <= 14:
        move_direction = DOWN
    elif 15 <= rand_int <= 17:
        move_direction = LEFT  
    else:
        move_direction = RIGHT

  
    new_x, new_y = agent_x, agent_y

    if move_direction == UP:
        new_x -= 1
    elif move_direction == DOWN:
        new_x += 1
    elif move_direction == LEFT:
        new_y -= 1
    else:
        new_y += 1

   
    if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
        grid[new_x][new_y] += 1
        agent_x, agent_y = new_x, new_y
        move_count += 1


print("Movement Heat Map:")
print_grid(grid)


manhattan_distance = abs(agent_x - start_x) + abs(agent_y - start_y)


print(f"Final Position: ({agent_x}, {agent_y})")
print(f"Manhattan Distance: {manhattan_distance}")
