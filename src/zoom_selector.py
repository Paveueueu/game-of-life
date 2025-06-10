import customtkinter

class ZoomSelector(customtkinter.CTkFrame):
    '''
        Zoom selector allows user to change the visible part of the grid.

        Attributes:
            label (customtkinter.CTkLabel)
            zoom_var (IntVar): current zoom level
            combobox (customtkinter.CTkComboBox): zoom selector combobox

        Methods:
            get_zoom(): returns the currently selected zoom (board size)
            get_max_zoom(): returns the maximum available zoom (board size)
    '''

    def __init__(self, master=None, command=None, default=20, options=None, **kwargs):
        super().__init__(master, **kwargs)
        if options is None:
            options = [10, 20, 30, 50, 80, 100, 150, 200]
        self.label = customtkinter.CTkLabel(self, text="Visible part of board:")
        self.label.pack(side="left", padx=(5, 0))

        self.zoom_var = customtkinter.IntVar(value=default)
        self.combobox = customtkinter.CTkComboBox(
            self,
            values=[str(opt) for opt in options],
            variable=self.zoom_var,
            width=80,
            command=command
        )
        self.combobox.pack(side="left", padx=5)

    def get_zoom(self):
        return self.zoom_var.get()

    def get_max_zoom(self):
        return int(self.combobox._values[-1])
