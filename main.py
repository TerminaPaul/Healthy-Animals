import pygame

import render
import player


class Main:
    def __init__(self):
        self.running = True
        self.player = player.Player(name="test")
        self.render = render.Render()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(dy=-1)
        if keys[pygame.K_a]:
            self.player.move(dx=-1)
        if keys[pygame.K_s]:
            self.player.move(dy=1)
        if keys[pygame.K_d]:
            self.player.move(dx=1)

    def run(self):
        while self.running:
            self.event()
            self.render.render(self.player)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Healthy Animals")
    game = Main()
    game.run()
