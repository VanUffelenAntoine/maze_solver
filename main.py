from cell import Cell
from graphics import Window, Line, Point
from maze import Maze

def main():
    # win = Window(800,600)
    # line1 = Line(Point(0,0),Point(99, 99))
    # win.draw_line(line1)

    # cell1 = Cell(win)
    # cell1.draw(50, 50, 100, 100)

    # cell2 = Cell(win)
    # cell2.draw(100, 50, 150, 100)

    # cell1.draw_move(cell2)

    num_row = 12
    num_col = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_col
    cell_size_y = (screen_y - 2 * margin) / num_row
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_row, num_col, cell_size_x, cell_size_y, win)   

    win.wait_for_close()

main()