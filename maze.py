import time

from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_s_x, cell_s_y, win = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.c_s_x = cell_s_x
        self.c_s_y = cell_s_y
        self.win = win
        self._cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                    col.append(self.__draw_cells(i,j))
            self._cells.append(col)

    def __draw_cells(self, i, j):
        cell = Cell(self.win)
        x_t_left = self.x1 + i * self.c_s_x
        y_t_left = self.y1 + j * self.c_s_y
        cell.draw(x_t_left, y_t_left, x_t_left + self.c_s_x, y_t_left + self.c_s_y)      
        self.__animate()
        return cell
    
    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)