"""
Group members: Moises Hernandez, Yash Gupta, Bao Nguyen, Youwei Dou
Professor: Bill Farmer
Assignment: Final Project
Date:12/
Challenges encountered:
Function of program: Keep track of and organize information. 
Specfically, keep track of employees information. 

"""
import os.path
import unittest
from unittest import TestCase

##Structure of code##
"""
Step 1: import tkinter. 
tkinter is a GUI library
which is used for creating 
GUI applications.  
"""
import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Data:
    def __init__(self):
        self.__data = []
        self.load()

    def save(self):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.__data)

    def load(self):
        if os.path.exists('data.csv'):
            with open('data.csv') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.__data.append(row)

        else:
            self.__data.extend([
                # name, gender, telephone, email
                ['Joe', 'M', '111-111-1111', 'test@yahoo.com'],
                ['Mary', 'F', '222-222-2222', 'mary@gmail.com'],
                ['John', 'M', '333-333-3333', 'john@outlook.com'],
            ])

    def values(self):
        return self.__data

    def append(self, item):
        self.__data.append(item)
        self.save()

    def get_by_index(self, index):
        return self.__data[index]

    def set_by_index(self, index, item):
        self.__data[index] = item
        self.save()

    def remove_by_index(self, index):
        del self.__data[index]
        self.save()


class UI:
    def __init__(self):
        # Window size
        window_width = 485
        window_height = 450

        # Colors for the GUI application
        color_0 = "#ffffff"  # White
        color_1 = "#000000"  # Black
        color_2 = "#e95566"  # Red

        # Create the main window for the application
        window = tk.Tk()
        window.title("")
        window.geometry(f"{window_width}x{window_height}")
        window.configure(background=color_1)
        window.resizable(width=False, height=False)
        self.window = window

        # Create a frame for the top section of the window
        frame_up = tk.Frame(window, width=window_width, height=50, bg=color_2)
        frame_up.grid(row=0, column=0, padx=0, pady=0)

        # Create a frame for the middle section of the window
        frame_down = tk.Frame(window, width=window_width, height=150, bg=color_0)
        frame_down.grid(row=1, column=0, padx=0, pady=1)

        # Create a frame for the bottom section of the window
        frame_table = tk.Frame(window, width=window_width, height=100, bg=color_1, relief="flat")
        frame_table.grid(row=2, column=0, padx=10, pady=1, sticky=tk.NW)

        tree = ttk.Treeview(frame_table, selectmode="extended", columns=['Name', 'Gender', 'Phone #', 'Email'],
                            show="headings")
        # Scrollbar so that user can scroll down if needed
        vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(column=0, row=0, sticky="nsew")
        vsb.grid(column=1, row=0, sticky="ns")
        hsb.grid(column=0, row=1, sticky="ew")
        tree.heading("#1", text='Name')
        tree.heading("#2", text='Gender')
        tree.heading("#3", text='Phone #')
        tree.heading("#4", text='Email')

        tree.column("#0", width=0)
        tree.column("#1", width=100)
        tree.column("#2", width=50)
        tree.column("#3", width=150)
        tree.column("#4", width=150)
        self.tree = tree

        ##For the Frame Table##
        """
        Using Frame
        Make a frame table which would hold the information from the user
        We will need 3 rows I believe (for phone #, email, name), which would be added within the Frame code. Additional cosmetics such as labels will be added.
        An entry bubble for the user will be made, using the Entry function.
        If we decide that we need to make dropdown options, we will do that too as needed, after discussing with our group.
        We will use similar code to have the user search for contacts as needed. 
        We will also make a table with the saved contacts. I think the code will be similar to the previosly used code, but we can ask the TA for help on that. I believe that we will use treeview, as it within the Tkinter we imported.



        """
        """Creating the widgets for upper frame by initializing the text name (App name), its height, its font with the size of font. Also, I have to choose the foreground color as black which was defined on top  """

        app_name = ttk.Label(frame_up, text="Customer Database Software", font='Verdana 17 bold')
        app_name.place(x=5, y=5)  # this will be located where the app name display at top by the order of x and y

        """Creating the widgets for lower frame which can be places to let the user input values"""
        """Define name value line"""

        """Create the search button"""
        y = 5
        y_delta = 28

        l_name = ttk.Label(frame_down, text="Name *", width=20, font='Ivy 10', anchor=tk.NW)
        l_name.place(x=10, y=y)
        e_name = ttk.Entry(frame_down, width=25, justify='left')
        e_name.place(x=80, y=y)
        self.e_name = e_name

        """Define gendervalue line"""
        y += y_delta
        l_gender = ttk.Label(frame_down, text="Gender *", width=20, font='Ivy 10', anchor=tk.NW)
        l_gender.place(x=10, y=y)
        c_gender = ttk.Combobox(frame_down, width=23)
        """Customer gender M: Male, F: Female"""
        c_gender['values'] = ['', 'M', 'F']
        c_gender.place(x=80, y=y)
        self.c_gender = c_gender

        """Define the telephone value line"""
        y += y_delta
        l_telephone = ttk.Label(frame_down, text="Phone Number", font='Ivy 10', anchor=tk.NW)
        l_telephone.place(x=10, y=y)
        e_telephone = ttk.Entry(frame_down, width=25, justify='left')
        e_telephone.place(x=80, y=y)
        self.e_telephone = e_telephone

        """Define the email value line"""
        y += y_delta
        l_email = ttk.Label(frame_down, text="Email", font='Ivy 10', anchor=tk.NW)
        l_email.place(x=10, y=y)
        e_email = ttk.Entry(frame_down, width=25, justify='left')
        e_email.place(x=80, y=y)
        self.e_email = e_email

        """Creating the view button"""
        y += y_delta
        b_view = ttk.Button(frame_down, text="VIEW", command=self.view)
        b_view.place(x=0, y=y)

        """Create the add button"""
        b_add = ttk.Button(frame_down, text="ADD", command=self.insert)
        b_add.place(x=100, y=y)

        """Create the update button"""
        b_update = ttk.Button(frame_down, text="UPDATE", command=self.update)
        b_update.place(x=200, y=y)

        """Create the delete button"""
        b_delete = ttk.Button(frame_down, text="DELETE", command=self.remove)
        b_delete.place(x=300, y=y)

        self.data = Data()
        self.show()

    def mainloop(self):
        self.window.mainloop()

    def show(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for item in self.data.values():
            self.tree.insert('', 'end', values=item)

    def get_form_item(self):
        name = self.e_name.get()
        gender = self.c_gender.get()
        telephone = self.e_telephone.get()
        email = self.e_email.get()
        if name == '' or gender == '' or telephone == '' or email == '':
            # Warning user if they do not fill in data
            messagebox.showwarning('Data', 'Please fill in all fields')
            return None
        return [name, gender, telephone, email]

    def reset_form(self):
        self.e_name.delete(0, 'end')
        self.c_gender.delete(0, 'end')
        self.e_telephone.delete(0, 'end')
        self.e_email.delete(0, 'end')

    def set_form_item(self, item):
        self.reset_form()
        self.e_name.insert(0, item[0])
        self.c_gender.insert(0, item[1])
        self.e_telephone.insert(0, item[2])
        self.e_email.insert(0, item[3])

    def insert(self):
        data = self.get_form_item()
        if data != None:
            self.data.append(data)
            self.reset_form()
            self.show()
            messagebox.showinfo('Data', 'Data added successfully')

    def get_selection_index(self):
        return self.tree.index(self.tree.focus())

    def view(self):
        index = self.get_selection_index()
        if index == None:
            messagebox.showwarning('No selection', message='Please select a row in the table.')
            return
        item = self.data.get_by_index(index)
        self.set_form_item(item)

    def update(self):
        index = self.get_selection_index()
        if index == None:
            messagebox.showwarning('No selection', message='Please select a row in the table.')
            return
        item = self.get_form_item()
        self.data.set_by_index(index, item)
        self.reset_form()
        self.show()
        messagebox.showwarning('Updated', message='Selected row updated.')

    def remove(self):
        index = self.get_selection_index()
        if index == None:
            messagebox.showwarning('No selection', message='Please select a row in the table.')
            return
        self.data.remove_by_index(index)
        self.tree.selection_clear()
        self.show()
        messagebox.showwarning('Updated', message='Selected row deleted.')


class Test(TestCase):
    def test_data_class(self):
        data = Data()
        values = data.values()
        self.assertEqual(values[0][0], 'Joe')


if __name__ == '__main__':
    unittest.main(exit=False)
    UI().mainloop()
