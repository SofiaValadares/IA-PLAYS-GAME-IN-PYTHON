import pygame
from classes import Photon, Board, Level
from levellist import photons_empty, level_list
from collections import deque

class GameState:
    def __init__(self, level):
        self.level = level
        self.p = 0

    def updade_state(self, level):
        self.level = level
    
    def get_p(self):
        self.p = 0

        while(self.level.board.photons[self.p].colors == [0, 0, 0]):
            self.p += 1

            if self.p >= 18:
                break

            if self.is_goal_state():
                self.p += 1

            if self.p >= 18:
                break

    def get_goals(self):
        goals_possible = []
        p_colors = self.level.board.photons[self.p].colors
        for photon in self.level.goal.photons:
            check = True
            if photon.colors != [0, 0, 0] and self.level.board.photons[photon.number - 1].colors != photon.colors:
                for i in range(3):
                    if photon.colors[i] == 0 and p_colors[i] == 1:
                        check = False
                        break
            else:
                check = False
            
            if check:
                goals_possible.append(photon)

        return goals_possible
    
    def path_move(self, goal):
        start = self.level.board.photons[self.p]
        photons = self.level.board.photons

        parent = {}
        # Fila para armazenar os fótons a serem visitados
        queue = deque([start])
        # Marca o fóton de partida como visitado
        visited = set()
        visited.add(start.number)

        while queue:
            current = queue.popleft()
            
            # Se o fóton atual for o destino, reconstrua o caminho
            if current.number == goal.number:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent.get(current.number)
                    
                return list(reversed(path))
            
            # Para cada vizinho do fóton atual
            for photon in photons:
                if photon.number == current.number:
                    for neighbor_id in photon.conected:
                        # Se o vizinho ainda não foi visitado
                        if neighbor_id not in visited and photon.posibility_move_to(photons[neighbor_id-1]):
                            # Marque-o como visitado, adicione-o à fila e defina seu pai como o fóton atual
                            visited.add(neighbor_id)
                            queue.append(photons[neighbor_id-1])
                            parent[neighbor_id] = current
        
        # Se não for possível alcançar o destino a partir do ponto de partida
        return None

    def less_move(self):
        self.get_p()
        goals_possible = self.get_goals()
        path = None
        
        for goal in goals_possible:
            path_test = self.path_move(goal)

            if path == None:
                path = path_test
            elif len(path) > len(path_test):
                path = path_test

        return path
        
    def get_goals_split(self, i):
        goals_possible = []
        p_colors = self.level.board.photons[self.p].colors[i]
        for photon in self.level.goal.photons:
            check = True
            if photon.colors != [0, 0, 0] and self.level.board.photons[photon.number - 1].colors[i] != photon.colors[i]:
                    if photon.colors[i] == 0 and p_colors == 1:
                        check = False
            else:
                check = False
            
            if check:
                goals_possible.append(photon)

        return goals_possible

    def path_move_split(self, goal, i):
        start = self.level.board.photons[self.p]
        photons = self.level.board.photons

        parent = {}
        # Fila para armazenar os fótons a serem visitados
        queue = deque([start])
        # Marca o fóton de partida como visitado
        visited = set()
        visited.add(start.number)

        while queue:
            current = queue.popleft()
            
            # Se o fóton atual for o destino, reconstrua o caminho
            if current.number == goal.number:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent.get(current.number)
                    
                return list(reversed(path))
            
            # Para cada vizinho do fóton atual
            for photon in photons:
                if photon.number == current.number:
                    for neighbor_id in photon.conected:
                        # Se o vizinho ainda não foi visitado
                        if neighbor_id not in visited and photon.posibility_move_to_split(photons[neighbor_id-1], i):
                            # Marque-o como visitado, adicione-o à fila e defina seu pai como o fóton atual
                            visited.add(neighbor_id)
                            queue.append(photons[neighbor_id-1])
                            parent[neighbor_id] = current
        
        # Se não for possível alcançar o destino a partir do ponto de partida
        return None
    
    def less_move_split(self, i):
        self.get_p()
        goals_possible = self.get_goals_split(i)
        path = None
        
        for goal in goals_possible:
            path_test = self.path_move_split(goal, i)

            if path == None:
                path = path_test
            elif len(path) > len(path_test):
                path = path_test

        return path
    
    def apply_move(self):
        path = self.less_move() 

        if path is not None:
            return [path[0].number, path[1].number]
        
        else:
            frist_color = 0
            for i in range(3):
                if self.level.board.photons[self.p].colors[i] == 1:
                    frist_color = i
                    break

            path = self.less_move_split(frist_color)

            if path is not None:
                return [self.p+1, 20 + frist_color, path[1].number]
            
            return None

    def is_goal_state(self):
        check_goal = False

        for i in range(3):
            if self.level.board.photons[self.p].colors[i] == self.level.goal.photons[self.p].colors[i] and self.level.board.photons[self.p].colors[i] == 1:
                check_goal = True
            elif self.level.board.photons[self.p].colors[i] != self.level.goal.photons[self.p].colors[i] and self.level.board.photons[self.p].colors[i] == 1:
                check_goal = False
                break
            
        return check_goal







        

