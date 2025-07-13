WIDTH = 10
HEIGHT = 10

# World initialization
world = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
player_x = WIDTH // 2
player_y = HEIGHT // 2

def print_world():
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                row += "@"
            else:
                row += world[y][x]
        print(row)
    print("-" * WIDTH)

def move_player(direction):
    global player_x, player_y
    if direction == "w" and player_y > 0:
        player_y -= 1
    elif direction == "s" and player_y < HEIGHT - 1:
        player_y += 1
    elif direction == "a" and player_x > 0:
        player_x -= 1
    elif direction == "d" and player_x < WIDTH - 1:
        player_x += 1

def place_block():
    world[player_y][player_x] = "#"

def remove_block():
    world[player_y][player_x] = "."

# Game loop
print("Simple Sandbox Game")
print("Use W/A/S/D to move, B to build, R to remove, Q to quit.")
print_world()

while True:
    command = input("Command: ").lower()

    if command == "q":
        print("Exiting game.")
        break
    elif command in ["w", "a", "s", "d"]:
        move_player(command)
    elif command == "b":
        place_block()
    elif command == "r":
        remove_block()
    else:
        print("Invalid command!")

    print_world()