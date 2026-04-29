"""" Placeholder docstring introducing the program (REPLACE THIS!!!!!) """

from tkinter import *
from tkinter import messagebox

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
        user_orders = []

        self.catering_packages = [CaterPackage("Corporate Lunch", "Garlic Pesto Pasta, Garlic Bread, Iced Lemon Tea ", 20),
                             CaterPackage("Wedding Dinner", "Grilled Sirloin Steak, Mashed Potatoes, Sparkling Water ", 40),
                             CaterPackage("Children's Birthday", "Pepperoni Pizza, French Fries, Fresh Orange Juice ", 30)]  # get length of list and add it to padding

        self.cater_packages_val = StringVar()
        self.cater_packages_val.set(self.catering_packages[0].name)

        self.menu_val = IntVar()
        self.menu_val.set(1)

        self.package_index = 0

        # parent
        cater_lbl = Label(parent, text="Rhon's Catering")
        cater_lbl.grid(row = 0, column = 0)

        home_rb = Radiobutton(parent, text = "Home", variable = self.menu_val, value = 1, command = self.switch_frames)
        home_rb.grid(row = 0, column = 1)

        place_order_rb = Radiobutton(parent, text = "Place Order", variable = self.menu_val, value = 2, command = self.switch_frames)
        place_order_rb.grid(row = 0, column = 2)

        check_orders_rb = Radiobutton(parent, text = "Check Orders", variable = self.menu_val, value = 3, command = self.switch_frames)
        check_orders_rb.grid(row = 0, column = 3)

        # home frame
        self.home_frame = Frame(parent)
        self.home_frame.grid(row = 1, column = 0, columnspan = 4)

        title_lbl = Label(self.home_frame, text = "Welcome to Rhon's Catering!")
        title_lbl.grid(row = 2, column = 0, columnspan = 2)

        subtitle_lbl = Label(self.home_frame, text = "Short subtitle text introducing the GUI to the User")
        subtitle_lbl.grid(row = 3, column = 0, columnspan = 2)

        package_lbl = Label(self.home_frame, text = "Catering Packages")
        package_lbl.grid(row = 4, column = 0)

        for package in self.catering_packages:
            cater_packages_lbl = Label(self.home_frame, text = f'{package.display_packages()}')       # it would be better to change this so each instance variable
            cater_packages_lbl.grid(sticky = W)                                                       # within the object has seperate labels, allowing for padding on each
        
        # ordering frame
        self.place_order_frame = Frame(parent)

        name_lbl = Label(self.place_order_frame, text = "First Name:")
        name_lbl.grid(row = 2, column = 0)

        number_ppl_lbl = Label(self.place_order_frame, text = "How many people?")
        number_ppl_lbl.grid(row = 2, column = 2)

        self.name_entry = Entry(self.place_order_frame)
        self.name_entry.grid(row = 3, column = 0)

        self.number_ppl_entry = Entry(self.place_order_frame)
        self.number_ppl_entry.grid(row = 3, column = 2)

        package_lbl = Label(self.place_order_frame, text = "Cater Package:")
        package_lbl.grid(row = 4, column = 0)

        pax_lbl = Label(self.place_order_frame, text = "Pax Cost:")
        pax_lbl.grid(row = 4, column = 2)

        package_opt_menu = OptionMenu(self.place_order_frame, self.cater_packages_val, *[package.name for package in self.catering_packages], command = self.update_pax) # list comprehension
        package_opt_menu.grid(row = 5, column = 0)

        self.pax_cost_lbl = Label(self.place_order_frame, text = f"${self.catering_packages[self.package_index].pax_cost:.2f}") # probably want to polish this in the future
        self.pax_cost_lbl.grid(row = 5, column = 2)

        '''
        maybe create some widgets that allows the user to input a date
        additional feature
        '''

        self.final_cost_lbl = Label(self.place_order_frame, text = "Order not yet calculated.")
        self.final_cost_lbl.grid(row = 6, column = 0, columnspan = 3)

        self.calculate_btn = Button(self.place_order_frame, text = "Calculate Cost", command = self.calculate_cost) # make an error pop-up for every invalid input
        self.calculate_btn.grid(row = 7, column = 0, columnspan=2)

        self.submit_btn = Button(self.place_order_frame, text = "Submit Order", state = DISABLED, command = self.submit_order) # create a pop-up that asks the user if they want to submit their order
        self.submit_btn.grid(row = 7, column = 2, columnspan=2)

        # check orders frame
        self.check_order_frame = Frame(parent)

        user_orders_lbl = Label(self.check_order_frame, text = "Order/s that you have made:")
        user_orders_lbl.grid(row = 2, column = 0)

        name_lbl = Label(self.check_order_frame, text = "First Name:")
        name_lbl.grid(row = 3, column = 0)
        
        number_ppl_lbl = Label(self.check_order_frame, text = "Number of People:")
        number_ppl_lbl.grid(row = 3, column = 2)

        self.user_name_lbl = Label(self.check_order_frame, text = "Lorem ipsum")
        self.user_name_lbl.grid(row = 4, column = 0)
        
        self.user_ppl_lbl = Label(self.check_order_frame, text = "Lorem ipsum")
        self.user_ppl_lbl.grid(row = 4, column = 2)

        package_lbl = Label(self.check_order_frame, text = "Cater Package:")
        package_lbl.grid(row = 5, column = 0)

        pax_lbl = Label(self.check_order_frame, text = "Pax Cost:")
        pax_lbl.grid(row = 5, column = 2)

        self.user_package_lbl = Label(self.check_order_frame, text = "Lorem ipsum")
        self.user_package_lbl.grid(row = 6, column = 0)
        
        self.user_pax_lbl = Label(self.check_order_frame, text = "Lorem ipsum")
        self.user_pax_lbl.grid(row = 6, column = 2)

        self.prev_btn = Button(self.check_order_frame, text = "Previous")
        self.prev_btn.grid(row = 7, column = 0)

        self.next_btn = Button(self.check_order_frame, text = "Next")
        self.next_btn.grid(row = 7, column = 2)



    def switch_frames(self):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        if self.menu_val.get() == 1:
            #print("Switched to frame one!")
            self.place_order_frame.grid_forget()
            self.check_order_frame.grid_forget()
            self.home_frame.grid(row = 1, column = 0, columnspan = 4)

        elif self.menu_val.get() == 2:
            #print("Switched to frame two!")
            self.home_frame.grid_forget()
            self.check_order_frame.grid_forget()
            self.place_order_frame.grid(row = 1, column = 0, columnspan = 4)

        else:
            self.home_frame.grid_forget()
            self.place_order_frame.grid_forget()                                        # update check order labels with user
            self.check_order_frame.grid(row = 1, column = 0, columnspan = 4)
            #print("Switched to frame three!")
        
    
    def calculate_cost(self):
        print("Calculated cost!")
        self.submit_btn.configure(state = NORMAL)

    def submit_order(self):
        print("Submitted order!")
        self.submit_btn.configure(state = DISABLED)
        # clear entries and reset option menu when finished

    def update_pax(self, choice):
        for package in self.catering_packages:
            if choice == package.name:
                self.pax_cost_lbl.configure(text = f'${package.pax_cost:.2f}')
        #print("Updated labels!")


if __name__ == "__main__":
    root = Tk()
    app = CateringGUI(root)
    root.mainloop()