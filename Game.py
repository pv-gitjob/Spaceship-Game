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
    obstacle1.draw()
    obstacle2.draw()
    score_text = font.render('Score: ' + str(score), 1, (255, 255, 255))
    window.blit(score_text, (10, 10))
    pygame.display.update()


player = Player()
increment = 0.8
speed1= 3
speed2 = 1.5
obstacle1 = Obstacle(3)
obstacle2 = Obstacle(1.5)
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

    obstacle1.move()
    if obstacle1.x < - obstacle1.width:
        score += 1
        speed1 += increment ** 1.1
        obstacle1 = Obstacle(speed1)

    if player.mask().overlap(obstacle1.mask(), (int(round(obstacle1.x - player.x)), int(round(obstacle1.y - player.y)))):
        run = False

    obstacle2.move()
    if obstacle2.x < - obstacle2.width:
        score += 1
        speed2 += increment ** 2
        obstacle2 = Obstacle(speed2)

    if player.mask().overlap(obstacle2.mask(), (int(round(obstacle2.x - player.x)), int(round(obstacle2.y - player.y)))):
        run = False

    draw_window()

pygame.quit()
