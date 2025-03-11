import pygame
import sys
import time
import random

# Difficulty settings
difficulty = 25

# Window size
frame_size_x = 1280
frame_size_y = 720

# Checks for errors encountered
check_errors = pygame.init()
if check_errors[1] > 0:
    print(
        f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Game Ular Sederhana')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10))
            * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2

game_state = MENU


# Game Over
def game_over():
    global game_state
    game_state = GAME_OVER
    my_font = pygame.font.SysFont('JetBrains Mono', 90)
    game_over_surface = my_font.render('YAHH MATI :(', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'JetBrains Mono', 20)
    show_score(1, white, 'JetBrains Mono', 30)
    show_options()
    pygame.display.flip()
    while game_state == GAME_OVER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    game_state = PLAYING
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


# Show options after game over
def show_options():
    my_font = pygame.font.SysFont('JetBrains Mono', 23)
    options_surface = my_font.render(
        'Tekan SPACE untuk restart atau ESC untuk keluar', True, white)
    options_rect = options_surface.get_rect()
    options_rect.midtop = (frame_size_x/2, frame_size_y/1.5)
    game_window.blit(options_surface, options_rect)


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont('JetBrains Mono', size)
    score_surface = score_font.render(
        'Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)


# Reset game state
def reset_game():
    global snake_pos, snake_body, food_pos, food_spawn, direction, change_to, score
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
    food_pos = [random.randrange(
        1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game_state == MENU:
                if event.key == pygame.K_SPACE:
                    game_state = PLAYING
            elif game_state == PLAYING:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    game_state = MENU
            elif game_state == GAME_OVER:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    game_state = PLAYING
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    if game_state == PLAYING:
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(
                1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        food_spawn = True

        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10 or snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
            game_over()

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(game_window, white, pygame.Rect(
            food_pos[0], food_pos[1], 10, 10))

        show_score(1, white, 'JetBrains Mono', 20)
    elif game_state == MENU:
        game_window.fill(black)
        show_score(0, red, 'JetBrains Mono', 50)
        my_font = pygame.font.SysFont('JetBrains Mono', 30)
        menu_text_surface = my_font.render(
            'Tekan SPACE untuk mulai', True, white)
        menu_text_rect = menu_text_surface.get_rect()
        menu_text_rect.midtop = (frame_size_x/2, frame_size_y/1.8)
        game_window.blit(menu_text_surface, menu_text_rect)

    elif game_state == GAME_OVER:
        game_over()

    pygame.display.update()
    fps_controller.tick(difficulty)
