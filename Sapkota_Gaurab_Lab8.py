import tkinter as tk


class Canvas(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.rectvar = tk.IntVar()
        self.rectvar.set(0)
        self.ovalvar = tk.IntVar()
        self.ovalvar.set(0)
        self.checkVar = tk.IntVar()
        self.checkVar.set(0)

        self.canvas = tk.Canvas(master=self.master, height=300, width=300)
        self.frame = tk.Frame(master=self.master)
        self.rectRadio = tk.Radiobutton(
            self.frame,
            text="Rectangle",
            variable=self.rectvar,
            state="normal",
            command=self.createRect,
        )

        self.ovalRadio = tk.Radiobutton(
            self.frame, text="Oval", variable=self.ovalvar, command=self.createOval
        )
        self.check = tk.Checkbutton(
            master=self.frame, text="Filled", variable=self.checkVar
        )
        self.deleteBtn = tk.Button(self.frame,text="Clear",command=self.clearCanvas)
        self.master.title("Canvas")
        self.canvas.grid(column=0, row=0)
        self.rectRadio.grid(row=0, column=0)
        self.ovalRadio.grid(row=0, column=1)
        self.check.grid(row=0, column=2)
        self.deleteBtn.grid(row=0,column=3)
        self.frame.grid(row=1, column=0)

    def createOval(self):
        if self.checkVar.get() == 1:
            self.canvas.create_oval(50, 100, 250, 200, outline="black",fill="blue")
        else:
            self.canvas.create_oval(50, 100, 250, 200, outline="black")


    def createRect(self):
        if self.checkVar.get() == 1:
            self.canvas.create_rectangle(50, 50, 250, 250, outline="black", fill="red")
            
        else:

            self.canvas.create_rectangle(
                50,
                50,
                250,
                250,
                outline="black",
            )

    def clearCanvas(self):
        self.canvas.delete("all")
        self.rectRadio.deselect()
        self.ovalRadio.deselect()


Canvas().mainloop()
