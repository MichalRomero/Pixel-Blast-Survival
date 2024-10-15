import pygame
from sprite import sprites, Sprite
from player import Player
from input import keys_down
from map import Map, TileKind
from camera import create_screen
from entity import Entity, active_objs

# Set up 
pygame.init()

pygame.display.set_caption("Pixel Blast: Survival")
screen = create_screen(800, 600, "Pixel Blast: Survival")

clear_color = (30, 150, 50)
running = True

tile_kinds = [
    TileKind("dirt", "images/dirt.png", False),
    TileKind("grass", "images/grass.png", False),
    TileKind("water", "images/water.png", False),
    TileKind("wood", "images/wood.png", False)
]

player = Entity(Player(), Sprite("images/player.png"), x=32*11, y=32*7)
map = Map("maps/start.map", tile_kinds, 32)

def make_tree(x, y):
    Entity(Sprite("images/tree.png"), x=x, y=y)

make_tree(0 * 32, 0 * 32)
make_tree(7 * 32, 2 * 32)
make_tree(1 * 32, 10* 32)
make_tree(12* 32, -1* 32)
make_tree(14* 32, 9 * 32)
make_tree(12* 32, -1* 32)
make_tree(13* 32, 12* 32)
make_tree(20* 32, 9 * 32)
make_tree(22* 32, -1* 32)
make_tree(24* 32, 12* 32)
make_tree(2 * 32, 8 * 32)
make_tree(15* 32, 15* 32)
make_tree(17 * 32,1 * 32)
make_tree(1 * 32, 15 * 32)


# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            keys_down.remove(event.key)

    # Update Code
    for a in active_objs:
        a.update()

    # Draw Code
    screen.fill(clear_color)
    map.draw(screen)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()

    # Cap the frames
    pygame.time.delay(17)


# Break down Pygame
pygame.quit()