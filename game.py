import pygame
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
        self.moves = None
        

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
        if self.moves is None:
            self.moves = self.ia.apply_move()
        
        if self.moves != None:
            time.sleep(1)
            print("Photon de origem (1-19): ", self.moves[0])
                
            photon1 = self.level.board.photons[self.moves[0]]

            time.sleep(1) 
            print("Photon de destino (1-19): ", self.moves[1])
                
            photon2 = self.level.board.photons[self.moves[1]] 
                
            if photon1.move_to(photon2, self.moves[1]):
                if self.level.update_energy(1, self.screen) != True:
                    print("Acabou a energia, vamos encerar o jogo")
                    exit()
                
            else:
                print("Inposivel mover photon para ai")

            print()
            del self.moves[0]

            if len(self.moves) <= 1:
                self.moves = None
            
                
        else:
            if self.level.verify_goal():
                next_level = self.level.number
                if next_level == 21:
                    print("Fim de Jogo")
                    time.sleep(5)
                    exit()
                else:
                    print("Proximo nivel")
                    time.sleep(3)
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