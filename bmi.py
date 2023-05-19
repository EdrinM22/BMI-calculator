import tkinter as tk
weight_kg, height_m, weight_lbs, height_in, result_label = None, None, None, None, None


def metrics_clicked():
    global weight_kg, height_m, result_label
    if weight_kg is None:
        tk.Label(input_frame, text="Enter Weight in kg:").pack()
        weight_kg = tk.Entry(input_frame)
        weight_kg.pack()
        tk.Label(input_frame, text="Enter Height in m:").pack()
        height_m = tk.Entry(input_frame)
        height_m.pack()
        tk.Button(input_frame, text="OK", command=calculate_metrics_bmi).pack()


def imperial_clicked():
    global weight_lbs, height_in, result_label
    if weight_lbs is None:
        tk.Label(input_frame, text="Enter Weight in lbs:").pack()
        weight_lbs = tk.Entry(input_frame)
        weight_lbs.pack()
        tk.Label(input_frame, text="Enter Height in in:").pack()
        height_in = tk.Entry(input_frame)
        height_in.pack()
        tk.Button(input_frame, text="OK", command=calculate_imperial_bmi).pack()


def reset_clicked():
    global weight_kg, height_m, weight_lbs, height_in, result_label
    weight_kg = None
    height_m = None
    weight_lbs = None
    height_in = None
    if result_label is not None:
        result_label.destroy()
        result_label = None
    canvas.coords(arrow, x_pos, y_pos - arrow_width, x_pos - arrow_width, y_pos + arrow_width, x_pos + arrow_width, y_pos + arrow_width)


def calculate_metrics_bmi():
    if weight_kg is not None or height_m is not None:
        bmi = Bmi_Calculator_metrics(float(weight_kg.get()), float(height_m.get()))
        display_result(bmi)
        move_arrow(bmi)


def calculate_imperial_bmi():
    if weight_lbs is not None or height_in is not None:
        bmi = Bmi_Calculator_Imperial(float(weight_lbs.get()), float(height_in.get()))
        display_result(bmi)
        move_arrow(bmi)


def display_result(bmi):
    global result_label
    if result_label is None:
        result_label = tk.Label(input_frame, text=f"BMI: {bmi:.2f}")
        result_label.pack()
    else:
        result_label.config(text=f"BMI: {bmi:.2f}")
    move_arrow(bmi)


def move_arrow(bmi):
    x_pos = 400  # Initial x-coordinate of the arrow
    y_pos = 350  # Initial y-coordinate of the arrow
    arrow_width = 10  # Width of the arrow


    # Calculate the new x-coordinate based on the BMI value
    if bmi < 18.5:
        x_pos -= arrow_width  # Move left
    elif bmi > 25:
        x_pos += arrow_width  # Move right


    canvas.coords(arrow, x_pos, y_pos - arrow_width, x_pos - arrow_width, y_pos + arrow_width, x_pos + arrow_width, y_pos + arrow_width)  # Update the arrow position


def Bmi_Calculator_metrics(weight, height):
    w = weight
    h = height
    return w / h**2


def Bmi_Calculator_Imperial(weightI, heightI):
    w = weightI
    h = (heightI ** 2)
    return (w / h) * 703


root = tk.Tk()
root.title('BMI Calculator by BodyCalc+')
root.geometry("800x600")
root.resizable(width=False, height=False)


canvas = tk.Canvas(root, width=800, height=550)
canvas.pack()


bg_image = tk.PhotoImage(file="BMIBg.png")
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)


input_frame = tk.Frame(root, bg='white')
input_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


metrics = tk.Button(input_frame, text="Metrics", command=metrics_clicked)
metrics.pack(side=tk.LEFT)
imperial = tk.Button(input_frame, text="Imperial", command=imperial_clicked)
imperial.pack(side=tk.LEFT)
reset = tk.Button(root, text="Reset", command=reset_clicked)
reset.pack(side=tk.BOTTOM)


x_pos = 400  
y_pos = 350  
arrow_width = 10  
arrow = canvas.create_polygon(x_pos, y_pos - arrow_width, x_pos - arrow_width, y_pos + arrow_width, x_pos + arrow_width, y_pos + arrow_width, fill='red')


root.mainloop()
