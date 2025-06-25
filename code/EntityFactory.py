#!/usr/bin/python
# -*- coding: utf-8 -*-
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
                for i in range(7):  # level1bg images number
                    list_bg.append(Background(f'fase1-{i}', (0, 0)))
                    list_bg.append(Background(f'fase1-{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'fase2':
                list_bg = []
                for i in range(5):  # level2bg images number
                    list_bg.append(Background(f'fase2-{i}', (0, 0)))
                    list_bg.append(Background(f'fase2-{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'jogador1':
                return Player('jogador1', (10, WIN_HEIGHT / 2 - 30))
            case 'jogador2':
                return Player('jogador2', (10, WIN_HEIGHT / 2 + 30))
            case 'assassino1':
                return Enemy('assassino1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'assassino2':
                return Enemy('assassino2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
