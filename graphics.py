from tkinter import (Tk, BOTH, Canvas)

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Hello there')
        self.__canvas = Canvas(self.__root, bg="black", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WIND", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.redraw():
            self.redraw()
        print('Window closed...')
    
    def close(self):
        self.__running = False