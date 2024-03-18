import pygame
from classes import Photon, Board, Level

# Inicialize o pygame
pygame.init()

# Inicialize o módulo de fonte do pygame
pygame.font.init()

photons_empty = [
            Photon(0, [0, 0, 0], 1, [16, 10, 11]),
            Photon(0, [0, 0, 0], 2, [11, 17, 12]),
            Photon(0, [0, 0, 0], 3, [12, 18, 7]),
            Photon(0, [0, 0, 0], 4, [7, 13, 8]),
            Photon(0, [0, 0, 0], 5, [8, 14, 9]),
            Photon(0, [0, 0, 0], 6, [9, 15, 10]),
            Photon(0, [0, 0, 0], 7, [4, 3, 13, 18]),
            Photon(0, [0, 0, 0], 8, [4, 5, 13, 14]),
            Photon(0, [0, 0, 0], 9, [5, 6, 14, 15]),
            Photon(0, [0, 0, 0], 10, [1, 6, 15, 16]),
            Photon(0, [0, 0, 0], 11, [1, 2, 16, 17]),
            Photon(0, [0, 0, 0], 12, [3, 2, 17, 18]),
            Photon(0, [0, 0, 0], 13, [4, 7, 8, 19]),
            Photon(0, [0, 0, 0], 14, [5, 8, 9, 19]),
            Photon(0, [0, 0, 0], 15, [6, 9, 10, 19]),
            Photon(0, [0, 0, 0], 16, [1, 10, 11, 19]),
            Photon(0, [0, 0, 0], 17, [2, 11, 12, 19]),
            Photon(0, [0, 0, 0], 18, [3, 7, 12, 19]),
            Photon(0, [0, 0, 0], 19, [13, 14, 15, 16, 17, 18]),
            ]
board1 = Board( photons = [
            Photon(0, [0, 0, 0], 1, [16, 10, 11]),
            Photon(0, [0, 0, 0], 2, [11, 17, 12]),
            Photon(0, [0, 0, 0], 3, [12, 18, 7]),
            Photon(0, [0, 0, 0], 4, [7, 13, 8]),
            Photon(0, [0, 0, 0], 5, [8, 14, 9]),
            Photon(0, [0, 0, 0], 6, [9, 15, 10]),
            Photon(0, [0, 1, 0], 7, [4, 3, 13, 18]),
            Photon(0, [0, 0, 1], 8, [4, 5, 13, 14]),
            Photon(0, [0, 0, 1], 9, [5, 6, 14, 15]),
            Photon(0, [1, 0, 0], 10, [1, 6, 15, 16]),
            Photon(0, [1, 0, 0], 11, [1, 2, 16, 17]),
            Photon(0, [0, 1, 0], 12, [3, 2, 17, 18]),
            Photon(0, [0, 0, 0], 13, [4, 7, 8, 19]),
            Photon(0, [0, 0, 1], 14, [5, 8, 9, 19]),
            Photon(0, [0, 0, 0], 15, [6, 9, 10, 19]),
            Photon(0, [1, 0, 0], 16, [1, 10, 11, 19]),
            Photon(0, [0, 0, 0], 17, [2, 11, 12, 19]),
            Photon(0, [0, 1, 0], 18, [3, 7, 12, 19]),
            Photon( 0, [0, 0, 0], 19, [13, 14, 15, 16, 17, 18]),
            ])

goal1 = Board( photons = [
            Photon(0, [0, 0, 0], 1, [16, 10, 11]),
            Photon(0, [0, 0, 0], 2, [11, 17, 12]),
            Photon(0, [0, 0, 0], 3, [12, 18, 7]),
            Photon(0, [0, 0, 0], 4, [7, 13, 8]),
            Photon(0, [0, 0, 0], 5, [8, 14, 9]),
            Photon(0, [0, 0, 0], 6, [9, 15, 10]),
            Photon(0, [0, 0, 0], 7, [4, 3, 13, 18]),
            Photon(0, [0, 0, 0], 8, [4, 5, 13, 14]),
            Photon(0, [0, 0, 0], 9, [5, 6, 14, 15]),
            Photon(0, [0, 0, 0], 10, [1, 6, 15, 16]),
            Photon(0, [0, 0, 0], 11, [1, 2, 16, 17]),
            Photon(0, [0, 0, 0], 12, [3, 2, 17, 18]),
            Photon(0, [0, 1, 1], 13, [4, 7, 8, 19]),
            Photon(0, [0, 0, 0], 14, [5, 8, 9, 19]),
            Photon(0, [1, 0, 1], 15, [6, 9, 10, 19]),
            Photon(0, [0, 0, 0], 16, [1, 10, 11, 19]),
            Photon(0, [1, 1, 0], 17, [2, 11, 12, 19]),
            Photon(0, [0, 0, 0], 18, [3, 7, 12, 19]),
            Photon( 0, [1, 1, 1], 19, [13, 14, 15, 16, 17, 18]),
            ])

board = Board( photons = [
            Photon(0, [0, 0, 0], 1, [16, 10, 11]),
            Photon(0, [0, 0, 0], 2, [11, 17, 12]),
            Photon(0, [0, 0, 0], 3, [12, 18, 7]),
            Photon(0, [0, 0, 0], 4, [7, 13, 8]),
            Photon(0, [0, 0, 0], 5, [8, 14, 9]),
            Photon(0, [0, 0, 0], 6, [9, 15, 10]),
            Photon(0, [0, 0, 0], 7, [4, 3, 13, 18]),
            Photon(0, [0, 0, 0], 8, [4, 5, 13, 14]),
            Photon(0, [0, 0, 0], 9, [5, 6, 14, 15]),
            Photon(0, [0, 0, 0], 10, [1, 6, 15, 16]),
            Photon(0, [0, 0, 0], 11, [1, 2, 16, 17]),
            Photon(0, [0, 0, 0], 12, [3, 2, 17, 18]),
            Photon(0, [0, 0, 0], 13, [4, 7, 8, 19]),
            Photon(0, [0, 0, 0], 14, [5, 8, 9, 19]),
            Photon(0, [0, 0, 0], 15, [6, 9, 10, 19]),
            Photon(0, [0, 0, 0], 16, [1, 10, 11, 19]),
            Photon(0, [0, 0, 0], 17, [2, 11, 12, 19]),
            Photon(0, [0, 0, 0], 18, [3, 7, 12, 19]),
            Photon( 0, [0, 0, 0], 19, [13, 14, 15, 16, 17, 18]),
            ])

board2 = Board( photons = [
            Photon(1, [0, 0, 0], 1, [16, 10, 11]),
            Photon(0, [0, 0, 0], 2, [11, 17, 12]),
            Photon(2, [0, 0, 0], 3, [12, 18, 7]),
            Photon(0, [0, 0, 0], 4, [7, 13, 8]),
            Photon(3, [0, 0, 0], 5, [8, 14, 9]),
            Photon(0, [0, 0, 0], 6, [9, 15, 10]),
            Photon(2, [0, 0, 1], 7, [4, 3, 13, 18]),
            Photon(3, [0, 1, 0], 8, [4, 5, 13, 14]),
            Photon(3, [1, 0, 0], 9, [5, 6, 14, 15]),
            Photon(1, [0, 0, 1], 10, [1, 6, 15, 16]),
            Photon(1, [0, 1, 0], 11, [1, 2, 16, 17]),
            Photon(2, [1, 0, 0], 12, [3, 2, 17, 18]),
            Photon(0, [0, 0, 0], 13, [4, 7, 8, 19]),
            Photon(3, [1, 1, 0], 14, [5, 8, 9, 19]),
            Photon(0, [0, 0, 0], 15, [6, 9, 10, 19]),
            Photon(1, [0, 1, 1], 16, [1, 10, 11, 19]),
            Photon(0, [0, 0, 0], 17, [2, 11, 12, 19]),
            Photon(2, [1, 0, 1], 18, [3, 7, 12, 19]),
            Photon( 0, [0, 0, 0], 19, [13, 14, 15, 16, 17, 18]),
            ])

goal1 = Board( photons = [
            Photon(0, [0, 0, 0], 1, [16, 10, 11]),
            Photon(0, [0, 0, 0], 2, [11, 17, 12]),
            Photon(0, [0, 0, 0], 3, [12, 18, 7]),
            Photon(0, [0, 0, 0], 4, [7, 13, 8]),
            Photon(0, [0, 0, 0], 5, [8, 14, 9]),
            Photon(0, [0, 0, 0], 6, [9, 15, 10]),
            Photon(0, [0, 0, 0], 7, [4, 3, 13, 18]),
            Photon(0, [0, 0, 0], 8, [4, 5, 13, 14]),
            Photon(0, [0, 0, 0], 9, [5, 6, 14, 15]),
            Photon(0, [0, 0, 0], 10, [1, 6, 15, 16]),
            Photon(0, [0, 0, 0], 11, [1, 2, 16, 17]),
            Photon(0, [0, 0, 0], 12, [3, 2, 17, 18]),
            Photon(0, [0, 1, 1], 13, [4, 7, 8, 19]),
            Photon(0, [0, 0, 0], 14, [5, 8, 9, 19]),
            Photon(0, [1, 0, 1], 15, [6, 9, 10, 19]),
            Photon(0, [0, 0, 0], 16, [1, 10, 11, 19]),
            Photon(0, [1, 1, 0], 17, [2, 11, 12, 19]),
            Photon(0, [0, 0, 0], 18, [3, 7, 12, 19]),
            Photon( 0, [1, 1, 1], 19, [13, 14, 15, 16, 17, 18]),
            ])

goal2 = Board( photons = [
            Photon(1, [0, 0, 0], 1, [16, 10, 11]),
            Photon(0, [0, 0, 0], 2, [11, 17, 12]),
            Photon(2, [0, 0, 0], 3, [12, 18, 7]),
            Photon(0, [0, 0, 0], 4, [7, 13, 8]),
            Photon(3, [0, 0, 0], 5, [8, 14, 9]),
            Photon(0, [0, 0, 0], 6, [9, 15, 10]),
            Photon(2, [0, 0, 0], 7, [4, 3, 13, 18]),
            Photon(3, [0, 0, 0], 8, [4, 5, 13, 14]),
            Photon(3, [0, 0, 0], 9, [5, 6, 14, 15]),
            Photon(1, [0, 0, 0], 10, [1, 6, 15, 16]),
            Photon(1, [0, 0, 0], 11, [1, 2, 16, 17]),
            Photon(2, [0, 0, 0], 12, [3, 2, 17, 18]),
            Photon(0, [0, 1, 1], 13, [4, 7, 8, 19]),
            Photon(3, [1, 1, 0], 14, [5, 8, 9, 19]),
            Photon(0, [1, 0, 1], 15, [6, 9, 10, 19]),
            Photon(1, [0, 1, 1], 16, [1, 10, 11, 19]),
            Photon(0, [1, 1, 0], 17, [2, 11, 12, 19]),
            Photon(2, [1, 0, 1], 18, [3, 7, 12, 19]),
            Photon(2, [0, 0, 0], 19, [13, 14, 15, 16, 17, 18]),
            ])

board3 = Board( photons = [
            Photon(3, [0, 0, 0], 1, [16, 10, 11]),
            Photon(3, [0, 0, 0], 2, [11, 17, 12]),
            Photon(0, [0, 1, 0], 3, [12, 18, 7]),
            Photon(3, [0, 0, 0], 4, [7, 13, 8]),
            Photon(3, [0, 0, 0], 5, [8, 14, 9]),
            Photon(0, [0, 0, 0], 6, [9, 15, 10]),
            Photon(3, [0, 0, 0], 7, [4, 3, 13, 18]),
            Photon(0, [0, 0, 0], 8, [4, 5, 13, 14]),
            Photon(3, [0, 0, 0], 9, [5, 6, 14, 15]),
            Photon(3, [0, 0, 0], 10, [1, 6, 15, 16]),
            Photon(0, [0, 0, 0], 11, [1, 2, 16, 17]),
            Photon(3, [0, 0, 0], 12, [3, 2, 17, 18]),
            Photon(0, [0, 0, 0], 13, [4, 7, 8, 19]),
            Photon(0, [0, 0, 0], 14, [5, 8, 9, 19]),
            Photon(3, [0, 0, 0], 15, [6, 9, 10, 19]),
            Photon(0, [0, 0, 0], 16, [1, 10, 11, 19]),
            Photon(0, [0, 0, 0], 17, [2, 11, 12, 19]),
            Photon(3, [0, 0, 0], 18, [3, 7, 12, 19]),
            Photon(2, [0, 0, 0], 19, [13, 14, 15, 16, 17, 18]),
            ])

goal3 = Board(photons = [
            Photon(3, [0, 0, 0], 1, [16, 10, 11]),
            Photon(3, [0, 0, 0], 2, [11, 17, 12]),
            Photon(0, [0, 0, 0], 3, [12, 18, 7]),
            Photon(3, [0, 0, 0], 4, [7, 13, 8]),
            Photon(3, [0, 0, 0], 5, [8, 14, 9]),
            Photon(0, [0, 1, 0], 6, [9, 15, 10]),
            Photon(3, [0, 0, 0], 7, [4, 3, 13, 18]),
            Photon(0, [0, 0, 0], 8, [4, 5, 13, 14]),
            Photon(3, [0, 0, 0], 9, [5, 6, 14, 15]),
            Photon(3, [0, 0, 0], 10, [1, 6, 15, 16]),
            Photon(0, [0, 0, 0], 11, [1, 2, 16, 17]),
            Photon(3, [0, 0, 0], 12, [3, 2, 17, 18]),
            Photon(0, [0, 0, 0], 13, [4, 7, 8, 19]),
            Photon(0, [0, 0, 0], 14, [5, 8, 9, 19]),
            Photon(3, [0, 0, 0], 15, [6, 9, 10, 19]),
            Photon(0, [0, 0, 0], 16, [1, 10, 11, 19]),
            Photon(0, [0, 0, 0], 17, [2, 11, 12, 19]),
            Photon(3, [0, 0, 0], 18, [3, 7, 12, 19]),
            Photon( 3, [0, 0, 0], 19, [13, 14, 15, 16, 17, 18]),
            ])

            
level_list = [
    Level(1, board1, goal1, 9),
    Level(2, board2, goal2, 8),
    Level(3, board3, goal3, 11),
]