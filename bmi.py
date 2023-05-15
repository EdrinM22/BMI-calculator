import tkinter as tk

def metrics_clicked():
    global weight_kg, height_m, result_label
    if weight_kg is None:
        tk.Label(root, text="Enter Weight in kg:").pack()
        weight_kg = tk.Entry(root)
        weight_kg.pack()
        tk.Label(root, text="Enter Height in m:").pack()
        height_m = tk.Entry(root)
        height_m.pack()
        tk.Button(root, text="OK", command=calculate_metrics_bmi).pack()

def imperial_clicked():
    global weight_lbs, height_in, result_label
    if weight_lbs is None:
        tk.Label(root, text="Enter Weight in lbs:").pack()
        weight_lbs = tk.Entry(root)
        weight_lbs.pack()
        tk.Label(root, text="Enter Height in in:").pack()
        height_in = tk.Entry(root)
        height_in.pack()
        tk.Button(root, text="OK", command=calculate_imperial_bmi).pack()

def calculate_metrics_bmi():
    bmi = Bmi_Calculator_metrics(float(weight_kg.get()), float(height_m.get()))
    display_result(bmi)

def calculate_imperial_bmi():
    bmi = Bmi_Calculator_Imperial(float(weight_lbs.get()), float(height_in.get()))
    display_result(bmi)

def display_result(bmi):
    global result_label
    if result_label is None:
        result_label = tk.Label(root, text=f"BMI: {bmi:.2f}")
        result_label.pack()
    else:
        result_label.config(text=f"BMI: {bmi:.2f}")

def Bmi_Calculator_metrics(weight, height):
    w = weight
    h = height
    return w/h**2

def Bmi_Calculator_Imperial(weightI, heightI):
    w = weightI
    h = (heightI**2)
    return (w/h)*703

root = tk.Tk()
root.geometry("800x600")
root.configure(background='lightblue')
weight_kg, height_m, weight_lbs, height_in = None, None, None, None
result_label = None
metrics = tk.Button(root, text="Metrics", command=metrics_clicked)
metrics.pack()
imperial = tk.Button(root, text="Imperial", command=imperial_clicked)
imperial.pack()
root.mainloop()
