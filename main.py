import tkinter as tk
from src.manage import Manager

def main():
    root = tk.Tk()
    app = Manager(root)
    root.mainloop()

if __name__ == "__main__":
    main()