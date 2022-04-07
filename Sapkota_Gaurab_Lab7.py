import tkinter as tk
from tkinter import messagebox as mb


class temperatureConversion:
    def __init__(self, master):
        master.title("Temperature Conversion")
        self.faren_var = tk.StringVar()
        self.celc_var = tk.StringVar()
        self.celc_var.set(0)
        self.kelv_var = tk.StringVar()
        self.from_celc()
        self.faren_label = tk.Label(
            master,
            text="Farenheit",
        )
        self.faren_label.grid(row=1, column=1)

        self.faren_box = tk.Entry(master, textvariable=self.faren_var)
        self.faren_box.grid(row=2, column=1)

        self.faren_button = tk.Button(
            master, text="Convert from Farenheit", command=self.from_faren
        )
        self.faren_button.grid(row=3, column=1)

        self.celc_label = tk.Label(master, text="Celcius")
        self.celc_label.grid(row=1, column=2)

        self.celc_box = tk.Entry(master, textvariable=self.celc_var)
        self.celc_box.grid(row=2, column=2)

        self.celc_button = tk.Button(
            master, text="Convert from Celcius", command=self.from_celc
        )
        self.celc_button.grid(row=3, column=2)

        self.kelv_label = tk.Label(master, text="Kelvin")
        self.kelv_label.grid(row=1, column=3)

        self.kelv_box = tk.Entry(master, textvariable=self.kelv_var)
        self.kelv_box.grid(row=2, column=3)

        self.kelv_button = tk.Button(
            master, text="Convert from Kelvin", command=self.from_kelv
        )
        self.kelv_button.grid(row=3, column=3)

    def from_celc(self):
        try:
            celc = float(self.celc_var.get())
            faren = celc * 1.8 + 32
            kelv = celc + 273.15
            self.faren_var.set(str(faren))
            self.kelv_var.set(str(kelv))
        except ValueError:
            self.show_error()

    def from_faren(self):
        try:
            faren = float(self.faren_var.get())
            celc = (faren - 32) * 5/9
            kelv = celc + 273.15
            self.celc_var.set(str(celc))
            self.kelv_var.set(str(kelv))
        except ValueError:
            self.show_error()

    def from_kelv(self):
        try:
            kelv = float(self.kelv_var.get())
            celc = kelv - 273.15
            faren = celc * 1.8 + 32
            self.faren_var.set(str(faren))
            self.celc_var.set(str(celc))
        except ValueError:
            self.show_error()

    def show_error(self):
        mb.showerror("Error", message="Error with the value")


def main():
    master = tk.Tk()
    app = temperatureConversion(master)
    master.mainloop()


main()
