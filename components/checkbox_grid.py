import customtkinter

class CheckboxGrid(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.checkboxes_spawn = []
        self.checkboxes_die = []
        self.labels = []

        n = 9

        # create labels
        for c in range(n):
            label = customtkinter.CTkLabel(master=self, text=f'{c}')
            label.grid(row=0, column=c+1)
            self.labels.append(label)

        label = customtkinter.CTkLabel(master=self, text='Spawn rules:')
        label.grid(row=1, column=0, padx=10)
        self.labels.append(label)

        label = customtkinter.CTkLabel(master=self, text='Die rules:')
        label.grid(row=2, column=0, padx=10)
        self.labels.append(label)


        # create checkboxes
        for c in range(n):
            checkbox = customtkinter.CTkCheckBox(self, text='', width=0)
            checkbox.grid(row=1, column=c + 1)
            self.checkboxes_spawn.append(checkbox)

        for c in range(n):
            checkbox = customtkinter.CTkCheckBox(self, text='', width=0)
            checkbox.grid(row=2, column=c + 1)
            self.checkboxes_die.append(checkbox)

        self.checkboxes_spawn[0].configure(state="disabled")


    def get_rules(self):
        rules_live = []
        for i, checkbox in enumerate(self.checkboxes_spawn):
            if checkbox.get():
                rules_live.append(i)

        rules_die = []
        for i, checkbox in enumerate(self.checkboxes_die):
            if checkbox.get():
                rules_die.append(i)

        return rules_live, rules_die


