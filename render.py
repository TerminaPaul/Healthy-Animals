import pygame


class Render:

    def __init__(self):
        self.screen = pygame.display.set_mode((16*100, 9*100))

    def render(self, player):
        self.screen.fill("White")

        self.screen.blit(pygame.image.load("Assets/ralsei.png"), (player.position[0], player.position[1]))
        pygame.display.flip()


if __name__ == '__main__':
    import player

    pygame.init()
    pygame.display.set_caption("Jeu")
    test = Render()
    while True:
        test.render(player.Player("render_test_player"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
