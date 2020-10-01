import tkinter as tk
import solver

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


""" Main Sudoku drawing board GUI """
class SudokuUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.__setup_UI()

        self.grid = [[None for i in range(9)] for i in range(9)]
        self.row, self.col = -1, -1
        self.__draw_entries()

    # ------------------------ UI setup start ------------------------
    def __setup_UI(self):
        self.master.title("Sudoku")
        
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)
        self.canvas.bind("<BackSpace>", self.__delete_entry)

        self.__draw_grid()

        buttonFrame = tk.Frame(self)
        buttonFrame.pack(side="bottom", fill="x")
        tk.Button(buttonFrame, text="Solve", command=self.__solve).pack(side="left")
        tk.Button(buttonFrame, text="Clear", command=self.__clear_all_entries).pack(side="left")
        tk.Button(buttonFrame, text="Quit", command=self.master.destroy).pack(side="left")

    def __draw_grid(self):
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0, x1 = MARGIN + i * SIDE, MARGIN + i * SIDE
            y0, y1 = MARGIN, HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0, x1 = MARGIN, WIDTH - MARGIN
            y0, y1 = MARGIN + i * SIDE, MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
    # ------------------------ UI setup end ------------------------


    # ------------------------ Event Handlers start ------------------------
    # select and highlight a cell when clicked
    def __cell_clicked(self, event):
        x, y = event.x, event.y
        self.canvas.delete("cursor")

        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()
            row, col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1  # if cell was selected already, deselect it
            else:
                self.row, self.col = row, col
                x0 = MARGIN + self.col * SIDE + 1
                y0 = MARGIN + self.row * SIDE + 1
                x1 = MARGIN + (self.col + 1) * SIDE - 1
                y1 = MARGIN + (self.row + 1) * SIDE - 1
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="red", tags="cursor")
        else:
            self.row, self.col = -1, -1


    # if backspace is pressed (on a valid cell), remove the entry from the grid and redraw
    def __delete_entry(self, event):
        if self.row >= 0 and self.col >= 0:
            self.grid[self.row][self.col] = None
            self.__draw_entries()


    # if a number is pressed (on a valid cell), add the entry to the grid and redraw
    def __key_pressed(self, event):
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.grid[self.row][self.col] = int(event.char)
            self.__draw_entries()
    # ------------------------ Event Handlers end ------------------------


    # solve the given sudoku
    def __solve(self):
        self.is_solved, self.grid = solver.solve(self.grid)
        self.__draw_entries()


    # clear all entries from the grid
    def __clear_all_entries(self):
        self.grid = [[None for i in range(9)] for i in range(9)]
        self.__draw_entries()


    # delete all numbers shown on canvas, and redraw them
    def __draw_entries(self):
        self.canvas.delete("numbers")
        for row_idx in range(9):
            for col_idx in range(9):
                entry = self.grid[row_idx][col_idx]
                if entry != None:
                    x = MARGIN + col_idx * SIDE + SIDE / 2
                    y = MARGIN + row_idx * SIDE + SIDE / 2
                    self.canvas.create_text(x, y, text=entry, font=("Purisa", int(SIDE * 0.7)), tags="numbers", fill="black")



if __name__ == '__main__':
        root = tk.Tk()
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        app = SudokuUI(master=root)
        app.mainloop()
