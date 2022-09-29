import tkinter as tk
from tkinter import ttk
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

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
  app = App()
  app.mainloop()