import tkinter as tk
import csv
from matplotlib import pyplot as plt
import numpy as np
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

    frame1 = tk.Frame(self,width=(screen_width),height=(screen_height),bg="blue",highlightbackground="black", highlightthickness=2)
    frame1.place(relx=.75,rely=.2)

    # label
    self.label = ttk.Label(self, text='Hello, Tkinter!')
    self.label.place(relx=.5,rely=.1)

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.place(relx=.5,rely=.2)
    label_file_explorer = ttk.Label(frame1, text = "File Explorer using Tkinter")
    label_file_explorer.pack()
    #self.button['command'] = self.button_clicked
    button_explore = ttk.Button(frame1, text = "Browse Files", command = (lambda: self.browseFiles(label_file_explorer)))
    
    if file_name is not None:
      button_process_data = ttk.Button(frame1, text = "Browse Files", command = (lambda: self.readFile))
      button_process_data.pack()
    
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

  def readFile(filename):
    f = open(filename, encoding='UTF8')
    d13c = []
    d15n = []
  
    with open(filename,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            d13c.append(row[0])
            d15n.append(int(row[1]))
  
    plt.scatter(d13c, d15n, color = 'g',s = 100)
    plt.xticks(rotation = 25)
    plt.xlabel('Carbon')
    plt.ylabel('Nitrogen')
    plt.title('Food chart', fontsize = 20)
  
    plt.show()

    f.close()

  
if __name__ == "__main__":
  app = App()
  app.mainloop()