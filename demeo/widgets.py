import tkinter as ttk

class Widgets:
    def __init__(self, root) -> None:
        self.frame = ttk.Frame(root)
        self.frame.pack(expand=True, fill=ttk.BOTH)
        self.labelText = ttk.StringVar()
        self.labelText.set("placeholder")

        self.labelTitle = ttk.Label(
            self.frame,
            textvariable=self.labelText
        )
        self.entry = ttk.Entry(
            self.frame,
            text="enter text inside"
        )
        self.button = ttk.Button(
            self.frame,
            text="Submit",
            command=self.updateLabel
        )

        # pack statements
        self.labelTitle.pack(
            expand=True,
            fill=ttk.BOTH,
            side=ttk.TOP,
            padx=5,
            pady=5
        )
        self.entry.pack(
            expand=True,
            fill=ttk.BOTH,
            side=ttk.LEFT,
            padx=5,
            pady=5
        )
        self.button.pack(
            expand=True,
            fill=ttk.BOTH,
            side=ttk.RIGHT,
            padx=5,
            pady=5
        )

    def updateLabel(self):
        self.labelText.set(self.entry.get())