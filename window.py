import tkinter as tk
from tkinter import *
from tkinter import OptionMenu, ttk
from tkinter import filedialog
from data_analysis_ddl import analysis_options
from tkinter.messagebox import showinfo

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Data Visualizer')
    width = self.winfo_screenwidth()
    height = self.winfo_screenheight()
    self.geometry("%dx%d" % (width, height))

    # label
    self.label = ttk.Label(self, text='Hello, Tkinter!')
    self.label.grid(row=0,column=0,columnspan=5)

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.grid(row=1,column=3,ipadx=.5,ipady=.5)
    label_file_explorer = ttk.Label(self, text = "File Explorer using Tkinter")
    label_file_explorer.place(relx=.75,rely=.05, anchor="c")
    self.button['command'] = self.button_clicked
    button_explore = ttk.Button(self, text = "Browse Files", command = (lambda: self.browseFiles(label_file_explorer)))
    
    button_explore.grid(row=3,column=4)
    
    clicked = StringVar(self)
    clicked.set("Select an analysis option")
    data_analysis_ddl = OptionMenu(self, clicked, *analysis_options)
    
    data_analysis_ddl.grid(row=4,column=5)

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')
    

  def browseFiles(self, label_file_explorer):
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files","*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

  
if __name__ == "__main__":
  app = App()
  app.mainloop()