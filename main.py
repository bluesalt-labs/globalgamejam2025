# Example file showing a basic pygame "game loop"
import pygame
import random

def main():

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_speed = 400
    object_speed = 100

    slope_start_range = 365, 831

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - 75)
    player_image = pygame.image.load("images/forog4.gif")
    tree_image = pygame.image.load("images/tree1.png")
    tree_image.set_colorkey((255,255,255))
    trees = []
    # tree_points = ((-40,20),(0,-60),(40,20),(10,20),(10,50),(-10,50),(-10,20),(-40,20))
    # new_tree = []
    # for point in tree_points:
    #     new_point = point[0]+500, point[1]+500
    #     new_tree.append(new_point)
    # trees.append(new_tree)
    # new_tree = []
    # for point in tree_points:
    #     new_point = point[0]*2+900, point[1]*2+500
    #     new_tree.append(new_point)
    # trees.append(new_tree)

    # new_tree = []
    # for point in tree_points:
    #     new_point = point[0]*.5+600, point[1]*.5+450
    #     new_tree.append(new_point)
    # trees.append(new_tree)

    trees.append([500, 500, 1])
    trees.append([900, 500, 2])
    trees.append([600, 450, 0.5])

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("light blue")


        #Draw clouds.

        #Draw mountains
        pygame.draw.polygon(screen, "grey", ((600,100), (450, 600), (700, 600)))

        pygame.draw.polygon(screen, "grey", ((800,200), (450, 600), (900, 600)))
        #Draw slope
        #draw Sides
        #left
        pygame.draw.polygon(screen, "light grey", ((0, 200), (0, 720), (800, 720)))
        #right
        pygame.draw.polygon(screen, "light grey", ((1280, 200), (1280, 720), (300, 720)))
        #ride surface
        pygame.draw.polygon(screen, "white", ((0,720), (365, 438), (831,438), (1280, 720)))



        # Handle/Draw trees
        # Add new trees?
        for tree in trees:
            tree[1] += object_speed * dt
            print(tree[0])
            if tree[1] > 720:
                tree[1] = 450
                tree[0] = random.randint(slope_start_range[0], slope_start_range[1])
            tree[2] = 50 / (720 - (tree[1]) + 1)
            new_img = pygame.transform.scale_by(tree_image, tree[2])
            screen.blit(new_img, (tree[0] - new_img.get_width() /2, tree[1]-new_img.get_height()))


        screen.blit(player_image, (player_pos.x - player_image.get_width()/2, player_pos.y - player_image.get_height()/2))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player_pos.x -= player_speed * dt
        if keys[pygame.K_d]:
            player_pos.x += player_speed * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
