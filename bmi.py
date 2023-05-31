import tkinter as tk

weight_kg, height_m, weight_lbs, height_in, result_label, error_label = None, None, None, None, None, None
input_frame = None
metrics_button = None
imperial_button = None
history_button = None  # Define history_button as a global variable
history_list = []  # Store the history of BMI calculations

def metrics_clicked():
    global weight_kg, height_m, result_label, error_label, input_frame, metrics_button, imperial_button
    if weight_kg is None:
        clear_labels()
        if input_frame:
            input_frame.destroy()
        input_frame = tk.Frame(root, bg='white')
        input_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        tk.Label(input_frame, text="Enter Weight in kg:").pack()
        weight_kg = tk.Entry(input_frame)
        weight_kg.pack()
        tk.Label(input_frame, text="Enter Height in m:").pack()
        height_m = tk.Entry(input_frame)
        height_m.pack()
        tk.Button(input_frame, text="OK", command=calculate_metrics_bmi).pack()
        metrics_button.pack_forget()
        imperial_button.pack_forget()
        history_button.pack_forget()  # Hide the history_button when entering new values

def imperial_clicked():
    global weight_lbs, height_in, result_label, error_label, input_frame, metrics_button, imperial_button
    if weight_lbs is None:
        clear_labels()
        if input_frame:
            input_frame.destroy()
        input_frame = tk.Frame(root, bg='white')
        input_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        tk.Label(input_frame, text="Enter Weight in lbs:").pack()
        weight_lbs = tk.Entry(input_frame)
        weight_lbs.pack()
        tk.Label(input_frame, text="Enter Height in in:").pack()
        height_in = tk.Entry(input_frame)
        height_in.pack()
        tk.Button(input_frame, text="OK", command=calculate_imperial_bmi).pack()
        metrics_button.pack_forget()
        imperial_button.pack_forget()
        history_button.pack_forget()  # Hide the history_button when entering new values

def reset_clicked():
    global weight_kg, height_m, weight_lbs, height_in, result_label, error_label, input_frame, metrics_button, imperial_button, history_button
    weight_kg = None
    height_m = None
    weight_lbs = None
    height_in = None
    clear_labels()
    if result_label is not None:
        result_label.destroy()
        result_label = None
    if error_label is not None:
        error_label.destroy()
        error_label = None
    if input_frame:
        input_frame.destroy()
    input_frame = tk.Frame(root, bg='white')
    input_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    metrics_button = tk.Button(input_frame, text="Metrics", command=metrics_clicked)
    metrics_button.pack(side=tk.LEFT)
    imperial_button = tk.Button(input_frame, text="Imperial", command=imperial_clicked)
    imperial_button.pack(side=tk.LEFT)
    history_button = tk.Button(input_frame, text="History", command=show_history)
    history_button.pack(side=tk.LEFT)

def quit_clicked():
    root.destroy()

def clear_labels():
    global input_frame
    if input_frame:
        for widget in input_frame.winfo_children():
            widget.destroy()

def calculate_metrics_bmi():
    if weight_kg is not None or height_m is not None:
        try:
            weight = float(weight_kg.get())
            height = float(height_m.get())
            if weight <= 0 or height <= 0:
                display_error("Invalid input. Weight and height must be positive.")
            else:
                bmi = Bmi_Calculator_metrics(weight, height)
                display_result(bmi)
                move_arrow(bmi)
                history_list.append(bmi)  # Add the BMI calculation to the history list
        except ValueError:
            display_error("Invalid input. Please enter numeric values.")

def calculate_imperial_bmi():
    if weight_lbs is not None or height_in is not None:
        try:
            weight = float(weight_lbs.get())
            height = float(height_in.get())
            if weight <= 0 or height <= 0:
                display_error("Invalid input. Weight and height must be positive.")
            else:
                bmi = Bmi_Calculator_Imperial(weight, height)
                display_result(bmi)
                move_arrow(bmi)
                history_list.append(bmi)  # Add the BMI calculation to the history list
        except ValueError:
            display_error("Invalid input. Please enter numeric values.")

def display_result(bmi):
    global result_label
    if result_label is None:
        result_label = tk.Label(input_frame, text=f"BMI: {bmi:.2f}")
        result_label.pack()
    else:
        result_label.config(text=f"BMI: {bmi:.2f}")
    move_arrow(bmi)

def move_arrow(bmi):
    x_pos = 400
    y_pos = 350
    arrow_width = 10

    if bmi < 18.5:  # underweight
        x_pos -= arrow_width * 15
    elif bmi > 25 and bmi < 29.9:  # overweight
        x_pos += arrow_width
    elif bmi > 18.5 and bmi < 24.9:  # normal
        x_pos -= arrow_width * 7.5
    elif bmi > 30 and bmi < 34.9:
        x_pos += arrow_width * 7.5
    elif bmi > 35:
        x_pos += arrow_width * 15

    canvas.coords(arrow, x_pos, y_pos - arrow_width, x_pos - arrow_width, y_pos + arrow_width,
                  x_pos + arrow_width, y_pos + arrow_width)

def Bmi_Calculator_metrics(weight, height):
    w = weight
    h = height
    return w / h ** 2

def Bmi_Calculator_Imperial(weightI, heightI):
    w = weightI
    h = (heightI ** 2)
    return (w / h) * 703

def display_error(message):
    global error_label
    if error_label is None:
        error_label = tk.Label(input_frame, text=message, fg='red')
        error_label.pack()
    else:
        error_label.config(text=message)

def show_history():
    top = tk.Toplevel(root)
    top.title('BMI Calculation History')
    history_text = tk.Text(top, height=10, width=30)
    history_text.pack()
    for i, bmi in enumerate(history_list, start=1):
        history_text.insert(tk.END, f'BMI Calculation {i}: {bmi:.2f}\n')

root = tk.Tk()
root.title('BMI Calculator by BodyCalc+')
root.geometry("800x600")
root.resizable(width=False, height=False)

canvas = tk.Canvas(root, width=800, height=550)
canvas.pack()

bg_image = tk.PhotoImage(file="BMIBg Final.png")
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

input_frame = tk.Frame(root, bg='white')
input_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

metrics_button = tk.Button(input_frame, text="Metrics", command=metrics_clicked)
metrics_button.pack(side=tk.LEFT)
imperial_button = tk.Button(input_frame, text="Imperial", command=imperial_clicked)
imperial_button.pack(side=tk.LEFT)
history_button = tk.Button(input_frame, text="History", command=show_history)
history_button.pack(side=tk.LEFT)

reset_button = tk.Button(root, text="Reset", command=reset_clicked)
reset_button.pack(side=tk.BOTTOM)

quit_button = tk.Button(root, text="Quit", command=quit_clicked)
quit_button.pack(side=tk.BOTTOM)

x_pos = 400
y_pos = 350
arrow_width = 10
arrow = canvas.create_polygon(x_pos, y_pos - arrow_width, x_pos - arrow_width, y_pos + arrow_width, x_pos + arrow_width,
                              y_pos + arrow_width, fill='black')

root.mainloop()
