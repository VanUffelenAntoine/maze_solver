from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall= True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x_t_left, y_t_left, x_b_right, y_b_right):
        self._x1 = x_t_left
        self._y1 = y_t_left
        self._x2 = x_b_right
        self._y2 = y_b_right

        if self.has_top_wall:
            self._win.draw_line(Line(Point(x_t_left, y_t_left), Point(x_b_right, y_t_left)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x_t_left, y_b_right), Point(x_b_right, y_b_right)))
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x_t_left, y_t_left), Point(x_t_left, y_b_right)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x_b_right, y_t_left), Point(x_b_right, y_b_right)))