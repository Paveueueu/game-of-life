import customtkinter


class ClickableGridFrame(customtkinter.CTkFrame):
    def __init__(self, master, rows=2, columns=2, **kwargs):
        super().__init__(master, **kwargs)
        self.rows = rows
        self.columns = columns

        self.canvas = customtkinter.CTkCanvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Configure>", self.draw_grid)

        self.selected_cell = None

    def on_click(self, event):
        cell_width = self.canvas.winfo_width() / self.columns
        cell_height = self.canvas.winfo_height() / self.rows

        column = int(event.x // cell_width)
        row = int(event.y // cell_height)
        print(f"Clicked {column=}, {row=}")

        self.selected_cell = (column, row)
        self.draw_grid()

    def draw_grid(self, event=None):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        cell_width = width / self.columns
        cell_height = height / self.rows

        # draw cells
        for i in range(self.columns):
            for j in range(self.rows):
                x1 = i * cell_width
                y1 = j * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                color = "red" if self.selected_cell == (i, j) else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

        # draw vertical lines
        for i in range(1, self.columns):
            x = i * width / self.columns
            self.canvas.create_line(x, 0, x, height, fill="black")

        # draw horizontal lines
        for j in range(1, self.rows):
            y = j * height / self.rows
            self.canvas.create_line(0, y, width, y, fill="black")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Game of Life")
        self.geometry("800x800")
        self.resizable(False, False)

        self.frame = ClickableGridFrame(master=self, rows=10, columns=10, corner_radius=10)
        self.frame.pack(fill="both", expand=True)
        

if __name__ == '__main__':
    app = App()
    app.mainloop()

