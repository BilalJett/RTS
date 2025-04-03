import tkinter as tk

def on_slide1(val):
    # Update the label with values from both sliders
    label.config(text=f"Slider 1 Value: {slider1.get()}   Slider 2 Value: {slider2.get()}")

def on_slide2(val):
    # Update the label with values from both sliders
    label.config(text=f"Slider 1 Value: {slider1.get()}   Slider 2 Value: {slider2.get()}")

root = tk.Tk()
root.title("Dual Slider Example")

# Create the first slider (Slider 1)
slider1 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=on_slide1)
slider1.pack(padx=10, pady=10)

# Create the second slider (Slider 2)
slider2 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=on_slide2)
slider2.pack(padx=10, pady=10)

# Label to display the slider values
label = tk.Label(root, text="Slider 1 Value: 0   Slider 2 Value: 0")
label.pack()

root.mainloop()
