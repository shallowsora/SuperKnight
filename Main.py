"""
作者：浅空
日期：2021年04月22日
"""
import pygame
import os
import setting as s
import character


def load_all_images(directory, colorkey=(255, 0, 255), accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics


class Run(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("The Game")
        self.font = pygame.font.Font(None, 32)
        self.window = pygame.display.set_mode(s.size)
        self.running = True
        self.fps = 30
        self.key = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pos()
        self.pause = False
        s.GTX = load_all_images(os.path.join("sourcepack"))
        self.character = character.Character()
        self.character_group = pygame.sprite.Group(self.character)

    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run.game_over()
            elif event.type == pygame.KEYDOWN:
                self.key = pygame.key.get_pressed()
                self.game_pause(self.key)

    def update(self):
        self.character_group.update(self.key)
        self.character_group.draw(self.window)

    def game_pause(self, key):
        if key == pygame.K_ESCAPE:
            while not self.pause:
                text = self.font.render("Press ESC to continue", True, s.black, s.white)
                textrect = text.get_rect()
                textrect.center = s.width/2, s.height/2
                self.window.blit(text, textrect)
                self.event_check()

    def game_start(self):
        while self.running:
            self.event_check()
            self.update()
            pygame.display.update()

    @staticmethod
    def game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':
    run = Run()
    run.game_start()
