from cell import Cell
from graphics import Window, Line, Point

def main():
    win = Window(800,600)
    # line1 = Line(Point(0,0),Point(99, 99))
    # win.draw_line(line1)

    cell1 = Cell(win)
    cell1.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.draw(100, 50, 150, 100)

    cell1.draw_move(cell2)

    win.wait_for_close()

main()