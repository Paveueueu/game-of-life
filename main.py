import customtkinter

import game_of_life
from components import *
import game_of_life

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Game of Life")
        self.geometry("800x800")
        self.resizable(False, False)

        self.frame = ClickableGridFrame(master=self, rows=10, columns=10, corner_radius=10)
        self.step_button = customtkinter.CTkButton(master=self, text="Step 1 frame", command=self.step)
        self.frame.pack(fill="both", expand=True)
        self.step_button.pack(fill="both")

    def step(self):
        result = game_of_life.step(self.frame.toggled_cells)
        self.frame.toggled_cells = result
        self.frame.draw_grid()
        print(self.frame.toggled_cells)
        

if __name__ == '__main__':
    app = App()
    app.mainloop()

