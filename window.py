import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Data Visualizer')
    self.attributes('-fullscreen', True)

    # label
    self.label = ttk.Label(self, text='Hello, Tkinter!')
    self.label.place(relx=.5, rely=.1, anchor="c")

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.pack()

    # close program button
    exit_button = ttk.Button(self, text="X", command=self.destroy)
    exit_button.place(relx=.982, rely=0.01, anchor="c")

    
    
    label_file_explorer = ttk.Label(self, text = "File Explorer using Tkinter")
    label_file_explorer.place(relx=.75,rely=.05, anchor="c")
    button_explore = ttk.Button(self, text = "Browse Files", command = self.browseFiles())
    
    

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

  def browseFiles(label_file_explorer):
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files","*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    


if __name__ == "__main__":
  app = App()
  app.mainloop()