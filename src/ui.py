import tkinter.ttk as ttk

class ui:
    def __init__(self, master=None):
        self.mapset_frame = ttk.Frame(master, name="mapset_frame")
        self.mapset_frame.configure(height=200, width=200)
        
        self.label_scarab_one = ttk.Label(self.mapset_frame, name="label_scarab_one")
        self.label_scarab_one.configure(text='Scarab 1')
        self.label_scarab_one.grid(column=0, padx=10, row=0)
        self.entry_scarab_one = ttk.Entry(self.mapset_frame, name="entry_scarab_one")
        self.entry_scarab_one.grid(column=1, padx=10, pady=10, row=0)
        
        self.label_scarab_two = ttk.Label(self.mapset_frame, name="label_scarab_two")
        self.label_scarab_two.configure(text='Scarab 2')
        self.label_scarab_two.grid(column=0, row=1)
        self.entry_scarab_two = ttk.Entry(self.mapset_frame, name="entry_scarab_two")
        self.entry_scarab_two.grid(column=1, padx=10, pady=10, row=1)
        
        self.label_scarab_three = ttk.Label(self.mapset_frame, name="label_scarab_three")
        self.label_scarab_three.configure(text='Scarab 3')
        self.label_scarab_three.grid(column=0, row=2)
        self.entry_scarab_three = ttk.Entry(self.mapset_frame, name="entry_scarab_three")
        self.entry_scarab_three.grid(column=1, padx=10, pady=10, row=2)
        
        self.label_scarab_four = ttk.Label(self.mapset_frame, name="label_scarab_four")
        self.label_scarab_four.configure(text='Scarab 4')
        self.label_scarab_four.grid(column=0, row=3)
        self.entry_scarab_four = ttk.Entry(self.mapset_frame, name="entry_scarab_four")
        self.entry_scarab_four.grid(column=1, padx=10, pady=10, row=3)
        
        self.label_compass_one = ttk.Label(self.mapset_frame, name="label_compass_one")
        self.label_compass_one.configure(text='Compass 1')
        self.label_compass_one.grid(column=2, padx=10, pady=10, row=0)
        self.entry_compass_one = ttk.Entry(self.mapset_frame, name="entry_compass_one")
        self.entry_compass_one.grid(column=3, padx=10, pady=10, row=0)
        
        self.label_compass_two = ttk.Label(self.mapset_frame, name="label_compass_two")
        self.label_compass_two.configure(text='Compass 2')
        self.label_compass_two.grid(column=2, row=1)
        self.entry_compass_two = ttk.Entry(self.mapset_frame, name="entry_compass_two")
        self.entry_compass_two.grid(column=3, row=1)
        
        self.label_compass_three = ttk.Label(self.mapset_frame, name="label_compass_three")
        self.label_compass_three.configure(text='Compass 3')
        self.label_compass_three.grid(column=2, row=2)
        self.entry_compass_three = ttk.Entry(self.mapset_frame, name="entry_compass_three")
        self.entry_compass_three.grid(column=3, row=2)
        
        self.label_compass_four = ttk.Label(self.mapset_frame, name="label_compass_four")
        self.label_compass_four.configure(text='Compass 4')
        self.label_compass_four.grid(column=2, row=3)
        self.entry_compass_four = ttk.Entry(self.mapset_frame, name="entry_compass_four")
        self.entry_compass_four.grid(column=3, row=3)
        
        self.label_total_cost = ttk.Label(self.mapset_frame, name="label_total_cost")
        self.label_total_cost.configure(text='Total Cost')
        self.label_total_cost.grid(column=0, padx=10, pady=10, row=4)
        
        self.label_chaos = ttk.Label(self.mapset_frame, name="label_chaos")
        self.label_chaos.grid(column=2, row=4)
        
        self.label_divines = ttk.Label(self.mapset_frame, name="label_divines")
        self.label_divines.grid(column=3, row=4)
        
        self.mapset_frame.pack(side="top")

        self.mainwindow = self.mapset_frame

    def run(self):
        self.mainwindow.mainloop()