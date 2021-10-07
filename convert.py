import tkinter as tk
import random

def convert():
	fahren = int(fahr.get())
	answer = (fahren - 32) * 5 / 9
	celc["text"] = str(answer)+" ℃"

window = tk.Tk()

btn_conv = tk.Button(master=window, relief=tk.RAISED, text="Convert", command=convert)
btn_conv.pack()

celc = tk.Label(master=window, text="-")
celc.pack()

lbl_instr = tk.Label(master=window, relief=tk.RIDGE, text="Enter the temperature in Fahrenheit and press 'convert' to convert into Celcius")
lbl_instr.pack(side=tk.BOTTOM)

fahr = tk.Entry()
fahr.pack()

window.mainloop()