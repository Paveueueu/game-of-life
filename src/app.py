from src.checkbox_grid import *
from src.clickable_grid_frame import *
from src.zoom_selector import *
import src.game_of_life as game_of_life


class App(customtkinter.CTk):
    '''
        Application. Implements UI for Conway's Game of Life.

        Attributes:
            tool_bar (customtkinter.CTkFrame)
            checkbox_grid (CheckboxGrid)
            zoom_selector (ZoomSelector)
            frame (ClickableGridFrame)
            play_button (customtkinter.CTkButton)
            is_playing (bool)

        Methods:
            step(): performs a single simulation step
            toggle_play(): toggles simulation playback on/off
            play_step(): performs simulation steps in a loop while playback is on
            change_zoom(event): updates the visible part of the board based oncurrent zoom level
            kill_all(): sets all the cells' states to 'dead'
    '''
    def __init__(self):
        super().__init__()
        self.title("Game of Life")
        self.geometry("800x940")
        self.resizable(False, False)

        self.tool_bar = customtkinter.CTkFrame(self)

        # rules checkbox grid
        self.checkbox_grid = CheckboxGrid(self.tool_bar)
        self.checkbox_grid.grid(column=0, rowspan=3, row=0, sticky="nsew", padx=10, pady=10)

        # zoom selector
        self.zoom_selector = ZoomSelector(self.tool_bar, command=self.change_zoom)
        self.zoom_selector.grid(column=1, row=0, sticky="nsew", padx=10, pady=10)
        zoom = self.zoom_selector.get_zoom()
        self.max_zoom = self.zoom_selector.get_max_zoom()
        grid_offset = (self.max_zoom - 1 - zoom) // 2

        # board size label
        self.size_label = customtkinter.CTkLabel(self.tool_bar, text=f"Board size: {self.max_zoom}")
        self.size_label.grid(column=1, row=1, sticky="nsew", padx=10, pady=10)

        # wrap checkbox
        self.wrap_checkbox = customtkinter.CTkCheckBox(self.tool_bar, text='Wrap board (torus)', width=0)
        self.wrap_checkbox.grid(column=1, row=2, sticky="nsew", padx=10, pady=10)

        # step button
        self.step_button = customtkinter.CTkButton(master=self.tool_bar, text="1 Step", command=self.step)
        self.step_button.grid(column=2, row=0, sticky="nsew", padx=10, pady=10)

        # play/pause button
        self.is_playing = False
        self.play_job = None
        self.play_button = customtkinter.CTkButton(master=self.tool_bar, text="Play", command=self.toggle_play)
        self.play_button.grid(column=2, row=1, sticky="nsew", padx=10, pady=10)

        # kill button
        self.kill_button = customtkinter.CTkButton(master=self.tool_bar, text="Kill all", command=self.kill_all)
        self.kill_button.grid(column=2, row=2, sticky="nsew", padx=10, pady=10)

        self.tool_bar.pack(side="top", fill="x")

        # game frame
        self.frame = ClickableGridFrame(master=self, rows=20, columns=20, corner_radius=10, grid_offset=grid_offset)
        self.frame.pack(fill="both", expand=True)

    def step(self):
        rules = self.checkbox_grid.get_rules()

        if not self.wrap_checkbox.get():
            alive = game_of_life.step(self.frame.toggled_cells, rules)
        else:
            alive = game_of_life.step_wrap_around(self.frame.toggled_cells, rules, self.max_zoom)

        self.frame.new_toggled_cells = alive

        self.frame.update_grid()
        # print(self.frame.toggled_cells)

    def toggle_play(self):
        if self.is_playing:
            self.is_playing = False
            self.play_button.configure(text="Play")
            if self.play_job:
                self.after_cancel(self.play_job)
                self.play_job = None
        else:
            self.is_playing = True
            self.play_button.configure(text="Pause")
            self.play_step()

    def play_step(self):
        if self.is_playing:
            self.step()
            self.play_job = self.after(200, self.play_step)

    def change_zoom(self, event):
        zoom = self.zoom_selector.get_zoom()
        max_zoom = self.zoom_selector.get_max_zoom()
        grid_offset = (max_zoom - 1 - zoom) // 2
        self.frame.set_grid_offset(grid_offset)

        if zoom > 50:
            self.frame.should_draw_lines = False
        else:
            self.frame.should_draw_lines = True

        self.frame.rows = zoom
        self.frame.columns = zoom
        self.frame.draw_grid()

    def kill_all(self):
        self.frame.toggled_cells = set()
        self.frame.new_toggled_cells = set()
        self.frame.draw_grid()
