import time
import random
from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_s_x, cell_s_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.c_s_x = cell_s_x
        self.c_s_y = cell_s_y
        self.win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()
        

    def __create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                    col.append(self.__draw_cell(i, j, Cell(self.win)))
            self._cells.append(col)

    def __draw_cell(self, i, j, cell = None):
        if cell == None:
            cell = self._cells[i][j]

        x_t_left = self.x1 + i * self.c_s_x
        y_t_left = self.y1 + j * self.c_s_y
        cell.draw(x_t_left, y_t_left, x_t_left + self.c_s_x, y_t_left + self.c_s_y)      
        self.__animate()
        return cell
    
    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.01)

    def __break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        entrance = self.__draw_cell(0,0)
        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        exit.has_bottom_wall = False
        exit = self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i , j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if i > 0 and not self._cells[i -1][j].visited:
                to_visit.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
        
            next_id = random.randrange(len(to_visit))
            next = to_visit[next_id]

            if next[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            elif next[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            elif next[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False 
            elif next[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            
            self.__break_walls_r(next[0], next[1])

    def __reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self.__solve_r(0,0)

    def __solve_r(self, i, j):
        self.__animate()
        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        to_visit = []

        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j - 1].has_bottom_wall:
            to_visit.append((i, j - 1))
        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j + 1].has_top_wall:
            to_visit.append((i, j + 1))
        if i > 0 and not self._cells[i -1][j].visited and not self._cells[i -1][j].has_right_wall:
            to_visit.append((i - 1, j))
        if i < self.num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i + 1][j].has_left_wall:
            to_visit.append((i + 1, j))

        for direction in to_visit:
            self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]])
            result = self.__solve_r(direction[0], direction[1])
            if result == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]], True)
        
        return False

            
        
        