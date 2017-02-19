import GUI
import tkinter as tk

servertype = "black"

master = tk.Tk()

GUI.Start(master, servertype)
master.mainloop()
master.destroy()