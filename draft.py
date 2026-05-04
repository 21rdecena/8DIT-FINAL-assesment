"""" Placeholder docstring introducing the program (REPLACE THIS!!!!!) """

from tkinter import *
from tkinter import messagebox

class CaterPackage:
    def __init__ (self, name, menu, pax_cost):
        self.name = name
        self.menu = menu
        self.pax_cost = pax_cost            # round up the costs to dollars
    
    def calculate_cost(self, pax):
        return pax * self.pax_cost


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
        self.menu_options = ["Home", "Place Order", "View Order"]
        self.menu_options_val = StringVar()
        self.menu_options_val.set(self.menu_options[0])
        
        self.user_orders = []
        self.order_index = 0

        self.catering_packages = [CaterPackage("Corporate Lunch", "Garlic Pesto Pasta, Garlic Bread, Iced Lemon Tea ", 20),
                             CaterPackage("Wedding Dinner", "Grilled Sirloin Steak, Mashed Potatoes, Sparkling Water ", 40),
                             CaterPackage("Children's Birthday", "Pepperoni Pizza, French Fries, Fresh Orange Juice ", 30)]  # get length of list and add it to padding 
        self.package_index = 0
        self.selected_package = self.catering_packages[self.package_index]      # acts as a cursor through the list
        

        self.cater_packages_val = StringVar()
        self.cater_packages_val.set(self.catering_packages[0].name)

        self.menu_val = IntVar()
        self.menu_val.set(1)

        # parent
        cater_lbl = Label(parent, text="Rhon's Catering")
        cater_lbl.grid(row = 0, column = 0)

        self.editing_order_lbl = Label(parent, text = "Editing Order...")

        self.navigation_menu = OptionMenu(parent, self.menu_options_val, *self.menu_options, command = self.switch_frames)
        self.navigation_menu.grid(row = 0, column = 3)

        # home frame
        self.home_frame = Frame(parent)
        self.home_frame.grid(row = 1, column = 0, columnspan = 4)

        title_lbl = Label(self.home_frame, text = "Welcome to Rhon's Catering!")
        title_lbl.grid(row = 2, column = 0, columnspan = 2)

        subtitle_lbl = Label(self.home_frame, text = "Short subtitle text introducing the GUI to the User")
        subtitle_lbl.grid(row = 3, column = 0, columnspan = 2)

        package_lbl = Label(self.home_frame, text = "Catering Packages")
        package_lbl.grid(row = 4, column = 0)

        self.create_package_labels()

        # ordering frame
        self.calculated_cost = 0

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

        self.package_opt_menu = OptionMenu(self.place_order_frame, self.cater_packages_val, *[package.name for package in self.catering_packages], command = self.update_pax) # list comprehension
        self.package_opt_menu.grid(row = 5, column = 0)

        self.pax_cost_lbl = Label(self.place_order_frame, text = f"${self.selected_package.pax_cost:.2f}") 
        self.pax_cost_lbl.grid(row = 5, column = 2)

        '''
        maybe create some widgets that allows the user to input a date
        additional feature
        '''

        self.calculate_btn = Button(self.place_order_frame, text = "Calculate Order Cost", command = self.calculate_cost) # make an error pop-up for every invalid input
        self.calculate_btn.grid(row = 6, column = 0, columnspan=4)


        # check orders frame
        self.view_order_frame = Frame(parent)

        user_orders_lbl = Label(self.view_order_frame, text = "Order/s that you have made:")
        user_orders_lbl.grid(row = 2, column = 0)

        name_lbl = Label(self.view_order_frame, text = "First Name:")
        name_lbl.grid(row = 3, column = 0)
        
        number_ppl_lbl = Label(self.view_order_frame, text = "Number of People:")
        number_ppl_lbl.grid(row = 3, column = 2)

        self.user_name_lbl = Label(self.view_order_frame, text = "No data entered yet")
        self.user_name_lbl.grid(row = 4, column = 0)
        
        self.user_ppl_lbl = Label(self.view_order_frame, text = "No data entered yet")
        self.user_ppl_lbl.grid(row = 4, column = 2)

        package_lbl = Label(self.view_order_frame, text = "Cater Package:")
        package_lbl.grid(row = 5, column = 0)

        pax_lbl = Label(self.view_order_frame, text = "Order Cost:")
        pax_lbl.grid(row = 5, column = 2)

        self.user_package_lbl = Label(self.view_order_frame, text = "No data entered yet")
        self.user_package_lbl.grid(row = 6, column = 0)
        
        self.user_cost_lbl = Label(self.view_order_frame, text = "No data entered yet")
        self.user_cost_lbl.grid(row = 6, column = 2)

        self.prev_btn = Button(self.view_order_frame, text = "Previous", command = lambda: self.switch_orders(-1))
        self.prev_btn.grid(row = 7, column = 0)

        self.edit_btn = Button(self.view_order_frame, text = "Modify Order", command = lambda: self.switch_to_modify("modify"))
        self.edit_btn.grid(row = 7, column = 1)

        self.next_btn = Button(self.view_order_frame, text = "Next", command = lambda: self.switch_orders(1))
        self.next_btn.grid(row = 7, column = 2)

        # modify frame

        self.modify_order_frame  = Frame(parent)

        name_lbl = Label(self.modify_order_frame, text = "First Name:")
        name_lbl.grid(row = 2, column = 0)

        number_ppl_lbl = Label(self.modify_order_frame, text = "How many people?")
        number_ppl_lbl.grid(row = 2, column = 2)

        self.modify_name_entry = Entry(self.modify_order_frame)
        self.modify_name_entry.grid(row = 3, column = 0)

        self.modify_pax_entry = Entry(self.modify_order_frame)
        self.modify_pax_entry.grid(row = 3, column = 2)

        package_lbl = Label(self.modify_order_frame, text = "Cater Package:")
        package_lbl.grid(row = 4, column = 0)

        pax_lbl = Label(self.modify_order_frame, text = "Pax Cost:")
        pax_lbl.grid(row = 4, column = 2)

        self.modify_package = OptionMenu(self.modify_order_frame, self.cater_packages_val, *[package.name for package in self.catering_packages], command = self.update_pax) # list comprehension
        self.modify_package.grid(row = 5, column = 0)

        self.modify_pax_cost_lbl = Label(self.modify_order_frame, text = f"${self.selected_package.pax_cost:.2f}") 
        self.modify_pax_cost_lbl.grid(row = 5, column = 2)

        self.modify_order_btn = Button(self.modify_order_frame, text = "Modify Order")
        self.modify_order_btn.grid(row = 6, column = 0)

        self.return_back_btn = Button(self.modify_order_frame, text = "Return Back")
        self.return_back_btn.grid(row = 6, column = 1)

        self.cancel_order_btn = Button(self.modify_order_frame, text = "Cancel Order")
        self.cancel_order_btn.grid(row = 6, column = 2)

    def switch_to_modify(self, option):
        if option == "modify":
            self.view_order_frame.grid_forget()
            self.navigation_menu.grid_forget()
            self.editing_order_lbl.grid(row = 0, column = 3)
            self.modify_order_frame.grid(row = 1, column = 0, columnspan = 4)
        else:
            # forget the modify frame and return back to view order frame
            pass


    def switch_frames(self, selected_option):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        if selected_option == "Home":
            self.place_order_frame.grid_forget()
            self.view_order_frame.grid_forget()
            self.home_frame.grid(row = 1, column = 0, columnspan = 4)

        elif selected_option == "Place Order":
            self.home_frame.grid_forget()
            self.view_order_frame.grid_forget()
            self.reset_order_frame()
            self.place_order_frame.grid(row = 1, column = 0, columnspan = 4)

        else:
            self.home_frame.grid_forget()
            self.place_order_frame.grid_forget()                                        # update check order labels with user
            self.check_orders()            
            self.view_order_frame.grid(row = 1, column = 0, columnspan = 4)
        
    def reset_order_frame(self):
        default_package = self.catering_packages[0]
        self.cater_packages_val.set(default_package.name)
        self.pax_cost_lbl.configure(text = f'${default_package.pax_cost:.2f}')
        self.clear_entries()

    def create_package_labels(self):
        row_count = 4                                       
        for package in self.catering_packages:              
            row_count += 1
            package_name_lbl = Label(self.home_frame, text = f'{package.name}')      
            package_menu_lbl = Label(self.home_frame, text = f'{package.menu}')
            package_cost_lbl = Label(self.home_frame, text = f'${package.pax_cost:.2f}')
            package_name_lbl.grid(row = row_count, column = 0)                                                   
            package_menu_lbl.grid(row = row_count, column = 1)
            package_cost_lbl.grid(row = row_count, column = 2)


    def calculate_cost(self):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        user_name = self.get_name_entry()
        user_package = self.selected_package.name

        try:
            user_pax = int(self.number_ppl_entry.get())
            if user_pax >= 1:
                self.user_order_cost = self.catering_packages[self.package_index].calculate_cost(user_pax)
                submit = messagebox.askyesno("Submit order?", f"Your final cost for this order is ${self.user_order_cost:.2f}\nDo you want to submit this order?")
                if submit:
                    messagebox.showinfo("Order added!", "Your order has been submitted!")
                    self.user_orders.append(Order(user_name, user_pax, user_package, self.user_order_cost))
                    self.clear_entries()
                else:
                    clear = messagebox.askyesno("Clear entries?", "Do you want to clear your entries?")
                    if clear:
                        self.clear_entries()
                    else:
                        self.name_entry.focus()
            else:
                messagebox.showerror("Negative number found", "Please enter a valid integer!")
                self.clear_entries()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer!")
            self.clear_entries()
        

    def get_name_entry(self):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        check_name_error = False
        name = self.name_entry.get().strip()
        if name == "":
            messagebox.showerror("Invalid name input", "Please enter a valid name!")
            self.clear_entries()                                                        # maybe check for the length of the name and 
        else:
            return name

    def update_pax(self, choice):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        for package in self.catering_packages:
            if choice == package.name:
                self.pax_cost_lbl.configure(text = f'${package.pax_cost:.2f}')
                self.clear_entries()

    def check_orders(self):
        if len(self.user_orders) != 0: 
            self.update_orders()
            self.check_order_index()
    
        else:    
            self.prev_btn.configure(state = DISABLED)
            self.edit_btn.configure(state = DISABLED)
            self.next_btn.configure(state = DISABLED)
    
    def check_order_index(self):
        max_index = len(self.user_orders) - 1

        if self.order_index == 0 and len(self.user_orders) == 1:
            self.prev_btn.configure(state = DISABLED)
            self.edit_btn.configure(state = NORMAL)
            self.next_btn.configure(state = DISABLED)
        
        elif self.order_index == 0:
            self.prev_btn.configure(state = DISABLED)
            self.edit_btn.configure(state = NORMAL)
            self.next_btn.configure(state = NORMAL)

        elif self.order_index == max_index:
            self.prev_btn.configure(state = NORMAL)
            self.next_btn.configure(state = DISABLED)
        
        else:
            self.prev_btn.configure(state = NORMAL)
            self.next_btn.configure(state = NORMAL)
            

    def update_orders(self):
        self.selected_order = self.user_orders[self.order_index]

        self.user_name_lbl.configure(text = f"{self.selected_order.name}")
        self.user_ppl_lbl.configure(text = f"{self.selected_order.num_of_ppl} pax")
        self.user_package_lbl.configure(text = f"{self.selected_order.cater_package}")
        self.user_cost_lbl.configure(text = f"${self.selected_order.cost:.2f}")

    def switch_orders(self, amount):
        self.order_index += amount
        self.check_order_index()
        self.update_orders()
    

    def clear_entries(self):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        self.name_entry.delete(0, END)
        self.number_ppl_entry.delete(0, END)
        self.name_entry.focus()

if __name__ == "__main__":
    root = Tk()
    app = CateringGUI(root)
    root.mainloop()