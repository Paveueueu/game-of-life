import tkinter

import customtkinter

from components.checkbox_grid import CheckboxGrid
from components.clickable_grid_frame import *
from components.zoom_selector import *
import game_of_life

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Game of Life")
        self.geometry("800x800")
        self.resizable(False, False)

        # settings
        self.settings = CheckboxGrid(self)
        self.settings.pack(fill="both")

        self.zoom_selector = ZoomSelector(self, command=self.change_zoom)
        self.zoom_selector.pack(fill="both")

        zoom = self.zoom_selector.get_zoom()
        max_zoom = self.zoom_selector.get_max_zoom()
        grid_offset = (max_zoom - 1 - zoom) // 2

        # game frame
        self.frame = ClickableGridFrame(master=self, rows=20, columns=20, corner_radius=10, grid_offset=grid_offset)
        self.frame.pack(fill="both", expand=True)

        # step button
        self.step_button = customtkinter.CTkButton(master=self, text="Step 1 frame", command=self.step)
        self.step_button.pack(fill="both")

    def step(self):
        rules = self.settings.get_rules()

        result = game_of_life.step(self.frame.toggled_cells, rules)
        self.frame.toggled_cells = result
        self.frame.draw_grid()
        # print(self.frame.toggled_cells)

    def change_zoom(self, event):
        # TODO temporary fix
        zoom = self.zoom_selector.get_zoom()
        max_zoom = self.zoom_selector.get_max_zoom()
        grid_offset = (max_zoom - 1 - zoom) // 2
        self.frame.set_grid_offset(grid_offset)

        if zoom > 99:
            self.frame.should_draw_lines = False
        else:
            self.frame.should_draw_lines = True

        self.frame.rows = zoom
        self.frame.columns = zoom
        self.frame.draw_grid()


if __name__ == '__main__':
    app = App()
    app.mainloop()
