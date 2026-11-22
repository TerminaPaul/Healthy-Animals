import pygame


class Render:

    def __init__(self):
        self.screen = pygame.display.set_mode((4*200, 3*200))

    def afficher(self):
        self.screen.fill("White")
        self.screen.blit(pygame.image.load("Assets/ralsei.png"), (100, 100))
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Jeu")
    test = Render()
    while True:
        test.afficher()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
