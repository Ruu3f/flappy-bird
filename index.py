import pygame
import random

pygame.init()

screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

bird_width = 50
bird_height = 50
bird_x = 50
bird_y = 225

gravity = 0.5
velocity = 0

pipe_width = 50
pipe_gap = 150
pipe_x = screen_width
pipe_height = random.randint(100, 300)
pipe_top_y = pipe_height - pipe_gap
pipe_bottom_y = pipe_height + pipe_gap

score = 0
font = pygame.font.Font(None, 36)

speed_changer_width = 20
speed_changer_height = 200
speed_changer_x = screen_width - 50
speed_changer_y = (screen_height - speed_changer_height) / 2

def draw():
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (bird_x, bird_y, bird_width, bird_height))
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, 0, pipe_width, pipe_top_y))
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, pipe_bottom_y, pipe_width, screen_height - pipe_bottom_y))

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), (speed_changer_x, speed_changer_y, speed_changer_width, speed_changer_height))

    speed_bar_pos = int((game_speed - 10) / 100 * (speed_changer_height - speed_changer_width)) + speed_changer_y
    speed_bar_rect = pygame.Rect(speed_changer_x, speed_bar_pos, speed_changer_width, speed_changer_width)
    pygame.draw.rect(screen, (255, 255, 255), speed_bar_rect)

    plus_text = font.render("-", True, (255, 255, 255))
    minus_text = font.render("+", True, (255, 255, 255))
    plus_rect = plus_text.get_rect(midtop=(speed_changer_x + speed_changer_width/2, speed_changer_y))
    minus_rect = minus_text.get_rect(midbottom=(speed_changer_x + speed_changer_width/2, speed_changer_y + speed_changer_height))
    screen.blit(plus_text, plus_rect)
    screen.blit(minus_text, minus_rect)

    speed_text = font.render("Speed: " + str(game_speed), True, (255, 255, 255))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))

    speed_rect = speed_text.get_rect(midleft=(20, screen_height - 25))
    score_rect = score_text.get_rect(midright=(screen_width - 20, screen_height - 25)) 

    screen.blit(speed_text, speed_rect)
    screen.blit(score_text, score_rect)

    pygame.display.update()

clock = pygame.time.Clock()
game_speed = 50
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            velocity = -10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            game_speed += 10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            game_speed -= 10
            if game_speed < 10:
                game_speed = 10
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[0] > speed_changer_x and event.pos[0] < speed_changer_x + speed_changer_width and event.pos[1] > speed_changer_y and event.pos[1] < speed_changer_y + speed_changer_height:
                game_speed = int((event.pos[1] - speed_changer_y) / speed_changer_height * 100) + 10
                if game_speed > 100:
                    game_speed = 100
                elif game_speed < 10:
                    game_speed = 10

    bird_y += velocity
    velocity += gravity

    pipe_x -= 5

    if bird_y < 0:
        bird_y += 5
    elif bird_y + bird_height > screen_height:
        bird_y -= 5

    if pipe_x < -pipe_width:
        pipe_x = screen_width
        pipe_height = random.randint(100, 300)
        pipe_top_y = pipe_height - pipe_gap
        pipe_bottom_y = pipe_height + pipe_gap
        score += 1
    elif pipe_x < bird_x + bird_width and pipe_x + pipe_width > bird_x:
        if bird_y < pipe_top_y or bird_y + bird_height > pipe_bottom_y:
            pygame.quit()
            quit()

    draw()

    clock.tick(game_speed)
