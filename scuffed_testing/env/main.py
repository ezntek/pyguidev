import tkinter as ttk
from tkinter import BOTH, TOP, LEFT, RIGHT, BOTTOM

ApplicationRoot = ttk.Tk()

ApplicationFrame = ttk.Frame(ApplicationRoot)
ApplicationFrame.pack(fill=BOTH, expand=True)

class Widgets(object):
    def __init__(self) -> None:
        # button
        self.button1 = ttk.Button(
            ApplicationFrame, 
            text="Test Text",
            background="red"
        )
        self.button2 = ttk.Button(
            ApplicationFrame,
            text="Second Button",
            background="blue"
        )
        self.button3 = ttk.Button(
            ApplicationFrame,
            text="Third Button",
            background="green"
        )
        # pack
        self.button1.pack(
            side=TOP, 
            fill=BOTH, 
            expand=True,
            padx=5,
            pady=5
        )
        self.button2.pack(
            side=LEFT,
            fill=BOTH,
            expand=True,
            padx=5,
            pady=5
        )
        self.button3.pack(
            side=LEFT,
            fill = BOTH,
            expand = True,
            padx=5,
            pady=5
        )
        

if __name__ == "__main__":
    Widgets()
    ApplicationRoot.mainloop()