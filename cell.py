from graphics import Line, Point


class Cell:
    def __init__(self, win = None):
        self.has_left_wall= True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x_t_left, y_t_left, x_b_right, y_b_right):
        if self._win is None:
            return
        
        self._x1 = x_t_left
        self._y1 = y_t_left
        self._x2 = x_b_right
        self._y2 = y_b_right

        if self.has_top_wall:
            self._win.draw_line(Line(Point(x_t_left, y_t_left), Point(x_b_right, y_t_left)))
        else:
            self._win.draw_line(Line(Point(x_t_left, y_t_left), Point(x_b_right, y_t_left)), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x_t_left, y_b_right), Point(x_b_right, y_b_right)))
        else:
            self._win.draw_line(Line(Point(x_t_left, y_b_right), Point(x_b_right, y_b_right)), 'black')
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x_t_left, y_t_left), Point(x_t_left, y_b_right)))
        else: 
            self._win.draw_line(Line(Point(x_t_left, y_t_left), Point(x_t_left, y_b_right)), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x_b_right, y_t_left), Point(x_b_right, y_b_right)))
        else:
            self._win.draw_line(Line(Point(x_b_right, y_t_left), Point(x_b_right, y_b_right)), "black")
    def draw_move(self, to_cell, undo = False):
        col = 'red' if undo else 'grey'

        half_self = abs(self._x2 - self._x1) // 2
        center_self_x = half_self + self._x1
        center_self_y = half_self + self._y1

        half_other = abs(to_cell._x2 - to_cell._x1) // 2
        center_other_x = half_other + to_cell._x1
        center_other_y = half_other + to_cell._y1

        line = Line(
            Point(center_self_x, center_self_y),
            Point(center_other_x, center_other_y))
        self._win.draw_line(line, col)