import tkinter as tk
import handleColor
class ColorGUI:
    def __init__(self):


        self.root = tk.Tk()
        self.root.geometry("1200x675")
        self.root.title("Train Colors")
        self.label = tk.Label(self.root, text="What color is this?")
        pixel = tk.PhotoImage(width=1, height=1)
        self.label.pack(padx=10, pady=10)
        self.colorFrame = tk.Frame(width=100, height=100)
        self.colorFrame.pack(padx=10, pady=10)
        self.predictLabel = tk.Label(self.root)
        self.getColor()
        self.buttonFrame = tk.Frame()
        # Tkinter does not really support these kinds of buttons so this part of the code is sloppy.
        #RED
        btn = tk.Button(self.buttonFrame, image=pixel, text="Red", width=100, height=100, background="RED",
                        foreground="BLACK", compound="bottom", command=lambda: self.teachColor("RED", self.colorRGB))
        btn.grid(row=0, column=0, sticky="we")
        #ORANGE
        btn = tk.Button(self.buttonFrame, image=pixel, text="Orange", width=100, height=100, background="ORANGE",
                        foreground="BLACK", compound="bottom", command=lambda: self.teachColor("ORANGE", self.colorRGB))
        btn.grid(row=0, column=1, sticky="we")
        #YELLOW
        btn = tk.Button(self.buttonFrame, image=pixel, text="Yellow", width=100, height=100, background="YELLOW",
                        foreground="BLACK", compound="bottom", command=lambda: self.teachColor("YELLOW", self.colorRGB))
        btn.grid(row=0, column=2, sticky="we")
        #GREEN
        btn = tk.Button(self.buttonFrame, image=pixel, text="Green", width=100, height=100, background="GREEN",
                        foreground="BLACK", compound="bottom", command=lambda: self.teachColor("GREEN", self.colorRGB))
        btn.grid(row=0, column=3, sticky="we")
        #BLUE
        btn = tk.Button(self.buttonFrame, image=pixel, text="Blue", width=100, height=100, background="BLUE",
                        foreground="WHITE", compound="bottom", command=lambda: self.teachColor("BLUE", self.colorRGB))
        btn.grid(row=1, column=0, sticky="we")
        #PURPLE
        btn = tk.Button(self.buttonFrame, image=pixel, text="Purple", width=100, height=100, background="PURPLE",
                        foreground="WHITE", compound="bottom", command=lambda: self.teachColor("PURPLE", self.colorRGB))
        btn.grid(row=1, column=1, sticky="we")
        #PINK
        btn = tk.Button(self.buttonFrame, image=pixel, text="Pink", width=100, height=100, background="PINK",
                        foreground="BLACK", compound="bottom", command=lambda: self.teachColor("PINK", self.colorRGB))
        btn.grid(row=1, column=2, sticky="we")
        #BROWN
        btn = tk.Button(self.buttonFrame, image=pixel, text="Brown", width=100, height=100, background="BROWN",
                        foreground="BLACK", compound="bottom", command=lambda: self.teachColor("BROWN", self.colorRGB))
        btn.grid(row=1, column=3, sticky="we")
        # WHITE
        btn = tk.Button(self.buttonFrame, image=pixel, text="White", width=100, height=100, background="WHITE",
                        foreground="BLACK", compound="bottom", command=lambda: self.teachColor("WHITE", self.colorRGB))
        btn.grid(row=2, column=0, sticky="we")
        # LIGHT GRAY
        btn = tk.Button(self.buttonFrame, image=pixel, text="Light Gray", width=100, height=100, background="LIGHT GRAY",
                        foreground="BLACK", compound="bottom", command=lambda: self.teachColor("LIGHT GRAY", self.colorRGB))
        btn.grid(row=2, column=1, sticky="we")
        # DARK GRAY
        btn = tk.Button(self.buttonFrame, image=pixel, text="Dark Gray", width=100, height=100, background="#646464",
                        foreground="WHITE", compound="bottom", command=lambda: self.teachColor("DARK GRAY", self.colorRGB))
        btn.grid(row=2, column=2, sticky="we")
        # BLACK
        btn = tk.Button(self.buttonFrame, image=pixel, text="Black", width=100, height=100, background="BLACK",
                        foreground="WHITE", compound="bottom", command=lambda: self.teachColor("BLACK", self.colorRGB))
        btn.grid(row=2, column=3, sticky="we")

        self.buttonFrame.pack()

        self.predictLabel.pack()
        self.root.mainloop()

    def teachColor(self, color, RGB):
        handleColor.learnColor(color, RGB)
        self.getColor()

    def getColor(self):
        self.colorRGB = handleColor.requestColor()
        self.colorText = handleColor.colorToText(self.colorRGB)
        self.colorFrame.config(bg=self.colorText)
        self.predictLabel.config(text=f"I think it's {handleColor.requestBestFit(self.colorRGB).lower()}!")