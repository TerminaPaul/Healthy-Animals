import pygame

import render
#import player


class Main:
    def __init__(self):
        self.running = True
        #self.player = player.Player

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("w")
                elif event.key == pygame.K_a:
                    print("a")
                elif event.key == pygame.K_s:
                    print("s")
                elif event.key == pygame.K_d:
                    print("d")

    def run(self):
        while self.running:
            self.event()
            jeu_render.afficher()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Healthy Animals")
    game = Main()
    jeu_render = render.Render()
    game.run()
