import pygame, time, random

pygame.init()


def play():
    width = 1000
    height = 760
    squar_size = 40
    screen = pygame.display.set_mode((width, height))
    x = width // squar_size * 10
    y = height // squar_size * 8
    wx = squar_size
    coor = 0
    coords = [(x, y), (x - squar_size, y), (x - squar_size * 2, y)]
    random_coord_for_apple_x = [i for i in range(100, width, squar_size)]
    random_coord_for_apple_y = [i for i in range(100, height, squar_size)]
    apple_x = random.choice(random_coord_for_apple_x)
    apple_y = random.choice(random_coord_for_apple_y)
    scoors = 0
    image_apple = pygame.image.load("images/apple.png")
    tail_snake = pygame.image.load("images/body_horizontal.png")
    tail_snake_2 = pygame.image.load("images/body_vertical.png")
    head_up = pygame.image.load("images/head_up.png")
    head_down = pygame.image.load("images/head_down.png")
    head_right = pygame.image.load("images/head_right.png")
    head_left = pygame.image.load("images/head_left.png")
    wall = pygame.image.load("images/wall.png")
    random_coord_for_wall_x = [i for i in range(100, width, squar_size)]
    random_coord_for_wall_y = [i for i in range(100, width, squar_size)]
    wall_x = random.choice(random_coord_for_wall_x)
    wall_y = random.choice(random_coord_for_wall_y)
    sp = [0, 0, 0]
    r = 0
    bullet = pygame.image.load("images/bullet.png")
    bullet_x = wall_x
    bullet_y = wall_y
    rose_of_wind = [(0, False), (0, True), (1, False), (1, True)]
    f = 0
    speed = 1
    speed_rec = 10
    l3 = False
    while True:
        if speed == speed_rec:
            speed -= 10
            speed_rec += 10
        l3 = False
        screen.fill((0, 0, 205))
        for l1 in range(width // squar_size):
            for l2 in range(height // squar_size):
                if l3:
                    pygame.draw.rect(screen, (0, 0, 225), (l1 * squar_size, l2 * squar_size, squar_size, squar_size))
                l3 = not l3
        screen.blit(wall, (wall_x, wall_y))
        font_1 = pygame.font.SysFont("Calibri", 52)
        font_2 = font_1.render(str(scoors), False, (255, 255, 0))
        screen.blit(font_2, (450, 70))
        screen.blit(bullet, (bullet_x, bullet_y))
        if f == 0 or f == 1:
            if rose_of_wind[f][1]:
                bullet_x -= speed
            else:
                bullet_x += speed
        else:
            if rose_of_wind[f][1]:
                bullet_y -= speed
            else:
                bullet_y += speed
        if bullet_x <= 0 or bullet_x >= width or bullet_y <= 0 or bullet_y >= height:
            bullet_x = wall_x
            bullet_y = wall_y
            if f == 3:
                f = 0
            else:
                f += 1
        sp[r] = coor
        if r == len(coords)-1:
            r = 0
        r += 1
        if coor == 1 and wx == -squar_size:
            screen.blit(head_up, (coords[0][0], coords[0][1]))
        elif coor == 1 and wx == squar_size:
            screen.blit(head_down, (coords[0][0], coords[0][1]))
        elif coor == 0 and wx == -squar_size:
            screen.blit(head_left, (coords[0][0], coords[0][1]))
        elif coor == 0 and wx == squar_size:
            screen.blit(head_right, (coords[0][0], coords[0][1]))

        for a in range(1, len(coords)):
            if sp[a] == 0:
                screen.blit(tail_snake, (coords[a][0], coords[a][1]))
            else:
                screen.blit(tail_snake_2, (coords[a][0], coords[a][1]))
        screen.blit(image_apple, (apple_x, apple_y))
        if coor == 0:
            x += wx
            coords.insert(0, (x, y))
        if coor == 1:
            y += wx
            coords.insert(0, (x, y))
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP and coor != 1 or e.key == pygame.K_UP and wx != squar_size and coor == 1:
                    coor = 1
                    wx = -squar_size
                    r = 0
                elif e.key == pygame.K_DOWN and coor != 1 or e.key == pygame.K_DOWN and wx != -squar_size and coor == 1:
                    coor = 1
                    wx = squar_size
                    r = 0
                elif e.key == pygame.K_RIGHT and coor != 0 or e.key == pygame.K_RIGHT and wx != -squar_size and coor == 0:
                    coor = 0
                    wx = squar_size
                    r = 0
                elif e.key == pygame.K_LEFT and coor != 0 or e.key == pygame.K_LEFT and wx != squar_size and coor == 0:
                    coor = 0
                    wx = -squar_size
                    r = 0
                elif e.key == pygame.K_r:
                    x = width // 2
                    y = height // 2
                    wx = squar_size
                    coor = 0
                    coords = [(x, y), (x - squar_size, y), (x - squar_size * 2, y)]
                    apple_x = random.randint(100, width - 100)
                    apple_y = random.randint(100, height - 100)
                    scoors = 0
                    sp = [0, 0, 0]
                    r = 0
                    continue
                elif e.key == pygame.K_l:
                    apple_x = random.randint(100, width - 100)
                    apple_y = random.randint(100, height - 100)
                elif e.key == pygame.K_c:
                    exit()
            elif e.type == pygame.QUIT:
                return
        snake_c = pygame.Rect(x, y, squar_size, squar_size)
        apple_c = pygame.Rect(apple_x, apple_y, squar_size, squar_size)
        if snake_c.colliderect(apple_c):
            apple_x = random.randint(100, width - 100)
            apple_y = random.randint(100, height - 100)
            scoors += 1
            speed += 1
            sp.append(0)
        else:
            coords.pop()
        snake_head_c = pygame.Rect(x, y, squar_size, squar_size)
        wall_s = pygame.Rect(wall_x, wall_y, squar_size, squar_size)
        bullet_s = pygame.Rect(bullet_x, bullet_y, squar_size, squar_size)
        if snake_head_c.colliderect(wall_s):
            return
        elif snake_head_c.colliderect(bullet_s):
            return
        for i in range(1, len(coords)):
            tail_c = pygame.Rect(coords[i][0], coords[i][1], squar_size, squar_size)
            if snake_head_c.colliderect(tail_c):
                return
            elif tail_c.colliderect(bullet_s):
                return
        if x <= 0:
            x = width
        elif x >= width:
            x = -35
        elif y >= height:
            y = -35
        elif y <= 0:
            y = height
        pygame.display.flip()
        time.sleep(0.20)


width = 500
height = 500
screen = pygame.display.set_mode((width, height))
font_1 = pygame.font.SysFont("Calibri", 52)
font_2 = font_1.render("Игра", False, (255, 255, 255))
while True:
    for l in pygame.event.get():
        if l.type == pygame.QUIT:
            exit(1)
        elif l.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (width // 2 - 52, height // 2 - 50):
                if pygame.mouse.get_pos() <= (width // 2 + 52, height // 2 + 50):
                    play()
                    width = 500
                    height = 500
                    screen = pygame.display.set_mode((width, height))
                    font_1 = pygame.font.SysFont("Calibri", 52)
                    font_2 = font_1.render("Игра", False, (255, 255, 255))
    screen.blit(font_2, (200, 200))
    pygame.display.flip()
