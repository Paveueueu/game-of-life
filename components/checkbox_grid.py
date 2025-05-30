import customtkinter

class CheckboxGrid(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.checkboxes_live = []
        self.checkboxes_die = []
        self.labels = []

        n = 9

        # create labels
        for c in range(n):
            label = customtkinter.CTkLabel(master=self, text=f'{c}')
            label.grid(row=0, column=c+1, padx=0, pady=0)
            self.labels.append(label)

        label = customtkinter.CTkLabel(master=self, text='Live')
        label.grid(row=1, column=0, padx=10, pady=0)
        self.labels.append(label)

        label = customtkinter.CTkLabel(master=self, text='Die')
        label.grid(row=2, column=0, padx=10, pady=0)
        self.labels.append(label)


        # create checkboxes
        for c in range(n):
            checkbox = customtkinter.CTkCheckBox(self, text='', width=0)
            checkbox.grid(row=1, column=c + 1, padx=0, pady=0)
            self.checkboxes_live.append(checkbox)

        for c in range(n):
            checkbox = customtkinter.CTkCheckBox(self, text='', width=0)
            checkbox.grid(row=2, column=c + 1, padx=0, pady=0)
            self.checkboxes_die.append(checkbox)


    def get_rules(self):
        rules_live = []
        for i, checkbox in enumerate(self.checkboxes_live):
            if checkbox.get():
                rules_live.append(i)

        rules_die = []
        for i, checkbox in enumerate(self.checkboxes_die):
            if checkbox.get():
                rules_die.append(i)

        return rules_live, rules_die


