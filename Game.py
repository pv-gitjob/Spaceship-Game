import os
import pygame
import random

windowWidth = 500
windowHeight = 400

pygame.init()
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Learning PyGame - Praveen Vandeyar")

ship_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "spaceship.png")).convert_alpha(), (60, 20))
meteor_image = [
    pygame.transform.scale(pygame.image.load(os.path.join("images", "meteor1.png")).convert_alpha(), (20, 20)),
    pygame.transform.scale(pygame.image.load(os.path.join("images", "meteor2.png")).convert_alpha(), (20, 20)),
    pygame.transform.scale(pygame.image.load(os.path.join("images", "meteor3.png")).convert_alpha(), (20, 20)),
    pygame.transform.scale(pygame.image.load(os.path.join("images", "meteor4.png")).convert_alpha(), (20, 20))]

class Player:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 60
        self.height = 20
        self.speed = 5
        self.image = ship_image

    def move(self, x, y):
        self.x += x
        self.y += y

    def mask(self):
        return pygame.mask.from_surface(self.image)

    def draw(self):
        window.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, speed):
        self.x = windowWidth
        self.y = windowHeight * random.random()
        self.width = 20
        self.height = 20
        self.speed = speed
        self.image = meteor_image[random.randint(0, 3)]

    def draw(self):
        window.blit(self.image, (self.x, self.y))

    def mask(self):
        return pygame.mask.from_surface(self.image)

    def move(self):
        self.x -= self.speed


score = 0
font = pygame.font.SysFont("comicsans", int(round(windowHeight / 15)), True)


def draw_window():
    window.fill((0, 0, 0))
    player.draw()
    obstacle.draw()
    score_text = font.render('Score: ' + str(score), 1, (255, 255, 255))
    name_text = font.render('Praveen Vandeyar', 1, (100, 100, 100))
    window.blit(score_text, (10, 10))
    window.blit(name_text, (windowWidth - 190, 10))
    pygame.display.update()


player = Player()
speed = 4
obstacle = Obstacle(speed)
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.speed:
        player.move(-player.speed, 0)

    if keys[pygame.K_RIGHT] and player.x < windowWidth - player.speed:
        player.move(player.speed, 0)

    if keys[pygame.K_UP] and player.y > player.speed:
        player.move(0, -player.speed)

    if keys[pygame.K_DOWN] and player.y < windowHeight - player.speed:
        player.move(0, player.speed)

    obstacle.move()
    if obstacle.x < - obstacle.width:
        score += 1
        speed += 0.5
        obstacle = Obstacle(speed)

    if player.mask().overlap(obstacle.mask(), (int(round(obstacle.x - player.x)), int(round(obstacle.y - player.y)))):
        run = False

    draw_window()

pygame.quit()
