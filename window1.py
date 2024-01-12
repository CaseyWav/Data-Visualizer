import tkinter as tk
from data_reader1 import read_file
from data_analysis_ddl import *
from tkinter import filedialog
from tkinter import Label
from tkinter import Canvas


# Create the main window
root = tk.Tk()
root.title("Statistical Analysis")
root.resizable(True, True)

# Create a frame to hold widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=40)
canvas = Canvas(root, bg="grey", height=250, width=300)
canvas.pack()
def open_file():
    file_path = filedialog.askopenfilename()
    # Do something with the selected file_path, like printing it
    label = Label(root, text=file_path)
    label.pack()

# Button to open files
open_button = tk.Button(frame, text="Open File", command=open_file)
open_button.pack(padx=10, pady=10)

# Dropdown list for statistical analysis methods
analysis_methods = tk.StringVar()
methods = ['Graph', 'Statistics', 'Method 3']  # Replace with your methods
analysis_methods.set(methods[0])  # Set default method

method_dropdown = tk.OptionMenu(frame, analysis_methods, *methods)
method_dropdown.pack(padx=10, pady=10)

statistical_methods = tk.StringVar()
statistical_methods.set(stat_methods[0])
stat_method_dropdown = tk.OptionMenu(frame, statistical_methods, *stat_methods)




def perform_analysis():
    selected_method = analysis_methods.get()
    # Do something with the selected_method, like printing it
    print("Selected method:", selected_method)



# Button to perform analysis
analyze_button = tk.Button(frame, text="Perform Analysis", command=perform_analysis)
analyze_button.pack(padx=10, pady=10)

def analysis_method_selector(*args):
    if analysis_methods.get() == 'Statistics' and not stat_method_dropdown.winfo_ismapped:
        stat_method_dropdown.pack(padx=10, pady=60)



analysis_methods.trace_add("write", analysis_method_selector)

root.mainloop()