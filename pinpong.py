from pygame import *

window = display.set_mode((700,500))
display.set_caption('pinpong')

clock = time.Clock()
FPS = 90

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move1(self):
        if key_pressed[K_s] and self.rect.y <=300:
            self.rect.y += self.speed
        if key_pressed[K_w] and self.rect.y >=5:
            self.rect.y -= self.speed
    def move2(self):
        if key_pressed[K_DOWN] and self.rect.y <=300:
            self.rect.y += self.speed
        if key_pressed[K_UP] and self.rect.y >=5:
            self.rect.y -= self.speed

speed_x = 3
speed_y = 3

finish = False

class Ball(GameSprite):
    def move_ball(self):
        global speed_x, speed_y, finish
        if finish != True:
            self.rect.x += speed_x
            self.rect.y += speed_y
        if ball.rect.y > 450 or self.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > 650 or self.rect.x < 0:
            finish = True
        if sprite.collide_rect(stick1, ball) or sprite.collide_rect(stick2, ball):
            speed_x *= -1

ball = Ball('eyeball.png', 325, 250, 50, 50, 0)
background = transform.scale(image.load('forest.jpg'),(700,500))
stick1 = GameSprite('sprite.png', 0, 0, 25, 200, 7)
stick2 = GameSprite('sprite.png', 675, 0, 25, 200, 7)

game = True
finish = False

while game:

    key_pressed = key.get_pressed()
    for i in event.get():

        if i.type == QUIT:
            game = False

    window.blit( background , (0,0))
    stick1.reset()
    stick2.reset()

    ball.reset()
    ball.move_ball()

    stick1.move1()
    stick2.move2()

    clock.tick(FPS)
    display.update()
