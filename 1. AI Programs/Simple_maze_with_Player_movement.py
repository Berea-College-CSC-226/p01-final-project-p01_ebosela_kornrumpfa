import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
TILE_SIZE = 50
MAZE_WIDTH = 10
MAZE_HEIGHT = 10
WINDOW_WIDTH = TILE_SIZE * MAZE_WIDTH
WINDOW_HEIGHT = TILE_SIZE * MAZE_HEIGHT


# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
GOLD = (255, 215, 0)

# Maze layout: W = Wall, ' ' = open, I = Item
maze = [
    [' ', 'W', ' ', ' ', 'W', ' ', ' ', ' ', 'W', ' '],
    [' ', 'W', ' ', 'W', 'W', ' ', 'W', ' ', 'W', ' '],
    [' ', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', ' '],
    ['W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', ' '],
    [' ', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' '],
    [' ', 'W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', ' '],
    [' ', 'W', ' ', ' ', ' ', ' ', ' ', 'W', 'I', ' '],
    [' ', 'W', ' ', 'W', 'W', 'W', ' ', 'W', 'W', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' '],
]


# Setup display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Game")

# Player position
player_pos = [0, 0]
has_item = False

def draw_maze():
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

            tile = maze[y][x]
            if tile == 'W':
                pygame.draw.rect(screen, BLACK, rect)
            elif tile == 'I' and not has_item:
                pygame.draw.rect(screen, GOLD, rect)
            else:
                pygame.draw.rect(screen, GRAY, rect)

            pygame.draw.rect(screen, WHITE, rect, 2)

    # Draw player
    px, py = player_pos
    pygame.draw.circle(
        screen, GREEN,
        (px * TILE_SIZE + TILE_SIZE // 2, py * TILE_SIZE + TILE_SIZE // 2),
        TILE_SIZE // 3
    )

def move_player(dx, dy):
    global has_item
    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy

    if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT:
        if maze[new_y][new_x] != 'W':
            player_pos[0] = new_x
            player_pos[1] = new_y

            if maze[new_y][new_x] == 'I':
                has_item = True
                print("🎉 You picked up the item!")

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    draw_maze()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(1, 0)
            elif event.key == pygame.K_UP:
                move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                move_player(0, 1)

    clock.tick(60)

pygame.quit()
sys.exit()
