import customtkinter

class Button(customtkinter.CTkButton):
    def __init__(self, root, row, column):
        self.row = row
        self.column = column
        super().__init__(root, text=f"{row}, {column}", command=self.on_clicked)
        self.grid(row=row, column=column, padx=2, pady=2, sticky="nsew")

    def on_clicked(self):
        print(f"button [{self.row}, {self.column}] clicked")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Game of Life")
        self.geometry("800x800")
        self.resizable(False, False)

        self.grid_frame = customtkinter.CTkFrame(self)

        self.rows = 20
        self.cols = 20
        self.buttons = []

        for r in range(self.rows):
            row_buttons = []
            for c in range(self.cols):
                button = Button(self.grid_frame, r, c)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        for i in range(self.rows):
            self.grid_frame.rowconfigure(i, weight=1)
        for j in range(self.cols):
            self.grid_frame.columnconfigure(j, weight=1)

        self.grid_frame.pack(fill="both", expand=True)



def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()

