import tkinter as tk
import sineX
from Color import colorPicker


def btn_clicked(button_val):
    current_value = textbox_var.get()
    button_val = str(button_val)
    if button_val == "=":
        result = sineX.evaluate(current_value)
        textbox_var.set(result)
    elif button_val == 'x^2':
        button_val = '^2'
        textbox_var.set(current_value + button_val)
    elif button_val == '1/x':
        button_val = '1/'
        textbox_var.set(current_value + button_val)
    elif button_val == '÷':
        button_val = '/'
        textbox_var.set(current_value + button_val)
    elif button_val == 'n!':
        button_val = '!'
        textbox_var.set(current_value + button_val)
    elif button_val == "C":
        textbox_var.set("")
    elif button_val == "←":
        textbox_var.set(current_value[:-1])
    elif button_val == "+/-":
        if current_value.startswith('-'):
            current_value = current_value[1:]
            textbox_var.set(current_value)
        else:
            current_value = '-' + current_value
            textbox_var.set(current_value)
    else:
        if current_value.endswith(("+", "-", "/", "*")) and button_val.endswith(("+", "-", "/", "*")):
            current_value = current_value[:-1]
            textbox_var.set(current_value + button_val)
        else:
            textbox_var.set(current_value + button_val)


root = tk.Tk()
root.title("Basic Calculator")

# creating input entry text box
textbox_var = tk.StringVar()
textbox = tk.Entry(root, textvariable=textbox_var, width=38, bg="#ffffff", borderwidth=0, fg="#000000",
                   font=('Arial', 18))
textbox.pack(padx=20, pady=20)

buttonFrame = tk.Frame(root)

buttons = {
    ('n!', 1, 1), ('C', 1, 2), ('←', 1, 3),
    ('1/x', 2, 0), ('√', 2, 1), ('x^2', 2, 2), ('÷', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('6', 4, 0), ('5', 4, 1), ('4', 4, 2), ('-', 4, 3),
    ('3', 5, 0), ('2', 5, 1), ('1', 5, 2), ('+', 5, 3),
    ('+/-', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3)
}

for (text, row, column) in buttons:
    background = colorPicker(row, column)

    button = tk.Button(buttonFrame, text=text, padx=20, pady=20, width=7, bg= background, fg="white", font=('Arial', 15),
                       command=lambda t=text: btn_clicked(t), borderwidth=1, relief=tk.RIDGE, highlightthickness=2,
                       highlightbackground="green")
    button.grid(row=row, column=column, sticky=tk.W + tk.E)

buttonFrame.pack()

tk.Label(root, ).pack()
root.mainloop()
