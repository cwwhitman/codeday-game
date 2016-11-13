import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.health = 2
        self.alive = True

        self.rect = pygame.Rect(x, y, 30, 30)
        self.vel_x, self.vel_y = 0.0, 0.0
        self.accl_x, self.accl_y = 0.0, 0.0

        self.on_ground = True
        self.jump_frame = 1
        self.jkp = False

        self.frames_jumped = 0 

        self.frames_walked = 0


    def spawn(self, x, y):
        self.alive = True
        self.pos_x, self.pos_y = x, y

    def jump(self):
        self.frames_jumped += 1
        self.vel_y += -5/self.frames_jumped
        self.on_ground = False
        if self.frames_jumped > 15:
            self.frames_jumped = 0

    def apply_accel(self):
        self.vel_x += self.accl_x
        self.vel_y += self.accl_y
        if self.on_ground:
            self.vel_y, self.accl_y = 0.0, 0.0

    def apply_vel(self):
        self.rect.move_ip(self.vel_x, self.vel_y)

    def gravity(self):
        if not self.on_ground:
            self.accl_y = 1

    def move_to_floor(self, correction):
        self.rect.move_ip(0, -correction)
        self.accl_y, self.vel_y, self.on_ground = 0, 0, True

    def walk(self, dir):
        self.frames_walked += 1
        if self.frames_walked < 10:
            speed = (self.frames_walked//1.25)*dir
        else:
            speed = 8*dir
        self.rect.move_ip(speed, 0)

    def update(self):
        pygame.event.pump()
        k = pygame.key.get_pressed()
        if k[pygame.K_UP] and (self.frames_jumped or self.on_ground):
            self.jump()
        else:
            self.frames_jumped = 0
        if k[pygame.K_LEFT]:
            self.walk(-1)
        elif k[pygame.K_RIGHT]:
            self.walk(1)
        else:
            self.frames_walked = 0



        self.apply_accel()
        self.apply_vel()
        self.gravity()

#tommy = Player()
#def show():
#    print tommy.vel_x, tommy.vel_y
#    print tommy.accl_x, tommy.accl_y
