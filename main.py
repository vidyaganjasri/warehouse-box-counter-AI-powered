import tkinter as tk
from gui.app_gui import WarehouseApp

def main():
    root = tk.Tk()
    app = WarehouseApp(root)  # App itself handles detection & counting flow internally
    root.mainloop()

if __name__ == "__main__":
    main()
