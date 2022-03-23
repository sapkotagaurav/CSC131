import tkinter as tk


main_frame = tk.Tk()
main_frame.title("Temperature Conversion Lab")
faren_var = tk.StringVar()
faren_var.set(32)
celc_var = tk.StringVar()
celc_var.set(0)
kelv_var = tk.StringVar()
kelv_var.set(273.15)


def from_celc():
    celc = float(celc_var.get())
    faren = celc * 1.8 + 32
    kelv = celc + 273.15
    faren_var.set(str(faren))
    kelv_var.set(str(kelv))


def from_faren():
    faren = float(faren_var.get())
    celc = (faren - 32) * 9 / 5
    kelv = celc + 273.15
    celc_var.set(str(celc))
    kelv_var.set(str(kelv))


def from_kelv():
    kelv = float(kelv_var.get())
    celc = kelv - 273.15
    faren = celc * 1.8 + 32
    faren_var.set(str(faren))
    celc_var.set(str(celc))


faren_label = tk.Label(
    main_frame,
    text="Farenheit",
)
faren_label.grid(row=1, column=1)

faren_box = tk.Entry(main_frame, textvariable=faren_var)
faren_box.grid(row=2, column=1)

faren_button = tk.Button(main_frame, text="Convert from Farenheit",command=from_faren)
faren_button.grid(row=3, column=1)


celc_label = tk.Label(main_frame, text="Celcius")
celc_label.grid(row=1, column=2)

celc_box = tk.Entry(main_frame, textvariable=celc_var)
celc_box.grid(row=2, column=2)

celc_button = tk.Button(main_frame, text="Convert from Celcius", command=from_celc)
celc_button.grid(row=3, column=2)


kelv_label = tk.Label(main_frame, text="Kelvin")
kelv_label.grid(row=1, column=3)

kelv_box = tk.Entry(main_frame, textvariable=kelv_var)
kelv_box.grid(row=2, column=3)

kelv_button = tk.Button(main_frame, text="Convert from Kelvin",command=from_kelv())
kelv_button.grid(row=3, column=3)

main_frame.mainloop()
