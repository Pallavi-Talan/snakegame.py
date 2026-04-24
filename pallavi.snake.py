import pygame
import random
import urllib.request
import io

pygame.init()
pygame.mixer.init()

# Function to load image from URL
def load_image(url):
    data = urllib.request.urlopen(url).read()
    image_file = io.BytesIO(data)
    return pygame.image.load(image_file)

# Function to load sound from URL
def load_sound(url):
    data = urllib.request.urlopen(url).read()
    sound_file = io.BytesIO(data)
    return pygame.mixer.Sound(sound_file)

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Load from Internet
snake_img = load_image("https://i.imgur.com/7yUvePI.png")
snake_img = pygame.transform.scale(snake_img, (20, 20))

food_img = load_image("https://i.imgur.com/6X4K6pB.png")
food_img = pygame.transform.scale(food_img, (20, 20))

eat_sound = load_sound("https://www.soundjay.com/button/sounds/button-16.wav")

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

font = pygame.font.SysFont("Arial", 25)
clock = pygame.time.Clock()

def game():
    x, y = 300, 200
    dx, dy = 0, 0

    snake = []
    length = 1

    food_x = random.randrange(0, WIDTH, 20)
    food_y = random.randrange(0, HEIGHT, 20)

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -20, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = 20, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -20
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, 20

        x += dx
        y += dy

        # Wall wrap
        if x >= WIDTH: x = 0
        if x < 0: x = WIDTH
        if y >= HEIGHT: y = 0
        if y < 0: y = HEIGHT

        head = [x, y]
        snake.append(head)

        if len(snake) > length:
            del snake[0]

        # Eat food
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH, 20)
            food_y = random.randrange(0, HEIGHT, 20)
            length += 1
            eat_sound.play()

        # Draw
        screen.blit(food_img, (food_x, food_y))

        for block in snake:
            screen.blit(snake_img, (block[0], block[1]))

        score_text = font.render("Score: " + str(length-1), True, WHITE)
        screen.blit(score_text, (10,10))

        pygame.display.update()
        clock.tick(10)

    pygame.quit()

game()
