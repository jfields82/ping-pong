import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Create paddles
player_paddle = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Score
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

def move_paddle(paddle, up=True):
    if up and paddle.top > 0:
        paddle.y -= PADDLE_SPEED
    if not up and paddle.bottom < HEIGHT:
        paddle.y += PADDLE_SPEED

def move_ball(ball):
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    # Score points
    if ball.left <= 0:
        opponent_score += 1
        ball_reset()
    if ball.right >= WIDTH:
        player_score += 1
        ball_reset()

def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move_paddle(player_paddle, up=True)
    if keys[pygame.K_s]:
        move_paddle(player_paddle, up=False)

    # Simple AI for opponent
    if opponent_paddle.centery < ball.centery:
        move_paddle(opponent_paddle, up=False)
    else:
        move_paddle(opponent_paddle, up=True)

    move_ball(ball)

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Display score
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH//4, 20))
    screen.blit(opponent_text, (3*WIDTH//4, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(60)