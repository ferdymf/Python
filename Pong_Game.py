import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_COLOR = (0, 150, 255)
BALL_COLOR = (255, 0, 0)
FONT_COLOR = (255, 255, 0)
BACKGROUND_COLOR = (30, 30, 30)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

# Setup layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle dan Bola
paddle1 = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) //
                      2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 40, (HEIGHT - PADDLE_HEIGHT) //
                      2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# Kecepatan Bola
ball_speed_x = 5
ball_speed_y = 5

# Skor
score1 = 0
score2 = 0

# Font
font = pygame.font.Font(None, 74)

# Game loop


def game_loop():
    global ball_speed_x, ball_speed_y, score1, score2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Kontrol Paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= 5
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
            paddle1.y += 5
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= 5
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y += 5

        # Gerakan Bola
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Pantulan Bola
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed_x *= -1

        # Reset Bola jika keluar dari layar
        if ball.left <= 0:
            score2 += 1
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball_speed_x *= -1
        if ball.right >= WIDTH:
            score1 += 1
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball_speed_x *= -1

        # Menggambar
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, PADDLE_COLOR, paddle1)
        pygame.draw.rect(screen, PADDLE_COLOR, paddle2)
        pygame.draw.ellipse(screen, BALL_COLOR, ball)

        # Tampilkan Skor
        score_text = font.render(f"{score1}  {score2}", True, FONT_COLOR)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        # Garis tengah
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0),
                           (WIDTH // 2, HEIGHT))

        pygame.display.flip()
        pygame.time.delay(30)


# Memulai game
game_loop()
