import tkinter as tk
from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from division import division
from modulo import modulo
from power import power
from sine import sine
from cosine import cosine
from square_root import square_root
from floor_value import floor_value
from ceil_value import ceil_value
from memory_add import memory_add
from memory_clear import memory_clear
from memory import memory

def main():
    def append_to_expression(value):
        entry_field.insert(tk.END, value)

    def clear_expression():
        entry_field.delete(0, tk.END)

    def calculate():
        try:
            expression = entry_field.get()
            result = eval(expression, {"__builtins__": None}, {
                "+": addition,
                "-": subtraction,
                "*": multiplication,
                "/": division,
                "%": modulo,
                "^": power,
                "sin": sine,
                "cos": cosine,
                "sqrt": square_root,
                "floor": floor_value,
                "ceil": ceil_value
            })
            entry_field.delete(0, tk.END)
            entry_field.insert(0, str(result))
        except Exception as e:
            entry_field.delete(0, tk.END)
            entry_field.insert(0, "Error")

    def add_to_memory():
        try:
            value = float(entry_field.get())
            memory_add(value)
            memory_label.config(text=f"Memory: {memory}")
        except ValueError:
            entry_field.delete(0, tk.END)
            entry_field.insert(0, "Error")

    def clear_memory():
        memory_clear()
        memory_label.config(text=f"Memory: {memory}")

    root = tk.Tk()
    root.title("Calculator")

    # Entry field
    entry_field = tk.Entry(root, width=20, font=("Arial", 18), bd=5, insertwidth=4, justify="right")
    entry_field.grid(row=0, column=0, columnspan=4, sticky="nsew")

    # Buttons
    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ("sin(", 5, 0), ("cos(", 5, 1), ("sqrt(", 5, 2), ("%", 5, 3),
        ("floor(", 6, 0), ("ceil(", 6, 1), ("^", 6, 2), ("C", 6, 3),
        (")", 5, 3)  # Move the closing bracket here, next to other functions
    ]

    for (text, row, col) in buttons:
        if text == "=":
            action = calculate
        elif text == "C":
            action = clear_expression
        else:
            action = lambda t=text: append_to_expression(t)

        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=action)
        button.grid(row=row, column=col, sticky="nsew")

    # Adjust grid weights for even spacing
    for i in range(7):
        root.grid_rowconfigure(i, weight=1)
    for j in range(4):
        root.grid_columnconfigure(j, weight=1)

    # Memory buttons
    memory_label = tk.Label(root, text=f"Memory: {memory}", font=("Arial", 14))
    memory_label.grid(row=7, column=0, columnspan=2, sticky="nsew")

    memory_add_button = tk.Button(root, text="M+", width=5, height=2, font=("Arial", 14), command=add_to_memory)
    memory_add_button.grid(row=7, column=2, sticky="nsew")

    memory_clear_button = tk.Button(root, text="MC", width=5, height=2, font=("Arial", 14), command=clear_memory)
    memory_clear_button.grid(row=7, column=3, sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    main()
