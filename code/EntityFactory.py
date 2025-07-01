import random
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'fase1':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'fase1-{i}', (0, 0)))
                    list_bg.append(Background(f'fase1-{i}', (WIN_WIDTH, 0)))   

                return list_bg
            case 'fase2':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'fase2-{i}', (0, 0)))
                    list_bg.append(Background(f'fase2-{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'jogador1':
                return Player('jogador1', (10, WIN_HEIGHT / 2 - 30))
            case 'jogador2':
                return Player('jogador2', (10, WIN_HEIGHT / 2 + 30))
            case 'assassino1':
                enemy = Enemy('assassino1', (0, 0))
                enemy_height = enemy.surf.get_height()
                max_y = WIN_HEIGHT - enemy_height // 2
                min_y = enemy_height // 2
                enemy.rect.centerx = WIN_WIDTH + 10
                enemy.rect.centery = random.randint(min_y, max_y)
                return enemy
            case 'assassino2':
                enemy = Enemy('assassino2', (0, 0))
                enemy_height = enemy.surf.get_height()
                max_y = WIN_HEIGHT - enemy_height // 2
                min_y = enemy_height // 2
                enemy.rect.centerx = WIN_WIDTH + 10
                enemy.rect.centery = random.randint(min_y, max_y)
                return enemy