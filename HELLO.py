import tkinter as tk

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=25, font=('Arial', 16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_add():
    first_number = display.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    display.delete(0, tk.END)

def button_equal():
    second_number = display.get()
    display.delete(0, tk.END)
    if math == "addition":
        result = f_num + int(second_number)
    display.insert(0, result)


button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
# Create buttons for other numbers, operations, and the equal sign

button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
# Position other buttons using grid()

button_clear.grid(row=1, column=0, columnspan=2)
button_add.grid(row=1, column=2)
button_equal.grid(row=4, column=0, columnspan=3)

root.mainloop()