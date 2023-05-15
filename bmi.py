import tkinter as tk

def Bmi_Calculator_metrics(weight, height):
    w = weight
    h = height
    return w/h**2

def Bmi_Calculator_Imperial(weightI, heightI):
    w = weightI
    h = (heightI**2)
    return (w/h)*703




root = tk.Tk()
root.mainloop()
