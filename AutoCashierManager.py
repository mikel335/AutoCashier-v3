import tkinter as tk
from RegisterManager import RegisterManager


class AutoCashierManager:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("AutoCashier")
    self.root.configure(background="#44505A")
    self.root.geometry("1000x700")

    self.RegFrame = tk.Frame(self.root, width=1000, height=700, bg="#44505A")
    self.RegFrame.place(relx=0, rely=0)
    self.RegPanel = RegisterManager(self.root, self.RegFrame)

if __name__ == "__main__":
  app = AutoCashierManager()
  app.mainloop()