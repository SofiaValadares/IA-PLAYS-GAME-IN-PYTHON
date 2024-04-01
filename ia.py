import heapq
from collections import deque
    
class GameState:
    """
    Represents the state of the game.

    Attributes:
        level (None or Level): The current level of the game.
        goals_index (list): The indices of the goal states.

    Methods:
        __init__(self, level): Initializes the GameState object.
        update_state(self, level): Updates the state of the game.
        close_to_goal(self, photon, move_to): Checks if moving the photon to a certain position brings it closer to the goal state.
        BreadthFirst(self): Performs a breadth-first search to find the next move.
        UniformCust(self, start, goal, board=None): Performs a uniform cost search to find the path from the start to the goal.
        next_possible(self, start, goal): Checks if there is a possible next move from the start to the goal.
        UniformCust2(self): Performs a modified uniform cost search to find the next move.
        heuristic_estimate(self, index): Estimates the cost to reach the goal state from a certain index.
        AStar(self): Performs an A* search to find the next move.
        apply_move(self): Applies the next move to the game.
    """

    def __init__(self, level):
        """
        Initializes the GameState object.

        Args:
            level (Level): The current level of the game.
        """
        self.level = None
        self.goals_index = []
        self.nodes_acessed = 0
        
        self.update_state(level)

    def update_state(self, level):
        """
        Updates the state of the game.

        Args:
            level (Level): The current level of the game.
        """
        self.level = level
        self.goals_index = []

        for index, photon in self.level.goal.photons.items():
            if photon.colors != [0, 0, 0]:
                self.goals_index.append(index)

    def close_to_goal(self, photon, move_to):
        """
        Checks if moving the photon to a certain position brings it closer to the goal state.

        Args:
            photon (int): The index of the photon.
            move_to (int): The index of the position to move the photon to.

        Returns:
            bool: True if moving the photon to the position brings it closer to the goal state, False otherwise.
        """
        board = self.level.board.photons
        goal = self.level.goal.photons

        if move_to not in self.goals_index:
            return False

        close = False

        for j in range(3):
            if board[photon].colors[j] == 1 and goal[move_to].colors[j] == 1:
                close = True
            elif board[photon].colors[j] == 1 and goal[move_to].colors[j] == 0:
                return False

        return close
    
    def next_possible(self, start, goal):
        """
        Checks if there is a possible next move from the start to the goal.

        Args:
            start (int): The index of the start position.
            goal (int): The index of the goal position.

        Returns:
            bool: True if there is a possible next move, False otherwise.
        """
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
                            return True

        if level_copy.verify_goal():
            return True
        
        return False
    
    def BreadthFirst(self):
        """
            Performs a breadth-first search to find the next move.

            Returns:
                list or None: The next move as a list of indices [start, goal], or None if no move is found.
        """
        
        board = self.level.board.photons

        for start, photon in board.items():
            if photon.colors != [0, 0, 0] and start not in self.goals_index:
                for end in self.goals_index:
                    if photon.colors_check(board[end]):
                        if self.close_to_goal(start, end):

                            visited = set()
                            queue = deque([(start, [start])])

                            while queue:
                                current, path = queue.popleft()

                                if current == end:
                                    if self.next_possible(start, end):
                                        return path
                                
                                visited.add(current)

                                for neighbor in board[current].connected:
                                    if neighbor not in visited:
                                        queue.append((neighbor, path + [neighbor]))
                                        visited.add(neighbor)
        return None


    def UniformCust(self, start, goal, board=None):
        """
        Performs a uniform cost search to find the path from the start to the goal.

        Args:
            start (int): The index of the start position.
            goal (int): The index of the goal position.
            board (dict): The board state. Defaults to None.

        Returns:
            list or None: The path from the start to the goal as a list of indices, or None if no path is found.
        """
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

    def UniformCust2(self):
        """
        Performs a modified uniform cost search to find the next move.

        Returns:
            list or None: The next move as a list of indices [start, goal], or None if no move is found.
        """
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
        """
        Estimates the cost to reach the goal state from a certain index.

        Args:
            index (int): The index of the goal state.

        Returns:
            int: The estimated cost to reach the goal state from the index.
        """
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
        """
        Performs an A* search to find the next move.

        Returns:
            list or None: The next move as a list of indices [start, goal], or None if no move is found.
        """
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
        """
        Applies the next move to the game.

        Returns:
            list or None: The next move as a list of indices [start, goal], or None if no move is found.
        """
        move1 = self.BreadthFirst()

        move2 = self.UniformCust2()
  

        move = None

        if move1 == move2:
            move = move1

        else:
            move = move2
        

        if self.level.verify_goal() == False and move is None:
            move = self.AStar()

        return move
