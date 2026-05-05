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
    def __init__ (self, name, pax, cater_package, cost):
        self.name = name
        self.pax = pax
        self.cater_package = cater_package
        self.cost = cost                    

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

        # PARENT

        cater_name_lbl = Label(parent, text="Rhon's Catering", bg = "lightblue", height = 3, wraplength = 200, font = ("arial", 9))
        self.navigation_menu = OptionMenu(parent, self.menu_options_val, *self.menu_options, command = self.switch_frames)
        self.navigation_menu.configure(highlightthickness = 0)
        self.editing_order_lbl = Label(parent, text = "Editing Order...", bg = "lightblue")


        cater_name_lbl.grid(row = 0, column = 0, padx = 62)
        self.navigation_menu.grid(row = 0, column = 3, padx = 62, pady = 15)

        # HOME FRAME
        self.home_frame = Frame(parent)
        title_lbl = Label(self.home_frame, text = "Welcome to Rhon's Catering!", font = ("Times", 18, "bold"))
        subtitle_lbl = Label(self.home_frame, text = "Below are the available catering packages that you can order.")
        package_lbl = Label(self.home_frame, text = "Catering Packages:", font = ('Arial', 11, 'underline'))

        self.home_frame.grid(row = 1, column = 0, columnspan = 4)
        title_lbl.grid(row = 2, column = 0, columnspan = 3)
        subtitle_lbl.grid(row = 3, column = 0, columnspan = 3, pady = 2)
        package_lbl.grid(row = 4, column = 0, sticky = W)
        self.create_package_labels()

        # ORDERING FRAME
        self.calculated_cost = 0

        self.place_order_frame = Frame(parent)

        name_lbl = Label(self.place_order_frame, text = "First Name:")
        number_ppl_lbl = Label(self.place_order_frame, text = "How many people? (8-100 pax)")
        self.name_entry = Entry(self.place_order_frame)
        self.number_ppl_entry = Entry(self.place_order_frame)
        package_lbl = Label(self.place_order_frame, text = "Cater Package:")
        pax_lbl = Label(self.place_order_frame, text = "Pax Cost:")
        self.package_opt_menu = OptionMenu(self.place_order_frame, self.cater_packages_val, *[package.name for package in self.catering_packages], command = lambda choice: self.update_pax(choice, "place")) # list comprehension                  
        self.pax_cost_lbl = Label(self.place_order_frame, text = f"${self.selected_package.pax_cost:.2f}") 
        self.calculate_btn = Button(self.place_order_frame, text = "Calculate Order Cost", command = self.calculate_cost) # make an error pop-up for every invalid input

        name_lbl.grid(row = 2, column = 0, padx = 51, pady = 3)
        number_ppl_lbl.grid(row = 2, column = 2, padx = 51, pady = 3)
        self.name_entry.grid(row = 3, column = 0, padx = 51, pady = 3)
        self.number_ppl_entry.grid(row = 3, column = 2, padx = 51, pady = 3)      
        package_lbl.grid(row = 4, column = 0, padx = 51, pady = 3)   
        pax_lbl.grid(row = 4, column = 2, padx = 51, pady = 3) 
        self.package_opt_menu.grid(row = 5, column = 0, padx = 51, pady = 3) 
        self.pax_cost_lbl.grid(row = 5, column = 2, padx = 51, pady = 3)
        self.calculate_btn.grid(row = 6, column = 0, columnspan=4, pady = 7)


        # VIEW ORDERS FRAME
        self.view_order_frame = Frame(parent)

        user_orders_lbl = Label(self.view_order_frame, text = "Order/s that you have made:")
        name_lbl = Label(self.view_order_frame, text = "First Name:")
        number_ppl_lbl = Label(self.view_order_frame, text = "Number of People:")
        self.user_name_lbl = Label(self.view_order_frame, text = "No data found yet")
        self.user_pax_lbl = Label(self.view_order_frame, text = "No data found yet")
        package_lbl = Label(self.view_order_frame, text = "Cater Package:")
        pax_lbl = Label(self.view_order_frame, text = "Order Cost:")
        self.user_package_lbl = Label(self.view_order_frame, text = "No data found yet")
        self.user_cost_lbl = Label(self.view_order_frame, text = "No data found yet")
        self.prev_btn = Button(self.view_order_frame, text = "Previous", command = lambda: self.switch_orders(-1))
        self.edit_btn = Button(self.view_order_frame, text = "Modify Order", command = lambda: self.switch_frames("Modify Order"))
        self.next_btn = Button(self.view_order_frame, text = "Next", command = lambda: self.switch_orders(1))


        user_orders_lbl.grid(row = 2, column = 0, padx = 39, pady = 3)
        name_lbl.grid(row = 3, column = 0, padx = 39, pady = 3)
        number_ppl_lbl.grid(row = 3, column = 2, padx = 39, pady = 3)  
        self.user_name_lbl.grid(row = 4, column = 0, padx = 39, pady = 3)
        self.user_pax_lbl.grid(row = 4, column = 2, padx = 39, pady = 3)  
        package_lbl.grid(row = 5, column = 0, padx = 39, pady = 3)
        pax_lbl.grid(row = 5, column = 2, padx = 39, pady = 3)
        self.user_package_lbl.grid(row = 6, column = 0, padx = 39, pady = 3)
        self.user_cost_lbl.grid(row = 6, column = 2, padx = 39, pady = 3)
        self.prev_btn.grid(row = 7, column = 0, padx = 39, pady = 3)
        self.edit_btn.grid(row = 7, column = 1, pady = 3)
        self.next_btn.grid(row = 7, column = 2, padx = 39, pady = 3)

        # MODIFY FRAME
        self.modify_order_frame  = Frame(parent)

        name_lbl = Label(self.modify_order_frame, text = "First Name:")
        number_ppl_lbl = Label(self.modify_order_frame, text = "How many people? (8-100 pax)")
        self.modify_name_entry = Entry(self.modify_order_frame)
        self.modify_pax_entry = Entry(self.modify_order_frame)
        package_lbl = Label(self.modify_order_frame, text = "Cater Package:")
        pax_lbl = Label(self.modify_order_frame, text = "Pax Cost:")
        self.modify_package = OptionMenu(self.modify_order_frame, self.cater_packages_val, *[package.name for package in self.catering_packages], command = lambda choice: self.update_pax(choice, "modify")) # list comprehension
        self.modify_pax_cost_lbl = Label(self.modify_order_frame, text = f"${self.selected_package.pax_cost:.2f}") 
        self.modify_order_btn = Button(self.modify_order_frame, text = "Modify Order", command = self.modify_order)
        self.return_back_btn = Button(self.modify_order_frame, text = "Return Back", command = lambda: self.switch_frames("Return to Frame"))
        self.cancel_order_btn = Button(self.modify_order_frame, text = "Cancel Order", command = self.cancel_order)


        name_lbl.grid(row = 2, column = 0, padx = 20, pady = 5)
        number_ppl_lbl.grid(row = 2, column = 2, padx = 20, pady = 5)
        self.modify_name_entry.grid(row = 3, column = 0, padx = 20, pady = 5)
        self.modify_pax_entry.grid(row = 3, column = 2, padx = 20, pady = 5)
        package_lbl.grid(row = 4, column = 0, padx = 20, pady = 5)
        pax_lbl.grid(row = 4, column = 2, padx = 20, pady = 5)
        self.modify_package.grid(row = 5, column = 0, padx = 20, pady = 5)
        self.modify_pax_cost_lbl.grid(row = 5, column = 2, padx = 20, pady = 5)
        self.modify_order_btn.grid(row = 6, column = 0, padx = 20, pady = 5)
        self.return_back_btn.grid(row = 6, column = 1, padx = 20)
        self.cancel_order_btn.grid(row = 6, column = 2, padx = 20, pady = 5)

    # FUCNTIONS

    # NAVIGATING FUNCTIONS

    def switch_frames(self, selected_option):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        if selected_option == "Home":
            self.place_order_frame.grid_forget()
            self.view_order_frame.grid_forget()
            self.home_frame.grid(row = 1, column = 0, columnspan = 4)

        elif selected_option == "Place Order":
            self.home_frame.grid_forget()
            self.view_order_frame.grid_forget()
            self.reset_frame("place")
            self.name_entry.focus()
            self.place_order_frame.grid(row = 1, column = 0, columnspan = 4)

        elif selected_option == "Modify Order":
            self.view_order_frame.grid_forget()
            self.navigation_menu.grid_forget()
            self.clear_entries("modify")
            self.update_order_labels("modify")
            self.editing_order_lbl.grid(row = 0, column = 3, padx = 62, pady = 15)
            self.modify_order_frame.grid(row = 1, column = 0, columnspan = 4)

        elif selected_option == "Return to Frame":
            self.editing_order_lbl.grid_forget()
            self.modify_order_frame.grid_forget()
            self.clear_entries("modify")
            self.navigation_menu.grid(row = 0, column = 3, padx = 62, pady = 15)
            self.view_order_frame.grid(row = 1, column = 0, columnspan = 4)
            self.reset_frame("view")

        else:
            self.home_frame.grid_forget()
            self.place_order_frame.grid_forget()                                       
            self.check_orders()            
            self.view_order_frame.grid(row = 1, column = 0, columnspan = 4)
    
    def switch_orders(self, amount):
        self.order_index += amount
        self.check_order_index()
        self.update_order_labels("view")

    # MODIFYING FUNCTIONS
    
    def modify_order(self):
        new_name = self.get_name_entry("modify")
        if new_name == 'error':
            return
        else:
            new_cater_package = self.selected_package.name
            try:
                new_pax = int(self.modify_pax_entry.get())
                if new_pax >= 8 and new_pax <= 100:
                    new_order_cost = self.selected_package.calculate_cost(new_pax) 
                    modify = messagebox.askyesno("Modify order?", f"These are the values you have inputted:\n\nFirst name: {new_name}\nNumber of people: {new_pax}\n"
                                            f"Cater package chosen: {new_cater_package}\nNew final cost: ${new_order_cost:.2f}\n\nAre you sure you want to modify this order?")
                    if modify:
                        messagebox.showinfo("Order succesfully modified", "Your order has been modified!")
                        current_selected_order = self.user_orders[self.order_index]
                        current_selected_order.name = new_name
                        current_selected_order.pax = new_pax
                        current_selected_order.cater_package = new_cater_package
                        current_selected_order.cost = new_order_cost
                        self.switch_frames("Return to Frame")
                    else:
                        messagebox.showinfo("Action cancelled", "Order was not modified.")
                elif new_pax <= 0:
                    messagebox.showerror("Number cannot be zero or less than zero", "Please enter an integer greater than 8!")
                    self.clear_entries("modify_pax")
                elif 0 < new_pax < 8:
                    messagebox.showerror("Number cannot be less than 8", "Please enter an integer greater than 8!")
                    self.clear_entries("modify_pax")
                else:
                    messagebox.showerror("Number cannot be greater than 100", "Please enter an integer less than 100!")
                    self.clear_entries("modify_pax") 
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid integer!")
                self.clear_entries("modify_pax") 

    def cancel_order(self):
        ensure = messagebox.askyesno("Cancelling Order", "WARNING! This will delete your order\nAre you sure?", icon = 'warning')
        if ensure:
            second_ensure = messagebox.askyesno("Cancelling Order", "Are you really sure?", icon = 'warning')
            if second_ensure:
                del self.user_orders[self.order_index]
                self.order_index = 0
                self.switch_frames("Return to Frame")
            else:
                messagebox.showinfo("Action cancelled", "You cancelled your action.")
        else:
            messagebox.showinfo("Action cancelled", "You cancelled your action.")
    
    # CALCULATING COST FUNCTIONS

    def calculate_cost(self):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        user_package = self.selected_package.name
        user_name = self.get_name_entry("place")
        if user_name == 'error':
            return
        else:
            try:
                user_pax = int(self.number_ppl_entry.get())
                if user_pax >= 8 and user_pax <= 100:
                    user_order_cost = self.catering_packages[self.package_index].calculate_cost(user_pax)
                    submit = messagebox.askyesno("Submit order?", f"Your final cost for this order is ${user_order_cost:.2f}\nDo you want to submit this order?")
                    if submit:
                        messagebox.showinfo("Order added!", "Your order has been submitted!")
                        self.user_orders.append(Order(user_name, user_pax, user_package, user_order_cost))
                        self.clear_entries("place")
                    else:
                        clear = messagebox.askyesno("Clear entries?", "Do you want to clear your entries?")
                        if clear:
                            self.clear_entries("place")
                        else:
                            self.name_entry.focus()
                elif user_pax <= 0:
                    messagebox.showerror("Number cannot be zero or less than zero", "Please enter an integer greater than 8!")
                    self.clear_entries("place")
                elif 0 < user_pax < 8:
                    messagebox.showerror("Number cannot be less than 8", "Please enter an integer greater than 8!")
                    self.clear_entries("place")
                else:
                    messagebox.showerror("Number cannot be greater than 100", "Please enter an integer less than 100!")
                    self.clear_entries("place")
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid integer!")
                self.clear_entries("place")
            
    def get_name_entry(self, frame):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        name = self.name_entry.get().strip()
        modify_name = self.modify_name_entry.get().strip()
        if frame == "place":
            if name == "":
                messagebox.showerror("Invalid name input", "Cannot be blank! Please enter a valid name.")
                self.clear_entries("place")
                return 'error'     
            elif len(name) == 1:   
                messagebox.showerror("Invalid name input", "Name must be at least 2 characters!")
                self.clear_entries("place")
                return 'error'                                               
            else:
                return name
        else:
            if modify_name == "":
                messagebox.showerror("Invalid name input", "Cannot be blank! Please enter a valid name.")
                self.clear_entries("modify_name")
                return 'error'
            elif len(modify_name) == 1:   
                messagebox.showerror("Invalid name input", "Name must be at least 2 characters!")
                self.clear_entries("modify_name")
                return 'error'                                             
            else:
                return modify_name

    # CREATING AND UPDATING UI
    
    def create_package_labels(self):
        row_count = 4                                       
        for package in self.catering_packages:              
            row_count += 1
            package_name_lbl = Label(self.home_frame, text = f'{package.name}')      
            package_menu_lbl = Label(self.home_frame, text = f'{package.menu}')
            package_cost_lbl = Label(self.home_frame, text = f'${package.pax_cost:.2f}')
            package_name_lbl.grid(row = row_count, column = 0, padx= 10, pady = 3, sticky = W)                                                   
            package_menu_lbl.grid(row = row_count, column = 1, padx = 10, pady = 3)
            package_cost_lbl.grid(row = row_count, column = 2, padx = 10, pady = 3, sticky = E)

    def reset_frame(self, frame):
        if frame == "view":
            if len(self.user_orders) != 0: 
                default_order = self.user_orders[0]
                self.user_name_lbl.configure(text = f"{default_order.name}")
                self.user_pax_lbl.configure(text = f"{default_order.pax} pax")
                self.user_package_lbl.configure(text = f"{default_order.cater_package}")
                self.user_cost_lbl.configure(text = f"${default_order.cost:.2f}")
                self.check_order_index()

            else:    
                self.user_name_lbl.configure(text = "No data found yet")
                self.user_pax_lbl.configure(text = "No data found yet")
                self.user_package_lbl.configure(text = "No data found yet")
                self.user_cost_lbl.configure(text = "No data found yet")
                self.edit_btn.configure(state = DISABLED)
        else:
            self.package_index = 0
            self.selected_package = self.catering_packages[0]

            default_package = self.catering_packages[0]
            self.cater_packages_val.set(default_package.name)
            self.pax_cost_lbl.configure(text = f'${default_package.pax_cost:.2f}')
            self.clear_entries("place")

    def update_order_labels(self, frame):
        self.selected_order = self.user_orders[self.order_index]
        count = 0
        
        if frame ==  "view":
            self.user_name_lbl.configure(text = f"{self.selected_order.name}")
            self.user_pax_lbl.configure(text = f"{self.selected_order.pax} pax")
            self.user_package_lbl.configure(text = f"{self.selected_order.cater_package}")
            self.user_cost_lbl.configure(text = f"${self.selected_order.cost:.2f}")
        else:
            self.modify_name_entry.insert(0, f'{self.selected_order.name}')
            self.modify_pax_entry.insert(0, f'{self.selected_order.pax}')
            for package in self.catering_packages:
                if self.selected_order.cater_package == package.name:
                    self.cater_packages_val.set(self.catering_packages[count].name)
                    self.package_index = count
                    self.selected_package = package
                    self.modify_pax_cost_lbl.configure(text = f'${package.pax_cost:.2f}')
                    break
                else:
                    count += 1
    
    def update_pax(self, choice, frame):
            """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
            count = 0
            if frame == "place":
                for package in self.catering_packages:
                    if choice == package.name:
                        self.pax_cost_lbl.configure(text = f'${package.pax_cost:.2f}')
                        self.clear_entries("place")
                        self.package_index = count
                        self.selected_package = package
                        break
                    else:
                        count += 1
            else:
                for package in self.catering_packages:
                    if choice == package.name:
                        self.modify_pax_cost_lbl.configure(text = f'${package.pax_cost:.2f}')
                        self.package_index = count
                        self.selected_package = package
                        break
                    else:
                        count += 1

    # CLEARING AND DISABLING BUTTONS FUNCTIONS  

    def check_orders(self):
        if len(self.user_orders) != 0: 
            self.update_order_labels("view")
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

    def clear_entries(self, frame):
        """ Placeholder docstring describing the method (REPLACE THIS!!!!!)"""
        if frame == "place":
            self.name_entry.delete(0, END)
            self.number_ppl_entry.delete(0, END)
            self.name_entry.focus()
        elif frame == "modify":
            self.modify_name_entry.delete(0, END)
            self.modify_pax_entry.delete(0, END)
        elif frame == "modify_name":
            self.modify_name_entry.delete(0, END)
            self.modify_name_entry.focus()
        else:
            self.modify_pax_entry.delete(0, END)
            self.modify_pax_entry.focus()

if __name__ == "__main__":
    root = Tk()
    app = CateringGUI(root)
    root.title("Rhon's Catering Order")
    root.configure(bg = "lightblue")
    root.mainloop()