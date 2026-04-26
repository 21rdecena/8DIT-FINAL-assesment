"""" Placeholder docstring introducing the program (REPLACE THIS!!!!!) """

from tkinter import *

class CaterPackage:
    def __init__ (self, name, menu, pax_cost):
        self.name = name
        self.menu = menu
        self.pax_cost = pax_cost            # round up the costs to dollars
    
    def display_packages(self):
        return f'{self.name}     {self.menu}     ${self.pax_cost:.2f}'

class Order:
    def __init__ (self, name, num_of_ppl, cater_package, cost):
        self.name = name
        self.num_of_ppl = num_of_ppl
        self.cater_package = cater_package
        self.cost = cost                    # round up the costs to dollars

class CateringGUI:
    def __init__ (self, parent):
        """ ask mr harding if __init__ needs a docstring"""
        # values
        catering_packages = [CaterPackage("Corporate Lunch", "Garlic Pesto Pasta, Garlic Bread, Iced Lemon Tea ", 20),
                             CaterPackage("Wedding Dinner", "Grilled Sirloin Steak, Mashed Potatoes, Sparkling Water ", 40),
                             CaterPackage("Children's Birthday", "Pepperoni Pizza, French Fries, Fresh Orange Juice ", 30)]
        menu_selections = ['home', 'place']
        self.menu_val = StringVar()
        self.menu_val.set(menu_selections[0])

        # parent
        cater_lbl = Label(parent, text="Rhon's Catering")
        cater_lbl.grid()

        menu_option = OptionMenu(parent, self.menu_val, *menu_selections, command = self.switch_frames())
        menu_option.grid()

        # home frame
        self.home_frame = Frame(parent)
        self.home_frame.grid()

        title_lbl = Label(self.home_frame, text = "Welcome to Rhon's Catering!")
        title_lbl.grid()

        subtitle_lbl = Label(self.home_frame, text = "Short subtitle text introducing the GUI to the User")
        subtitle_lbl.grid()

        package_lbl = Label(self.home_frame, text = "Catering Packages")
        package_lbl.grid()

        for package in catering_packages:
            cater_packages_lbl = Label(self.home_frame, text = f'{package.display_packages()}')
            cater_packages_lbl.grid()
        
        # ordering frame
        self.place_order_frame = Frame(parent)

        test_lbl = Label(self.place_order_frame, text = "Testing Label!")
        test_lbl.grid()


    def switch_frames(self):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!) """
        if self.menu_val.get() == "place":
            self.home_frame.grid_forget()
            self.place_order_frame.grid()

        else:
            self.place_order_frame.grid_forget()
            self.home_frame.grid()



if __name__ == "__main__":
    root = Tk()
    app = CateringGUI(root)
    root.mainloop()