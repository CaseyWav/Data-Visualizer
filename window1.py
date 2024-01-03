import tkinter as tk
from data_reader1 import read_file
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    # Do something with the selected file_path, like printing it
    print("Selected file:", file_path)

def perform_analysis():
    selected_method = analysis_methods.get()
    # Do something with the selected_method, like printing it
    print("Selected method:", selected_method)


# Create the main window
root = tk.Tk()
root.title("Statistical Analysis")
root.resizable(True, True)
#root.attributes('-fullscreen', True)  # Set the window to fullscreen


# Function to exit fullscreen (press F11 to toggle fullscreen)
#def toggle_fullscreen(event=None):
 #   root.attributes("-fullscreen", not root.attributes("-fullscreen"))

#root.bind("<F11>", toggle_fullscreen)
# Create a frame to hold widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=40)

# Button to open files
open_button = tk.Button(frame, text="Open File", command=open_file)
open_button.pack(padx=10, pady=10)

# Dropdown list for statistical analysis methods
analysis_methods = tk.StringVar()
methods = ['Graph', 'Statistics', 'Method 3']  # Replace with your methods
analysis_methods.set(methods[0])  # Set default method

method_dropdown = tk.OptionMenu(frame, analysis_methods, *methods)
method_dropdown.pack(padx=10, pady=10)

if analysis_methods.get == 'Statistics':
    statistical_methods = tk.StringVar()
    stat_methods = ['Mean','Median','Max','Min']
    statistical_methods.set(stat_methods[0])
    stat_method_dropdown = tk.OptionMenu(frame, statistical_methods, *stat_methods)
    stat_method_dropdown.pack(padx=10, pady=60)

# Button to perform analysis
analyze_button = tk.Button(frame, text="Perform Analysis", command=perform_analysis)
analyze_button.pack(padx=10, pady=10)



root.mainloop()