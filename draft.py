from tkinter import *

class Order:
    def __init__ (self, name, num_of_ppl, cater_package, cost):
        self.name = name
        self.num_of_ppl = num_of_ppl
        self.cater_package = cater_package
        self.cost = cost

class OrderGUI:
    def __init__ (self, parent):
        test_lb = Label(parent, text="Hello World!")
        test_lb.pack()


if __name__ == "__main__":
    root = Tk()
    app = OrderGUI(root)
    root.mainloop()