import pygame
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)

class Photon(pygame.sprite.Sprite):
    def __init__(self,  boder, colors, number, conected):
        super().__init__()
        self.colors = colors  # Array para armazenar as cores (R, G, B)
        self.boder = boder # Pode ser (C, R, G, B) = (0, 1, 2, 3)
        self.conected = conected
        self.number = number  # Número do fóton
        self.radius = 15
        self.font = pygame.font.Font(None, 24)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Superfície transparente
        self.rect = self.image.get_rect()
        self.update_color()
        self.update_number()

    def copy(self):
        return Photon(self.colors[:], self.boder, self.conected[:], self.number, self.position)

    def get_position(self, position):
        self.rect = self.image.get_rect(center = position)

    def update_color(self):
        # Calcula a cor do fundo com base nas cores armazenadas
        red = self.colors[0]
        green = self.colors[1]
        blue = self.colors[2]

        # Calcula a cor resultante da mistura das cores
        if red and green and blue:
            background_color = (255, 255, 255)  # White
        elif red and green:
            background_color = (255, 255, 0)  # Yellow
        elif red and blue:
            background_color = (255, 0, 255)  # Magenta
        elif green and blue:
            background_color = (0, 255, 255)  # Cyan
        elif red:
            background_color = (255, 0, 0)  # Red
        elif green:
            background_color = (0, 255, 0)  # Green
        elif blue:
            background_color = (0, 0, 255)  # Blue
        else:
            background_color = (128, 128, 128)  # Gray (sem cor)

        if self.boder == 0:
            boder_color = (0, 0, 0)  # Black
        elif self.boder == 1:
            boder_color = (150, 0, 0)  # Red
        elif self.boder == 2:
            boder_color = (0, 150, 0)  # Green
        elif self.boder == 3:
            boder_color = (0, 0, 150)  # Blue

        # Redesenha o círculo com a nova cor de fundo
        self.image.fill((0, 0, 0, 0))  # Limpa a superfície
        pygame.draw.circle(self.image, background_color, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, boder_color, (self.radius, self.radius), self.radius, 4)  # Desenha o círculo preto

        self.update_number()

    def update_number(self):
        text = self.font.render(str(self.number), True, BLACK)
        text_rect = text.get_rect(center=(self.radius, self.radius))  # Posiciona o texto no centro do círculo
        self.image.blit(text, text_rect)  # Desenha o texto no centro do círculo

    def posibility_move_to(self, photon2):
        for i in range(3):
            if (self.colors[i] == photon2.colors[i] or (self.colors[i] == 1 and i + 1 == photon2.boder)) and self.colors[i] != 0:
                return False

        return True 
    
    def move_to(self, photon2):
        check_color = False

        if photon2.number in self.conected:
            check_color = True
            check_color = self.posibility_move_to(photon2)

        else:
            print("Photons precisam estar conectados por uma linha")

        if check_color:
            for j in range(3):
                if self.colors[j] == 1:
                    photon2.colors[j] = 1

                self.colors[j] = 0

            photon2.update_color()
            self.update_color()

            return True
        
        return False
    
    def possibility_to_split(self):
        count_colors = 0

        for color in self.colors:
            if color == 1:
                count_colors += 1

        if count_colors > 1:
            return True
        
        return False
    
    def posibility_move_to_split(self, photon2, i):
        if (self.colors[i] == photon2.colors[i] or (self.colors[i] == 1 and i + 1 == photon2.boder)) and self.colors[i] != 0:
            return False

        return True 
    
    def move_to_split(self, photon2, i):
        check_color = False

        if photon2.number in self.conected:
            check_color = True
            check_color = self.posibility_move_to_split(photon2, i)

        else:
            print("Photons precisam estar conectados por uma linha")

        if check_color:
            photon2.colors[i] = 1
            self.colors[i] = 0

            photon2.update_color()
            self.update_color()

            return True
        
        return False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Board:
    def __init__(self, photons):
        self.photons = photons

        self.size = 200
        self.tilt_angle = 30  # Ângulo de inclinação em graus
        self.vertices = self.calculate_vertices()
        self.center = self.calculate_center()

        self.screen_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def copy(self):
        copied_photons = [photon.copy() for photon in self.photons]
        return Board(copied_photons)
    
    def calculate_vertices(self):
        vertices = []
        angle_step = 2 * math.pi / 6  # Dividindo o círculo em 6 partes iguais

        # Calcula as coordenadas dos vértices do polígono de 6 lados
        for i in range(6):
            angle = i * angle_step + math.radians(self.tilt_angle)  # Adiciona a inclinação ao ângulo
            x = SCREEN_WIDTH / 2 + self.size * math.cos(angle)
            y = SCREEN_HEIGHT / 2 + self.size * math.sin(angle)
            vertices.append((x, y))

        return vertices

    def calculate_center(self):
        # Calcula o ponto central do polígono
        center_x = sum(vertex[0] for vertex in self.vertices) / len(self.vertices)
        center_y = sum(vertex[1] for vertex in self.vertices) / len(self.vertices)
        return (center_x, center_y)

    def calculate_lines_to_outside(self):
        # Calcula as linhas que vão do centro do polígono para fora do polígono
        lines = []
        for i in range(len(self.vertices)):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % len(self.vertices)]
            
            # Calcula o ponto intermediário entre o centro e o vértice
            mid_point = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            
            # Calcula o vetor entre o ponto intermediário e o centro
            dx = self.center[0] - mid_point[0]
            dy = self.center[1] - mid_point[1]
            
            # Calcula o ponto final da linha
            p3 = (self.center[0] +  1.5 * dx, self.center[1] +  1.5 * dy)
            lines.append((mid_point, p3))
        return lines

    def draw_connections(self, surface):
        for photon in self.photons:
            photon_position = photon.rect.center

            for connected_photon_index in photon.conected:
                connected_photon = self.photons[connected_photon_index - 1]  # Os índices começam em 1
                connected_photon_position = connected_photon.rect.center

                pygame.draw.line(surface, LINE_COLOR, photon_position, connected_photon_position, 2)



    def draw(self, surface):
        photon_inx = 0

        for line in self.calculate_lines_to_outside():
            self.photons[photon_inx].get_position((int(line[1][0]), int(line[1][1])))
            photon_inx += 1

        for vertex in self.vertices:
            self.photons[photon_inx].get_position((int(vertex[0]), int(vertex[1])))
            photon_inx += 1

        for i in range(len(self.vertices)):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % len(self.vertices)]
            midpoint = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            self.photons[photon_inx].get_position(midpoint)
            photon_inx += 1

        self.photons[photon_inx].get_position(self.screen_center)

        self.draw_connections(surface)
        for photon in self.photons:
            photon.draw(surface)

    def draw_goal(self, surface):
        photon_inx = 0

        for line in self.calculate_lines_to_outside():
            self.photons[photon_inx].get_position((int(line[1][0]/3), int(line[1][1]/3)))
            photon_inx += 1

        for vertex in self.vertices:
            self.photons[photon_inx].get_position((int(vertex[0]/3), int(vertex[1]/3)))
            photon_inx += 1

        for i in range(len(self.vertices)):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % len(self.vertices)]
            midpoint = ((p1[0] + p2[0]) / 6, (p1[1] + p2[1]) / 6)
            self.photons[photon_inx].get_position(midpoint)
            photon_inx += 1

        self.photons[photon_inx].get_position((130, 100))

        self.draw_connections(surface)
        for photon in self.photons:
            photon.draw(surface)


class Level:
    def __init__(self, number, board, goal, energy):
        self.number = number  # Número do level
        self.board = board
        self.goal = goal
        self.energy = energy
        self.font = pygame.font.Font(None, 24)


    def copy(self):
        copied_board = self.board.copy()  # Suponha que a classe Board tenha um método copy()
        copied_goal = self.goal.copy()  # Suponha que a classe Goal tenha um método copy()
        return Level(self.number, copied_board, copied_goal, self.energy)
        
    def verify_goal(self):
        for i in range(19):
            if self.board.photons[i].colors != self.goal.photons[i].colors:
                return False
            
        return True

    def update_energy(self,lost, surface):
        self.energy -= lost

        text = self.font.render("Energy:" + str(self.energy), True, BLACK)
        text_rect = text.get_rect(topleft=(700, 20))
        surface.blit(text, text_rect)

        '''
        if self.energy == 0 and self.verify_goal != True:
            print("Perdeu level, vamos encerar o programa")
            return False
        '''
        return True
        
    def draw(self, surface):
        self.board.draw(surface) 
        self.goal.draw_goal(surface)
        text = self.font.render("Energy:" + str(self.energy), True, BLACK)
        text_rect = text.get_rect(topleft=(700, 20))
        surface.blit(text, text_rect)


    
