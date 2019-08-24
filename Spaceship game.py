import pygame
import random


def redraw_window(surface, player_position, poz, ship):
    surface.blit(poz, (0, 0))
    text = font.render("Score:" + str(score), 1, (255, 0, 0))
    surface.blit(text, (10, 10))
    surface.blit(ship, (player_position[0], player_position[1]))
    pygame.display.update()

    for enemy_position in enemy_positions:
        pygame.draw.rect(surface, (230, 230, 250), (enemy_position[0], enemy_position[1], sirina, duzina))

    pygame.display.update()


def collision(player_position, enemy_positions):
    for enemy_position in enemy_positions:
        if enemy_position[1] + duzina / 1.5 >= player_position[1] - duzina / 2 and enemy_position[1] - duzina / 2 <= \
                player_position[1] + duzina / 2 and enemy_position[0] + sirina / 2 >= player_position[
            0] - sirina / 2 and enemy_position[0] - sirina / 2 <= player_position[0] + sirina / 2:
            return True
    return False


def enemy_movement(enemy_positions, enemy_velocity):
    for enemy_position in enemy_positions:
        enemy_position[1] += enemy_velocity


def spawn_enemy():
    enemy_positions.append([random.randint(0, 500), 0])


def main():
    pygame.mixer.pre_init(44100,16,2,4096)
    pygame.init()

    global sirina, duzina, enemy_positions, font, score, win

    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Spaceship")
    font = pygame.font.SysFont("comicsans", 30, True)
    poz = pygame.image.load('poz.jpg')
    ship = pygame.image.load('brod1.png')

    player_position = [225, 300]
    sirina = 37
    duzina = 74
    vel = 9

    enemy_positions = []
    vel1 = 16

    score = 0

    pygame.mixer.music.load('Sunflower (Instrumental).mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1,5.3)

    run = True
    while run:

        score += 1
        value = random.random()
        if value > 0.80:
            spawn_enemy()

        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        enemy_movement(enemy_positions, vel1)

        redraw_window(win, player_position, poz, ship)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_position[0] > vel:
            player_position[0] -= vel
        if keys[pygame.K_RIGHT] and player_position[0] < 500 - sirina - vel:
            player_position[0] += vel

        if collision(player_position, enemy_positions):
            run = False

    while True:
        pygame.mixer.music.pause()
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        win.blit(poz, (0, 0))
        text1 = font.render("You died !", 1, (255, 0, 0))
        text0 = font.render("SCORE: "+str(score), 1, (255, 0, 0))
        text2 = font.render("Play again (R)", 1, (255, 0, 0))
        text3 = font.render("Quit (N)", 1, (255, 0, 0))
        win.blit(text1, (200, 140))
        win.blit(text0, (194, 200))
        win.blit(text2, (180, 260))
        win.blit(text3, (210, 290))
        pygame.display.update()
        a = pygame.key.get_pressed()
        if a[pygame.K_r]:
            main()
        elif a[pygame.K_n]:
            break

main()
pygame.quit()