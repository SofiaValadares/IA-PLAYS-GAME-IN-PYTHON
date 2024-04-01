import pygame
import math


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)
GRAY = (128, 128, 128)

pygame.init()

class Photon(pygame.sprite.Sprite):
    def __init__(self, border, colors, connected):
        super().__init__()
        self.colors = colors  # Array para armazenar as cores (R, G, B)
        self.border = border # Pode ser (C, R, G, B) = (0, 1, 2, 3)
        self.connected = connected
        self.radius = 15
        self.font = pygame.font.Font(None, 24)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Superfície transparente
        self.rect = self.image.get_rect()
        

    def get_position(self, position):
        self.rect = self.image.get_rect(center = position)

    def copy(self):
        new_photon = Photon(self.border, self.colors[:], self.connected)
        return new_photon

    def update_color(self, number):
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

        if self.border == 0:
            border_color = (0, 0, 0)  # Black
        elif self.border == 1:
            border_color = (150, 0, 0)  # Red
        elif self.border == 2:
            border_color = (0, 150, 0)  # Green
        elif self.border == 3:
            border_color = (0, 0, 150)  # Blue

        # Redesenha o círculo com a nova cor de fundo
        self.image.fill((0, 0, 0, 0))  # Limpa a superfície
        pygame.draw.circle(self.image, background_color, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, border_color, (self.radius, self.radius), self.radius, 4)  # Desenha o círculo preto

        self.update_number(number)

    def update_number(self, number):
        text = self.font.render(str(number), True, BLACK)
        text_rect = text.get_rect(center=(self.radius, self.radius))  # Posiciona o texto no centro do círculo
        self.image.blit(text, text_rect)  # Desenha o texto no centro do círculo

    def connected_to(self, index):
        if index in self.connected:
            return True
        
        return False
    
    def colors_check(self, photon2):
        for i in range(3):
            if self.colors[i] == 1 and (photon2.colors[i] == 1 or i + 1 == photon2.border):
                return False
            
        return True
                 

    def posibility_move_to(self, photon2, index):
        check = self.connected_to(index)

        if check:
            check = self.colors_check(photon2)

        return check
    
    def move_to(self, photon2, index):
        check_color = self.posibility_move_to(photon2, index)

        if check_color:
            for j in range(3):
                if self.colors[j] == 1:
                    photon2.colors[j] = 1

                self.colors[j] = 0

            photon2.update_color(index)
            self.update_color(index)

            return True
        
        return False

    def draw(self, surface, number):
        surface.blit(self.image, self.rect)

        self.update_color(number)

class Board:
    """
    Represents a game board.

    Attributes:
    - photons (dict): A dictionary of photons on the board.
    - size (int): The size of the board.
    - tilt_angle (float): The tilt angle of the board in degrees.
    - vertices (list): The vertices of the board polygon.
    - center (tuple): The center point of the board polygon.
    - screen_center (tuple): The center point of the screen.
    - font (pygame.font.Font): The font used for rendering text.

    Methods:
    - copy(): Creates a copy of the board.
    - calculate_vertices(): Calculates the vertices of the board polygon.
    - calculate_center(): Calculates the center point of the board polygon.
    - calculate_lines_to_outside(): Calculates the lines from the center of the board polygon to the outside.
    - draw_connections(surface): Draws connections between photons on the board.
    - draw(surface): Draws the board and photons on the surface.
    - draw_goal(surface): Draws the goal state of the board on the surface.
    """

    def __init__(self, photons):
        self.photons = photons

        self.size = 200
        self.tilt_angle = 30  # Ângulo de inclinação em graus
        self.vertices = self.calculate_vertices()
        self.center = self.calculate_center()

        self.screen_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.font = pygame.font.Font(None, 24)

    def copy(self):
        """
        Creates a copy of the board.

        Returns:
        - Board: A new instance of the Board class with the same photons as the original board.
        """
        copy_photonts = {}

        for index, photon in self.photons.items():
            copy_photonts[index] = photon.copy()

        return Board(copy_photonts)
    
    def calculate_vertices(self):
        """
        Calculates the vertices of the board polygon.

        Returns:
        - list: A list of tuples representing the coordinates of the vertices.
        """
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
        """
        Calculates the center point of the board polygon.

        Returns:
        - tuple: A tuple representing the coordinates of the center point.
        """
        # Calcula o ponto central do polígono
        center_x = sum(vertex[0] for vertex in self.vertices) / len(self.vertices)
        center_y = sum(vertex[1] for vertex in self.vertices) / len(self.vertices)
        return (center_x, center_y)

    def calculate_lines_to_outside(self):
        """
        Calculates the lines from the center of the board polygon to the outside.

        Returns:
        - list: A list of tuples representing the start and end points of the lines.
        """
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
        """
        Draws connections between photons on the board.

        Parameters:
        - surface (pygame.Surface): The surface to draw on.
        """
        for photon in self.photons.values():
            photon_position = photon.rect.center

            for connected_photon_index in photon.connected:
                connected_photon = self.photons[connected_photon_index]  # Os índices começam em 1
                connected_photon_position = connected_photon.rect.center

                pygame.draw.line(surface, LINE_COLOR, photon_position, connected_photon_position, 2)

    def draw(self, surface):
        """
        Draws the board and photons on the surface.

        Parameters:
        - surface (pygame.Surface): The surface to draw on.
        """
        photon_inx = 1

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

        for i, photon in self.photons.items():
            photon.draw(surface, i)

    def draw_goal(self, surface):
        """
        Draws the goal state of the board on the surface.

        Parameters:
        - surface (pygame.Surface): The surface to draw on.
        """
        photon_inx = 1

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

        for i, photon in self.photons.items():
            photon.draw(surface, i)


class Level:
    def __init__(self, number, board, goal, energy):
        self.number = number  # Número do level
        self.board = board
        self.goal = goal
        self.energy = energy
        self.font = pygame.font.Font(None, 24)

    def copy(self):
        copy_board = self.board.copy()
        return Level(self.number, copy_board, self.goal, self.energy)

        
    def verify_goal(self):
        for i, _ in self.goal.photons.items():
            if self.board.photons[i].colors != self.goal.photons[i].colors:
                return False
            
        return True

    def update_energy(self,lost, surface):
        self.energy -= lost

        text = self.font.render("Energy:" + str(self.energy), True, BLACK)
        text_rect = text.get_rect(topleft=(700, 20))
        surface.blit(text, text_rect)

        return True
        
    def draw(self, surface):
        self.board.draw(surface) 
        self.goal.draw_goal(surface)
        text = self.font.render("Energy:" + str(self.energy), True, BLACK)
        text_rect = text.get_rect(topleft=(700, 20))
        surface.blit(text, text_rect)


    
