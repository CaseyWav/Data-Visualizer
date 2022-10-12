import tkinter as tk
from tkinter import *
from tkinter import OptionMenu, ttk
from tkinter import filedialog
from turtle import bgcolor
from data_analysis_ddl import analysis_options
from tkinter.messagebox import showinfo

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Data Visualizer')
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    self.geometry("%dx%d" % (screen_width, screen_height))

    frame1 = tk.Frame(self,width=(screen_width*.5),height=(screen_height*.5),bg="blue")
    frame1.place(relx=.5,rely=.5)

    # label
    self.label = ttk.Label(self, text='Hello, Tkinter!')
    self.label.place(relx=.5,rely=.1)

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.place(relx=.8,rely=.2)
    label_file_explorer = ttk.Label(frame1, text = "File Explorer using Tkinter")
    label_file_explorer.pack()
    #self.button['command'] = self.button_clicked
    button_explore = ttk.Button(frame1, text = "Browse Files", command = (lambda: self.browseFiles(label_file_explorer)))
    
    button_explore.pack()
    
    clicked = StringVar(self)
    clicked.set("Select an analysis option")
    data_analysis_ddl = OptionMenu(self, clicked, *analysis_options)
    
    data_analysis_ddl.grid(row=4,column=5)

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')
    

  def browseFiles(self, label_file_explorer):
    filename = filedialog.askopenfilename()
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

  
if __name__ == "__main__":
  app = App()
  app.mainloop()