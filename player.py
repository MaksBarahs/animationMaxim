import pygame
class Player():
    def __init__(self,screen):
        self.screen = screen
        self.screenrect = self.screen.get_rect()
        self.image = pygame.image.load("images/pygame_idle.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screenrect.midbottom

        self._x = float(self.rect.x)
        self._y = float(self.rect.y)
        self.IsJumping = False
        self.right = False
        self.left = False
        self.yisUp = False
        self.yisDown = False
        self.MaxJumpHeit = self.rect.y - 300
        self.MinJumpHeit = self.rect.y
    def Update(self):
        if self.right == True and self.rect.right < self.screenrect.right:
            self._x += 2.1
            self.image = pygame.image.load("images/pygame_right_2.png")
        elif self.left == True and self.rect.left > self.screenrect.left:
            self._x -= 2.1
            self.image = pygame.image.load("images/pygame_left_1.png")
        elif (self.right == False and self.left == False) or (self.right == True and self.left == True):
            self.image = pygame.image.load("images/pygame_idle.png")
        if self.IsJumping == True:
            if self.yisUp == True:
                self._y -= 2
                if self._y == self.MaxJumpHeit:
                    self.yisUp = False
                    self.yisDown = True
            if self.yisDown == True:
                self._y += 2
                if self._y == self.MinJumpHeit:
                    self.yisDown = False
                    self.IsJumping = False

        self.rect.x = self._x
        self.rect.y = self._y
    def Blitme(self):
        self.screen.blit(self.image,self.rect)

    def StartJumping(self):
        self.yisUp = True
        self.IsJumping = True