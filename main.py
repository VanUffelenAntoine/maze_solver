from graphics import Window, Line, Point

def main():
    win = Window(800,600)
    line1 = Line(Point(0,0),Point(99, 99))
    win.draw_line(line1)

    win.wait_for_close()

main()