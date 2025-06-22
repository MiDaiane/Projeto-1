import pygame
from pygame import Surface, Rect

W_WIDTH = 963
W_HEIGHT = 538
# Inicializar o Módulo do PyGame
pygame.init()
print('setup start')
# Criação de janela do pygame
window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# Carregar imagem e gerar uma superfície
bg_surf: Surface = pygame.image.load('./asset/fundo_menu.png').convert_alpha()
player1_surf: Surface = pygame.image.load('./asset/samurai_flecha.png').convert_alpha()

# Obter o retângulo da superfície
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=100, top=100)

# Desenhar na janela (window)
window.blit(source=bg_surf, dest=bg_rect)
window.blit(source=player1_surf, dest=player1_rect)

# Atualizar a janela
pygame.display.flip()

# Colocar um relógio no nosso jogo
clock = pygame.time.Clock()

# Carregar musica e deixar ela tocando
pygame.mixer_music.load('./asset/musica_menu.flac')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.3)
print('setup end')
print('loop start')
while True:
    clock.tick(140)  # esse loop está acontecendo 30 vezes por segundo
    # print(f'{clock.get_fps() :.0f}')  # executar o print o fps
    window.blit(source=bg_surf, dest=bg_rect)
    window.blit(source=player1_surf, dest=player1_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
        pass
#
