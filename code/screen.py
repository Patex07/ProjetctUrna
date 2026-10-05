import sys
import pygame.draw
from pygame import Surface, Rect
from pygame.font import Font

from code.CONST import WIN_HEIGHT, WIN_WIDTH, RECT_WIDTH, RECT_HEIGHT, COLOR_GRAY, COLOR_LIGHT_GRAY, NUMBER_HEIGHT, \
    IMAGE_WIDTH, COLOR_BLACK, TEXT_NUMBER_SIZE


class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.fullscreen = False

        self.canvas_urna = pygame.Surface((RECT_WIDTH,RECT_HEIGHT))

    def trade_fullscreen(self):
        self.fullscreen = not self.fullscreen

        if self.fullscreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.trade_fullscreen()

            #desenho na tela real
            self.canvas_urna.fill (COLOR_LIGHT_GRAY)
            self.screen.fill(COLOR_GRAY)

            self.menu_text(TEXT_NUMBER_SIZE - 10, 'SEU VOTO PARA', COLOR_BLACK, (140, 20))


            #voto
            #pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (RECT_WIDTH/2 - 210, 40, 420, 60), width=2)
            self.menu_text(TEXT_NUMBER_SIZE, 'PRESIDENTE', COLOR_BLACK, (RECT_WIDTH/2 - 160, 80), True)

            #imagens
            pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (IMAGE_WIDTH, 150, 240, 280), width=2)
            pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (IMAGE_WIDTH + 60, 432, 180, 220), width=2)

            #numeros
            #pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (160, NUMBER_HEIGHT, 200, 50), width=2)
            self.menu_text(TEXT_NUMBER_SIZE, 'Número: ', COLOR_BLACK, (140, NUMBER_HEIGHT))
            pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (320, NUMBER_HEIGHT, 40, 50), width=2)
            self.menu_text(TEXT_NUMBER_SIZE, '0', COLOR_BLACK, (340, NUMBER_HEIGHT + 25), True)
            pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (370,  NUMBER_HEIGHT, 40, 50), width=2)
            self.menu_text(TEXT_NUMBER_SIZE, '0', COLOR_BLACK, (390,  NUMBER_HEIGHT + 25 ), True)

            #nome
            #pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (160, (NUMBER_HEIGHT * 1.5), 200, 50), width=2)
            self.menu_text(TEXT_NUMBER_SIZE, 'Nome: ', COLOR_BLACK, (140, NUMBER_HEIGHT * 1.8))
            #pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (320, NUMBER_HEIGHT * 1.5, 40, 50), width=2)
            self.menu_text(TEXT_NUMBER_SIZE, 'Nome TESTE AbC', COLOR_BLACK, (320, NUMBER_HEIGHT * 1.8))

            #vice_candidato
            #pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (140, (NUMBER_HEIGHT * 2.2), 200, 50), width=2)
            self.menu_text(TEXT_NUMBER_SIZE, 'Vice-Presidente: ', COLOR_BLACK, (140, NUMBER_HEIGHT * 2.4))
            #pygame.draw.rect(self.canvas_urna, COLOR_GRAY, (420, NUMBER_HEIGHT * 2.2, 40, 50), width=2)
            self.menu_text(TEXT_NUMBER_SIZE, 'Nome TESTE AbC', COLOR_BLACK, (420, NUMBER_HEIGHT * 2.4))

            #pega o tamanho atual da tela e se tiver em tela cheia redimensiona
            width_actually, height_actually = self.screen.get_size()
            new_width = int(width_actually * 0.9)
            new_height= int(height_actually * 0.9)
            scale_canvas = pygame.transform.smoothscale(self.canvas_urna,(new_width,new_height))
            rect = scale_canvas.get_rect(center = (width_actually/2,height_actually/2))
            self.screen.blit(scale_canvas,rect)


            pygame.display.flip()
        pygame.quit()
        sys.exit()
    def menu_text(self, text_size: int, text: str, text_color: tuple,text_center_pos: tuple,text_position_center : bool = False):
        text_font: Font = pygame.font.Font('./Assets/arial/ARIAL.ttf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        if text_position_center:
            text_rect: Rect =  text_surf.get_rect(center =text_center_pos)
        else:
            text_rect: Rect = text_surf.get_rect(topleft =text_center_pos)
        self.canvas_urna.blit(source=text_surf, dest=text_rect)