import pygame
from os import path

class Interface():

    def __init__(self):
        self.configs()
        self.screen()

    def configs(self):
        self.fps = 60
        self.screen_size = (1280, 720)

    def screen(self):
        pygame.display.set_mode(self.screen_size)
        pygame.time.Clock().tick(self.fps)
        pygame.display.flip()

    def save_window(self):
        print("a")



class Jogo(Interface):

    def __init__(self):
        self.load_save()

    def new_save(self):
        if path.exists('./save0.json') == False:
            ... # Criar new save

        

    def load_save(self):
        super().__init__()
        super().save_window()




running = False
if __name__ == "__main__":
    running = True

Jogo().new_save()
while running == True:

    Jogo()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False