import tkinter.ttk as ttk
import tkinter as tk
import math
from api import fetch_resource_names, ResourceType

class ui:
    def __init__(self, master=None):
        self.scarab_values = fetch_resource_names(ResourceType.SCARAB)
        self.compass_values = fetch_resource_names(ResourceType.COMPASS)
        self.mapset_frame = ttk.Frame(master, name="mapset_frame")
        self.mapset_frame.configure(height=200, width=200)
        
        self.label_scarab_one = ttk.Label(self.mapset_frame, name="label_scarab_one")
        self.label_scarab_one.configure(text='Scarab 1')
        self.label_scarab_one.grid(column=0, padx=10, row=0)
        self.choice_scarab_one = tk.StringVar(self.mapset_frame)
        self.choice_scarab_one.set("Scarab 1 Option")     
        self.dropdown_scarab_one = ttk.OptionMenu(self.mapset_frame, self.choice_scarab_one, *self.scarab_values)
        self.dropdown_scarab_one.grid(column=1, padx=10, pady=10, row=0)
        
        self.label_scarab_two = ttk.Label(self.mapset_frame, name="label_scarab_two")
        self.label_scarab_two.configure(text='Scarab 2')
        self.label_scarab_two.grid(column=0, row=1)
        self.choice_scarab_two = tk.StringVar(self.mapset_frame)
        self.choice_scarab_two.set("Scarab 2 Option")
        self.dropdown_scarab_two = ttk.OptionMenu(self.mapset_frame, self.choice_scarab_two,  *self.scarab_values)
        self.dropdown_scarab_two.grid(column=1, padx=10, pady=10, row=1)
        
        self.label_scarab_three = ttk.Label(self.mapset_frame, name="label_scarab_three")
        self.label_scarab_three.configure(text='Scarab 3')
        self.label_scarab_three.grid(column=0, row=2)
        self.choice_scarab_three = tk.StringVar(self.mapset_frame)
        self.choice_scarab_three.set("Scarab 3 Option")
        self.dropdown_scarab_three = ttk.OptionMenu(self.mapset_frame, self.choice_scarab_three, *self.scarab_values)
        self.dropdown_scarab_three.grid(column=1, padx=10, pady=10, row=2)
        
        self.label_scarab_four = ttk.Label(self.mapset_frame, name="label_scarab_four")
        self.label_scarab_four.configure(text='Scarab 4')
        self.label_scarab_four.grid(column=0, row=3)
        self.choice_scarab_four = tk.StringVar(self.mapset_frame)
        self.choice_scarab_four.set("Scarab 4 Option")
        self.dropdown_scarab_four = ttk.OptionMenu(self.mapset_frame, self.choice_scarab_four,  *self.scarab_values)
        self.dropdown_scarab_four.grid(column=1, padx=10, pady=10, row=3)
        
        self.label_compass_one = ttk.Label(self.mapset_frame, name="label_compass_one")
        self.label_compass_one.configure(text='Compass 1')
        self.label_compass_one.grid(column=2, padx=10, pady=10, row=0)
        self.choice_compass_one = tk.StringVar(self.mapset_frame)
        self.choice_compass_one.set("Compass 1 Option")
        self.dropdown_compass_one = ttk.OptionMenu(self.mapset_frame, self.choice_compass_one, *self.compass_values)
        self.dropdown_compass_one.grid(column=3, padx=10, pady=10, row=0)
        
        self.label_compass_two = ttk.Label(self.mapset_frame, name="label_compass_two")
        self.label_compass_two.configure(text='Compass 2')
        self.label_compass_two.grid(column=2, row=1)
        self.choice_compass_two = tk.StringVar(self.mapset_frame)
        self.choice_compass_two.set("Compass 2 Option")
        self.dropdown_compass_two = ttk.OptionMenu(self.mapset_frame, self.choice_compass_two, *self.compass_values)
        self.dropdown_compass_two.grid(column=3, padx=10, pady=10, row=1)
        
        self.label_compass_three = ttk.Label(self.mapset_frame, name="label_compass_three")
        self.label_compass_three.configure(text='Compass 3')
        self.label_compass_three.grid(column=2, row=2)
        self.choice_compass_three = tk.StringVar(self.mapset_frame)
        self.choice_compass_three.set("Compass 3 Option")
        self.dropdown_compass_three = ttk.OptionMenu(self.mapset_frame, self.choice_compass_three, *self.compass_values)
        self.dropdown_compass_three.grid(column=3, padx=10, pady=10, row=2)
        
        self.label_compass_four = ttk.Label(self.mapset_frame, name="label_compass_four")
        self.label_compass_four.configure(text='Compass 4')
        self.label_compass_four.grid(column=2, row=3)
        self.choice_compass_four = tk.StringVar(self.mapset_frame)
        self.choice_compass_four.set("Compass 4 Option")
        self.dropdown_compass_four = ttk.OptionMenu(self.mapset_frame, self.choice_compass_four, *self.compass_values)
        self.dropdown_compass_four.grid(column=3, padx=10, pady=10, row=3)
        
        self.label_total_cost = ttk.Label(self.mapset_frame, name="label_total_cost")
        self.label_total_cost.configure(text='Total Cost')
        self.label_total_cost.grid(column=0, padx=10, pady=10, row=5)
        
        self.label_chaos = ttk.Label(self.mapset_frame, name="label_chaos")
        self.label_chaos.grid(column=1, row=5)
        
        self.label_divines = ttk.Label(self.mapset_frame, name="label_divines")
        self.label_divines.grid(column=2, row=5)
        
        self.label_total_sets = ttk.Label(self.mapset_frame, name="label_total_sets", text="Total Sets")
        self.label_total_sets.grid(column=0, row=4)
        
        self.entry_total_sets = ttk.Entry(self.mapset_frame, name="entry_total_sets")
        self.entry_total_sets.insert(0, 1)
        self.entry_total_sets.grid(column=1, row=4)
        
        self.submit = tk.Button(self.mapset_frame, text='Calculate', command=self.calculate_total) 
        self.submit.grid(column=3, row=5)
        
        self.mapset_frame.pack(side="top")

        self.mainwindow = self.mapset_frame
        
    def run(self):
        self.mainwindow.mainloop()     
        
    def calculate_total(self):
        total_scarab_chaos = int(self.scarab_values[self.choice_scarab_one.get()] \
        + self.scarab_values[self.choice_scarab_two.get()] \
        + self.scarab_values[self.choice_scarab_three.get()] \
        + self.scarab_values[self.choice_scarab_four.get()]) \
            * int(self.entry_total_sets.get())
        
        total_compass_sets_rounded = math.ceil(int(self.entry_total_sets.get()) / 4)

        total_compass_chaos = int(self.compass_values[self.choice_compass_one.get()] \
        + self.compass_values[self.choice_compass_two.get()] \
        + self.compass_values[self.choice_compass_three.get()] \
        + self.compass_values[self.choice_compass_four.get()]) \
            * total_compass_sets_rounded
        
        total_chaos = total_scarab_chaos + total_compass_chaos
        
        self.label_chaos['text'] = str(total_chaos) + "c"
        self.label_divines['text'] = str(round(total_chaos / 215, 2)) + "div"
        