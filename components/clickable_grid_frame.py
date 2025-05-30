import customtkinter

class ClickableGridFrame(customtkinter.CTkFrame):
    def __init__(self, master, grid_offset, rows, columns, **kwargs):
        super().__init__(master, **kwargs)
        self.rows = rows
        self.columns = columns

        self.canvas = customtkinter.CTkCanvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Configure>", self.draw_grid)

        self.selected_cell = None
        self.toggled_cells = set()
        self.grid_offset = grid_offset
        self.should_draw_lines = True

    def on_click(self, event):
        cell_width = self.canvas.winfo_width() / self.columns
        cell_height = self.canvas.winfo_height() / self.rows

        c = int(event.x // cell_width)
        r = int(event.y // cell_height)

        col = c + self.grid_offset
        row = r + self.grid_offset

        # print(f"Clicked {col=}, {row=}")

        self.selected_cell = (col, row)

        if self.selected_cell in self.toggled_cells:
            self.toggled_cells.remove(self.selected_cell)
        else:
            self.toggled_cells.add(self.selected_cell)

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

                color = "white"
                if (i + self.grid_offset, j + self.grid_offset) in self.toggled_cells:
                    color = "black"
                # if (i, j) == self.selected_cell:
                #     color = "red"
                outline = "black" if self.should_draw_lines else color
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline)

    def set_grid_offset(self, new_grid_offset):
        self.grid_offset = new_grid_offset
        self.draw_grid()
