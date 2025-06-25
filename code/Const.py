# C
import pygame

c_GREEN_FLUORESCENT = (57, 255, 20)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'fase1-0': 0,
    'fase1-1': 1,
    'fase1-2': 2,
    'fase1-3': 3,
    'fase1-4': 4,
    'fase1-5': 5,
    'fase1-6': 6,
    'fase2-0': 0,
    'fase2-1': 1,
    'fase2-2': 2,
    'fase2-3': 3,
    'fase2-4': 4,
    'fase2-5': 5,
    'fase2-6': 6,
    'fase2-7': 7,
    'jogador1': 3,
    'tiro_jogador1': 1,
    'jogador2': 3,
    'tiro_jogador2': 3,
    'assassino1': 1,
    'tiro_assassino1': 5,
    'assassino2': 1,
    'tiro_assassino2': 2,
}

ENTITY_HEALTH = {
    'fase1-0': 999,
    'fase1-1': 999,
    'fase1-2': 999,
    'fase1-3': 999,
    'fase1-4': 999,
    'fase1-5': 999,
    'fase1-6': 999,
    'fase2-0': 999,
    'fase2-1': 999,
    'fase2-2': 999,
    'fase2-3': 999,
    'fase2-4': 999,
    'fase2-5': 999,
    'fase2-6': 999,
    'fase2-7': 999,
    'jogador1': 300,
    'tiro_jogador1': 1,
    'jogador2': 300,
    'tiro_jogador2': 1,
    'assassino1': 50,
    'tiro_assassino1': 1,
    'assassino2': 60,
    'tiro_assassino2': 1,
}

ENTITY_DAMAGE = {
    'fase1-0': 0,
    'fase1-1': 0,
    'fase1-2': 0,
    'fase1-3': 0,
    'fase1-4': 0,
    'fase1-5': 0,
    'fase1-6': 0,
    'fase2-0': 0,
    'fase2-1': 0,
    'fase2-2': 0,
    'fase2-3': 0,
    'fase2-4': 0,
    'fase2-5': 0,
    'fase2-6': 0,
    'fase2-7': 0,
    'jogador1': 1,
    'tiro_jogador1': 25,
    'jogador2': 1,
    'tiro_jogador2': 20,
    'assassino1': 1,
    'tiro_assassino1': 20,
    'assassino2': 1,
    'tiro_assassino2': 15,
}

ENTITY_SCORE = {
    'fase1-0': 0,
    'fase1-1': 0,
    'fase1-2': 0,
    'fase1-3': 0,
    'fase1-4': 0,
    'fase1-5': 0,
    'fase1-6': 0,
    'fase2-0': 0,
    'fase2-1': 0,
    'fase2-2': 0,
    'fase2-3': 0,
    'fase2-4': 0,
    'fase2-5': 0,
    'fase2-6': 0,
    'fase2-7': 0,
    'jogador1': 0,
    'tiro_jogador1': 0,
    'jogador2': 0,
    'tiro_jogador2': 0,
    'assassino1': 100,
    'tiro_assassino1': 0,
    'assassino2': 125,
    'tiro_assassino2': 0,
}

ENTITY_SHOT_DELAY = {
    'jogador1': 20,
    'jogador2': 15,
    'assassino1': 100,
    'assassino2': 200,
}

# M
MENU_OPTION = ('NOVO JOGO - UM JOGADOR',
               'NOVO JOGO - DOIS JOGADORES',
               'NOVO JOGO - COMPETITIVO',
               'PONTUAÇÃO',
               'SAIR')

# P
PLAYER_KEY_UP = {'jogador1': pygame.K_UP,
                 'jogador2': pygame.K_w}
PLAYER_KEY_DOWN = {'jogador1': pygame.K_DOWN,
                   'jogador2': pygame.K_s}
PLAYER_KEY_LEFT = {'jogador1': pygame.K_LEFT,
                   'jogador2': pygame.K_a}
PLAYER_KEY_RIGHT = {'jogador1': pygame.K_RIGHT,
                    'jogador2': pygame.K_d}
PLAYER_KEY_SHOOT = {'jogador1': pygame.K_RCTRL,
                    'jogador2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s
# W
WIN_WIDTH = 1020
WIN_HEIGHT = 572

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
