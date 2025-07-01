import pygame.key
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY, SHOT_SOUND
from code.Entity import Entity
from code.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.name = name
        if self.name == 'jogador1':
            self.animation_prefix = 'j1run'
            self.animation_attack = 'j1attack'
        elif self.name == 'jogador2':
            self.animation_prefix = 'j2run'
            self.animation_attack = 'j2attack'
        
        self.run_images = [
            pygame.image.load(f'./asset/{self.animation_prefix}{i}.png').convert_alpha()
            for i in range(1, 9)
        ]
        self.attack_images = [
            pygame.image.load(f'./asset/{self.animation_attack}{i}.png').convert_alpha() 
            for i in range(1, 8)]

        self.animation_index = 0
        self.animation_delay = 5
        self.frame_count = 0
        self.state = "run"
        self.surf = self.run_images[0]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        self.frame_count += 1
        if self.frame_count >= self.animation_delay:
            self.frame_count = 0
            self.animation_index += 1

            if self.state == "run":
                self.animation_index %= len(self.run_images)
                self.surf = self.run_images[self.animation_index]

            elif self.state == "attack":
                if self.animation_index < len(self.attack_images):
                    self.surf = self.attack_images[self.animation_index]
                else:
                    self.animation_index = 0
                    self.state = "run"
                    self.surf = self.run_images[0]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]
                SHOT_SOUND.play()
                self.state = "attack"
                self.animation_index = 0
                return PlayerShot(name=f'{self.name}fogo', position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
            return None
