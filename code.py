import pygame
import pygame.freetype
from pygame.locals import *
pygame.init()

bg = pygame.image.load("resized-image-Promo.jpeg")
bgg = pygame.transform.scale(bg,(900,720))

yellow = (255, 255, 0)
red = (255, 0, 0)
white = (255,255,255)
black = (0,0,0)
width = 720

bg1 = pygame.image.load("frame_0_delay-0.07s.gif")
bg2 = pygame.transform.scale(bg1, (900,720))

screen_width = 900
screen_height = 720
screen=pygame.display.set_mode((screen_width, screen_height))



font_size = 40


title_font = pygame.font.Font("Absolute_Zero.otf",50)
button_font = pygame.font.Font("Absolute_Zero.otf",font_size)
titleX = 270
titleY = 250
startX = 340
startY = 340

#Title
def show_title(x,y):
    title = title_font.render("Car Game", True, white)
    screen.blit(title,(270, y))


back_g = True

def background():
    i = 0
    while back_g:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        
        screen.fill((0,0,0))
        screen.blit(bg2, (0, i))
        screen.blit(bg2, (0, width + i))

        if i == - width:
            screen.blit(bg2, (0, width + i))
            i = 0

        i -= 3

        pygame.display.update()

start_text = button_font.render("Start", True, red)
quit_text = button_font.render("Quit", True, white)
class Button():
    def __init__(self, x, y, text):
        self.text = text
        self.rect = self.text.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self):
        action = False
        #Get mouse position
        pos = pygame.mouse.get_pos()

        #Check Mouseover
        if self.rect.collidepoint(pos):
            font_size = 50
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Draw Buttons
        screen.blit(self.text, (self.rect.x, self.rect.y))
        return action


#Button Instances
start_button = Button(340,460, start_text)
quit_button = Button(370,560, quit_text)



def main_menu():
    menu = True
    while menu == True:
        screen.blit(bgg,(0,0))
        show_title(titleX,titleY)
        if start_button.draw() == True:
            #menu = False
            background()
            

        if quit_button.draw():
            pygame.quit()



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        pygame.display.update()


run = True
def game_loop():
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen.fill(black)
                    main_menu()
                    pygame.display.update()
        pygame.display.update()
        


main_menu()
game_loop()




