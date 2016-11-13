import pygame
import joinGame

WHITE = (255, 255, 255)

buttons = ['res/startgamee.png']
title = 'title.png'

class Background(pygame.sprite.Sprite):

    def __init__(self):
        """ Constructor function """
 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('res/scaledbg.png')

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

class MenuButton(pygame.sprite.Sprite):

    def __init__(self, button):
        """Constructor"""

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(buttons[button])

        self.rect = self.image.get_rect()
        self.rect.y = 200
        self.rect.x = 400
    
def main():
    pygame.init()
    screen = pygame.display.set_mode([900, 450])

    pygame.display.set_caption('Menu')

    backgroundSprites = pygame.sprite.Group()
    activeSprites = pygame.sprite.Group()

    background = Background()
    backgroundSprites.add(background)

    clock = pygame.time.Clock()

    done = False

    startGameButton = MenuButton(0)
    activeSprites.add(startGameButton)

    while not done:

        event = pygame.event.poll()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if startGameButton.rect.collidepoint(pygame.mouse.get_pos()):
                    joinGame.main()
                    pygame.quit()

        elif event.type == pygame.QUIT:
            done = True
            
        screen.fill(WHITE)
 
        backgroundSprites.draw(screen)
        activeSprites.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    
