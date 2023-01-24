import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def open_file():
    filepath = filedialog.askopenfilename()
    data = pd.read_csv(filepath)
    display_data(data)

def display_data(data):
    figure = plt.figure(figsize=(5, 5))
    ax = figure.add_subplot(111)

    display_type = var.get()
    if display_type == "Scatter Plot":
        ax.scatter(data.iloc[:,0], data.iloc[:,1])
        ax.set_xlabel(data.columns[0])
        ax.set_ylabel(data.columns[1])
    elif display_type == "Pie Chart":
        data.iloc[:,2].plot.pie(ax=ax)
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root = tk.Tk()
root.title("CSV Data Reader")

var = tk.StringVar(value="Scatter Plot")
dropdown = tk.OptionMenu(root, var, "Scatter Plot", "Pie Chart")
dropdown.pack()

open_file_button = tk.Button(text="Open File", command=open_file)
open_file_button.pack()

root.mainloop()