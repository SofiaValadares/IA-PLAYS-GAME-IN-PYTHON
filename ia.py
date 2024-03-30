import heapq
    
class GameState:
    def __init__(self, level):
        self.level = None
        self.goals_index = []
        
        self.updade_state(level)

    def updade_state(self, level):
        self.level = level
        self.goals_index = []

        for index, photon in self.level.goal.photons.items():
            if photon.colors != [0, 0, 0]:
                self.goals_index.append(index)


    # Verifica se mover o photon para certa posicao nos deixa mais perto do goal state
    def close_to_goal(self, phothon, move_to):
        board = self.level.board.photons
        goal = self.level.goal.photons

        if move_to not in self.goals_index:
            return False

        close = False

        for j in range(3):
            if board[phothon].colors[j] == 1 and goal[move_to].colors[j] == 1:
                close = True
                

            elif board[phothon].colors[j] == 1 and goal[move_to].colors[j] == 0:
                return False

        return close


    #Busca entre os visinhos de goal se algum deles pode nos deixar mais perto do goal state
    def BreadthFirst(self):
        board = self.level.board.photons

        for index, photon in board.items():
            if photon.colors != [0, 0, 0] and index not in self.goals_index: # Se o photon esta vazio não faz a verificação

                for neighbors in photon.connected:
                    if neighbors in self.goals_index: # Se o vizinho não é um local de goal state não continua
                        if photon.posibility_move_to(board[neighbors], neighbors):
                            if self.close_to_goal(index, neighbors):
                                return [index, neighbors]
                            
        # Caso não ache goal nos vizinhos retorna None
        return None

    def UniformCust(self, start, goal, board = None):
        
        if board is None:
            board = self.level.board.photons 

        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {}
        cost_so_far = {start: 0}

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                return path

            for next_node in board[current].connected:
                if next_node == goal or next_node not in self.goals_index:
                    if board[current].connected_to(next_node) and board[start].colors_check(board[next_node]):
                        new_cost = cost_so_far[current] + 1  
                        if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                            cost_so_far[next_node] = new_cost
                            priority = new_cost 
                            heapq.heappush(frontier, (priority, next_node))
                            came_from[next_node] = current


        return None 

    def next_possible(self, start, goal):
        level_copy = self.level.copy()
        board_copy = level_copy.board.photons

        for i in range(3):
            if board_copy[start].colors[i] == 1:
                board_copy[goal].colors[i] = 1

            board_copy[start].colors[i] = 0
         
        for i, photon in board_copy.items():
            if photon.colors != [0, 0, 0] and i not in self.goals_index:
                for j in self.goals_index:
                    if photon.colors_check(board_copy[j]):
                        if self.close_to_goal(i, j):
                            path = self.UniformCust(i, j, board_copy)

                            if path is not None:
                                return True

        if level_copy.verify_goal():
            return True
        
        return False


    def UniformCust2(self):
        board = self.level.board.photons 
        move = None

        for index, photon in board.items():
            if photon.colors != [0, 0, 0] and index not in self.goals_index:
                for goal in self.goals_index:
                    if self.close_to_goal(index, goal):
                        new_move = self.UniformCust(index, goal)
                         
                        if new_move is not None:
                            if self.next_possible(index, goal):
                                if move is None:
                                    move = new_move
                                elif len(move) >= len(new_move):
                                    move = new_move

        if move is not None:
            return move
        
        return None
    
    def heuristic_estimate(self, index):
        goal = self.level.board.photons[index]
        save_colors = goal.colors
        goal.colors = [0, 0, 0]
        board = self.level.goal.photons
        cust = 0

        for i, photon in board.items():
            if i not in self.goals_index:
                if photon.colors_check(goal):
                    if self.close_to_goal(i, index):
                        path = self.UniformCust(i, index)

                        if path is not None:
                            cust_new = len(path) - 1

                            if cust == 0 or cust > cust_new:
                                cust = cust_new

                    
        goal.colors = save_colors
        return cust
                    
    
    def AStar(self):
        board = self.level.board.photons

        cust_less = None
        move = None

        for index1 in self.goals_index:
            for index2 in self.goals_index:
                if index1 != index2:
                    if self.close_to_goal(index1, index2):
                        if board[index1].colors_check(board[index2]):
                            move_test = self.UniformCust(index1, index2)

                            if move_test is not None:
                                next_cust = self.heuristic_estimate(index1)

                                if next_cust != 0:
                                    cust = len(move_test) - 1 + next_cust
                                    if move is None:
                                        move = move_test
                                        cust_less = cust
                                    elif cust_less > cust:
                                        move = move_test
                                        cust_less = cust     

        return move
    
    def apply_move(self):
        move = self.BreadthFirst()
        

        if move is None:
            move = self.UniformCust2()

        if self.level.verify_goal() == False and move is None:
            move = self.AStar()
            

        return move







        

