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
        pygame.display.set_caption("Drops of Light")
        self.clock = pygame.time.Clock()
        self.running = True
        self.moves = None
        

    def run(self):
        self.menu_active = True
        while self.running:
            if self.menu_active:
                self.menu()
            else:
                self.handle_events()
                self.render()
                self.update()
            self.clock.tick(60)

    def menu(self):
        self.screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        play_text = font.render("Jogar(p)", True, BLACK)
        quit_text = font.render("Sair(q)", True, BLACK)
        self.screen.blit(play_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(quit_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.menu_active = False
                    self.select_level()
                elif event.key == pygame.K_q:
                    self.running = False

    def select_level(self):
        level = input("Escolha o nível: ")

        while level not in ['1', '2', '3', '4']:
            level = input("Escolha um nível valido: ")

        self.level = level_list[int(level)-1].copy()
        self.ia = GameState(self.level)
        self.screen.fill(WHITE)  # Clear the screen
        self.menu_active = False

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
                    print("Acabou a energia, vamos encerrar o jogo")
                    exit()
                
            else:
                print("Inposivel mover photon para ai")

            print()
            del self.moves[0]

            if len(self.moves) <= 1:
                self.moves = None
            
                
        else:
            if self.level is not None and self.level.verify_goal():
                self.menu_active = True
                self.level = None
                self.ia = None

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