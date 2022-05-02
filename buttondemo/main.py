import tkinter as ttk
ApplicationRoot = ttk.Tk()
ApplicationFrame = ttk.Frame(ApplicationRoot)

# base config
ApplicationRoot.title("button demo")

# grid setup
ApplicationFrame.grid(ipadx=5, ipady=5)
ApplicationFrame.columnconfigure(5, weight=5)
ApplicationFrame.rowconfigure(5, weight=5)

class Widgets(object):
    def __init__(self) -> None:
        # ttk.*Var() definitions
        self.labelvar = ttk.StringVar()
        self.entryvar = ttk.StringVar()
        self.labelvar.set("enter text to change")

        # widget definitions
        self.label = ttk.Label(
            ApplicationFrame, 
            textvariable=self.labelvar
        )
        self.entry = ttk.Entry(
            ApplicationFrame,
            textvariable=self.entryvar
        )
        self.submitBtn = ttk.Button(
            ApplicationFrame,
            text="Submit",
            command=self.update
        )

        # grid calls
        self.label.grid(
            column=0, 
            row=0, 
            columnspan=2, 
            padx=5, pady=5,
            sticky="nwes"
        )
        self.entry.grid(
            column=0,
            row=1,
            padx=5, pady=5,
            sticky="nwes"
        )
        self.submitBtn.grid(
            column=1,
            row=1,
            padx=5, pady=5,
            sticky="nwes"
        )
    
    def update(self) -> None:
        self.labelvar.set("updated: {}".format(self.entry.get()))

if __name__ == "__main__": 
    Widgets()
    ApplicationRoot.mainloop()