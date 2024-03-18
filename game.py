import math
import pygame
import sys
from classes import Photon, Board, Level
from levellist import level_list

from ia import GameState
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Photon Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = level_list[0]
        self.ia = GameState(self.level)
        

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
            self.update()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Obtém a entrada do usuário para os fótons de origem e destino
        moves = self.ia.apply_move()
        
        if moves != None:
            time.sleep(2)
            #photon1_index = moves[0].number
            print("Photon de origem (1-19): ", moves[0])
            
            photon1 = self.level.board.photons[moves[0] - 1]
            
            time.sleep(2) 
            #photon2_index = moves[1].number
            print("Photon de destino (1-19): ", moves[1])
            
            photon2 = self.level.board.photons[moves[1] - 1] 

            check_color = False

            if moves[1] in photon1.conected:
                check_color = True
                check_color = photon1.posibility_move_to(photon2)

            else:
                print("Photons precisam estar conectados por uma linha")

            if check_color:
                for j in range(3):
                    if photon1.colors[j] == 1:
                        photon2.colors[j] = 1

                    photon1.colors[j] = 0

                photon2.update_color()
                photon1.update_color()

                if self.level.update_energy(1, self.screen) != True:
                    exit()

            else: 
                print("Imposivel colocar cor em photon de destino")

            # Atualiza a cor do fóton de destino com a cor do fóton de origem
                
        if self.level.verify_goal():
            next_level = self.level.number
            if next_level == 3:
                print("Fim de Jogo")
                time.sleep(20)
                exit()
            else:
                print("Proximo nivel")
                time.sleep(5)
                self.level = level_list[next_level]
                self.ia.updade_state(self.level)
                self.screen.fill(WHITE)  # Limpa a tela
                pygame.display.flip()



    def render(self):
        self.screen.fill(WHITE)
        self.level.board.draw(self.screen) 
        self.level.goal.draw_goal(self.screen)
        self.level.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
