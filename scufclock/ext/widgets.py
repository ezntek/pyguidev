import time
from tkinter import TOP, StringVar, ttk, BOTH
import datetime

class Widgets(object):
    def __init__(self, root) -> None:
        self.window = ttk.Frame(root)
        self.window.pack(fill=BOTH, expand=True)
        widgets = self.addWidgets()
        self.timeStringVar = StringVar()        
        # pack calls
        widgets[0].pack(
            side=TOP,
            expand=True,
            fill=BOTH,
            padx=5,
            pady=5
        )
        widgets[1].pack(
            side=TOP,
            expand=True,
            fill=BOTH,
            padx=5,
            pady=5
        )

    def addWidgets(self):
        # stringVars
        #imeStringVar = StringVar()
        formattedTime = datetime.datetime.now().strftime("%H:%M:%S")
        self.timeStringVar.set(formattedTime)

        # list
        widgets = []

        # widgets
        label = ttk.Label(self.window, textvariable=self.timeStringVar)
        refreshButton = ttk.Button(self.window, text="Refresh", command=self.refreshClock)    
        widgets.append(label)
        widgets.append(refreshButton)

        return widgets
    
    def refreshClock(self):
        while True:
            formattedTime = datetime.datetime.now().strftime("%H:%M:%S")
            self.timeStringVar = formattedTime
            time.sleep(1)
