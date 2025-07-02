import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, C_GREEN_FLUORESCENT, MENU_OPTION, C_WHITE, C_YELLOW

class Menu:
    def __init__(self, window):
        self.window = window
        self.menu = pygame.image.load('./asset/menu.png').convert_alpha()
        self.rect = self.menu.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/musica_menu.flac')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.menu, dest=self.rect)
            font_path = './asset/formato_letra.ttf'
            title_font = pygame.font.Font(font_path, 60)

            self.menu_text(60, "Corra, Atire e Fuja", C_GREEN_FLUORESCENT, (WIN_WIDTH / 2, 60), shadow=True, font=title_font)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 150 + 28 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 150 + 28 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, shadow: bool = False, font: pygame.font.Font = None):
        text_font = pygame.font.SysFont("courier new", text_size, bold=True)
        if font is None:
            text_font = pygame.font.SysFont("courier new", text_size, bold=True)
        else:
            text_font = font

        if shadow:
            shadow_surf = text_font.render(text, True, (0, 0, 0))
            shadow_rect = shadow_surf.get_rect(center=(text_center_pos[0] + 2, text_center_pos[1] + 2))
            self.window.blit(shadow_surf, shadow_rect)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
