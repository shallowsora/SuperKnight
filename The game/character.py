"""
作者：浅空
日期：2021年04月22日
"""
import pygame
import setting as s


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()
        self.sprite_sheet = s.GTX['Knight']
        self.right_frame = []
        self.left_frame = []
        self.frame_index = 0
        self.load_from_sheet()
        self.image = self.right_frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.state = s.stand
        self.x_v = s.x_v
        self.y_v = s.y_v
        self.x_a = s.x_a
        self.max_x_v = s.max_x_v
        self.jump_v = s.jump_v
        self.gravity = s.gravity
        self.facing_right = True
        self.keys = pygame.key.get_pressed()

    def state_handle(self, keys):
        if self.state == s.stand:
            self.stand(keys)
        elif self.state == s.walk:
            self.walk(keys)
        elif self.state == s.jump:
            self.jump(keys)
        elif self.state == s.fall:
            self.fall(keys)
        # elif self.state == s.attack:
        #     self.attack(keys)

    def stand(self, keys):
        self.frame_index = 0
        self.x_v = 0
        self.y_v = 0
        self.gravity = s.gravity
        if keys[pygame.K_LEFT]:
            self.facing_right = False
            self.state = s.walk
        elif keys[pygame.K_RIGHT]:
            self.facing_right = True
            self.state = s.walk
        elif keys[pygame.K_SPACE]:
            self.state = s.jump
        else:
            self.state = s.stand

    def walk(self, keys):
        pass

    def jump(self, keys):
        pass

    def fall(self, keys):
        pass

    # def attack(self, keys):
    #     pass

    def update(self, keys):
        self.state_handle(keys)
        self.update_position()
        self.animation()

    def update_position(self):
        self.rect.x += self.x_v
        self.rect.y += self.y_v

    def animation(self):
        if self.facing_right:
            self.image = self.right_frame[self.frame_index]
        else:
            self.image = self.left_frame[self.frame_index]

    def get_image(self, x, y, w, h):
        image = pygame.Surface([w, h]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        image.set_colorkey(s.black)
        return image

    def load_from_sheet(self):
        self.left_frame.append(self.get_image(4000, 70, 200, 130))
        self.left_frame.append(self.get_image(80, 32, 15, 16))
        self.left_frame.append(self.get_image(99, 32, 15, 16))
        self.left_frame.append(self.get_image(114, 32, 15, 16))
        self.left_frame.append(self.get_image(144, 32, 16, 16))
        self.left_frame.append(self.get_image(130, 32, 14, 16))
        for frame in self.left_frame:
            new_image = pygame.transform.flip(frame, True, False)
            self.right_frame.append(new_image)
