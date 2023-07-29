import tkinter as tk

def on_click(event):
    current_text = display.get()
    clicked_text = event.widget.cget("text")

    if clicked_text == "=":
        try:
            result = eval(current_text)
            display.set(result)
        except Exception as e:
            display.set("Error")
    elif clicked_text == "C":
        display.set("")
    else:
        display.set(current_text + clicked_text)

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.config(bg="#F0F0F0")  # Set background color

# Create a custom font
font_style = ("Arial", 18, "bold")

# Create the display label
display = tk.StringVar()
display.set("")

display_label = tk.Label(root, textvariable=display, font=font_style, anchor="e", bd=10, relief=tk.RIDGE)
display_label.pack(fill=tk.BOTH, padx=10, pady=10)

# Create custom colors
button_bg = "#E0E0E0"
button_active_bg = "#C0C0C0"
button_fg = "#333333"

# Create the buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack()

button_texts = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for row in button_texts:
    button_row = tk.Frame(buttons_frame)
    button_row.pack()

    for text in row:
        button = tk.Button(button_row, text=text, font=font_style, relief=tk.GROOVE, bd=3,
                           bg=button_bg, activebackground=button_active_bg, fg=button_fg)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_click)

# Start the main event loop
root.mainloop()