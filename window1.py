import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    # Do something with the selected file_path, like printing it
    print("Selected file:", file_path)

def perform_analysis():
    selected_method = analysis_methods.get()
    # Do something with the selected_method, like printing it
    print("Selected method:", selected_method)

def minimize_window():
    root.attributes('-topmost', 1)
    root.iconify()

def maximize_window():
    root.attributes('-topmost', 1)
    root.state('zoomed')
    maximize_button.destroy
    minify_button.place(x=root.winfo_screenwidth() - 80, y=0, width=30, height=30)
    root.resizable(False, False)

def minify_window():
    root.attributes('-topmost', 1)
    root.geometry("500*400")
    minify_button.destroy
    maximize_button.place(x=root.winfo_screenwidth() - 80, y=0, width=30, height=30)
    root.resizable(True, True)

def close_window():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Statistical Analysis")

#root.attributes('-fullscreen', True)  # Set the window to fullscreen


# Function to exit fullscreen (press F11 to toggle fullscreen)
#def toggle_fullscreen(event=None):
 #   root.attributes("-fullscreen", not root.attributes("-fullscreen"))

#root.bind("<F11>", toggle_fullscreen)
# Create a frame to hold widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=40)
root.resizable(True, True)
# Button to open files
open_button = tk.Button(frame, text="Open File", command=open_file)
open_button.pack(padx=10, pady=10)

# Dropdown list for statistical analysis methods
analysis_methods = tk.StringVar()
methods = ['Method 1', 'Method 2', 'Method 3']  # Replace with your methods
analysis_methods.set(methods[0])  # Set default method

method_dropdown = tk.OptionMenu(frame, analysis_methods, *methods)
method_dropdown.pack(padx=10, pady=10)

# Button to perform analysis
analyze_button = tk.Button(frame, text="Perform Analysis", command=perform_analysis)
analyze_button.pack(padx=10, pady=10)

# Buttons for window controls
minimize_button = tk.Button(root, text="_", command=minimize_window)
minimize_button.place(x=root.winfo_screenwidth() - 120, y=0, width=30, height=30)

maximize_button = tk.Button(root, text="□", command=maximize_window)
maximize_button.place(x=root.winfo_screenwidth() - 80, y=0, width=30, height=30)

minify_button = tk.Button(root, text="□", command=minify_window)

close_button = tk.Button(root, text="X", command=close_window)
close_button.place(x=root.winfo_screenwidth() - 40, y=0, width=30, height=30)

root.mainloop()