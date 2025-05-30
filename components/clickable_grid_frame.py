import customtkinter

class ClickableGridFrame(customtkinter.CTkFrame):
    def __init__(self, master, grid_offset, rows, columns, **kwargs):
        super().__init__(master, width=800, height=800, **kwargs)
        self.rows = rows
        self.columns = columns

        self.canvas = customtkinter.CTkCanvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Configure>", self.draw_grid)

        self.selected_cell = None
        self.toggled_cells = set()
        self.new_toggled_cells = set()
        self.grid_offset = grid_offset
        self.should_draw_lines = True

        # store id for later changes of color
        self.rect_ids = {}

    def on_click(self, event):
        cell_width = self.canvas.winfo_width() / self.columns
        cell_height = self.canvas.winfo_height() / self.rows

        c = int(event.x // cell_width)
        r = int(event.y // cell_height)

        col = c + self.grid_offset
        row = r + self.grid_offset

        self.selected_cell = (col, row)

        if self.selected_cell in self.toggled_cells:
            self.toggled_cells.remove(self.selected_cell)
            color = "white"
        else:
            self.toggled_cells.add(self.selected_cell)
            color = "green"

        rect_id = self.rect_ids.get((c, r))
        if rect_id:
            outline = "black" if self.should_draw_lines else "white"
            self.canvas.itemconfig(rect_id, fill=color, outline=outline)

    def draw_grid(self, event=None):
        self.canvas.delete("all")
        self.rect_ids.clear()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        cell_width = width / self.columns
        cell_height = height / self.rows

        for col in range(self.columns):
            for row in range(self.rows):
                x1 = col * cell_width
                y1 = row * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height

                # white - dead, green - alive, black - outline
                color = "white"
                if (col + self.grid_offset, row + self.grid_offset) in self.toggled_cells:
                    color = "green"
                outline = "black" if self.should_draw_lines else "white"

                # store id for later changes of color
                rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline)
                self.rect_ids[(col, row)] = rect_id


    def update_grid(self):
        for (col, row), rect_id in self.rect_ids.items():
            cell = (col + self.grid_offset, row + self.grid_offset)
            was_alive = cell in self.toggled_cells
            is_alive = cell in self.new_toggled_cells
            if was_alive != is_alive:
                color = "green" if is_alive else "white"
                outline = "black" if self.should_draw_lines else "white"
                self.canvas.itemconfig(rect_id, fill=color, outline=outline)

        self.toggled_cells = self.new_toggled_cells
        self.new_toggled_cells = set()


    def set_grid_offset(self, new_grid_offset):
        self.grid_offset = new_grid_offset
        self.draw_grid()
