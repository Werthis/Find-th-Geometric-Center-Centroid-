import tkinter as tk
from tkinter import *
import find_geometric_center as find_geo

class GuiGeometric():

    def __init__(self, backend):
        self._backend = backend
        self._numbers_from_entry = []    
        self.coordinates_list = []

        # self.root

        self.window = tk.Tk()
        self.window.title('Geometric Center Finder')
        self.window.geometry('400x400')

        self.coordinates_info = tk.StringVar()

        info_label = tk.Label(self.window, text='Geometric Center Finder', font=('arial', 14))

        put_two_numbers = tk.Label(self.window, text='put coordinates here:', font=('arial', 12))

        info_label.pack()
        put_two_numbers.pack()

        for i in range(1, self._backend._number_of_points + 1):
            coordinates_label = tk.Label(self.window, text=f'Dimension {i}', font=('arial', 12))
            coordinates_label.pack()

            self.number = tk.StringVar()
            coordination_entry = tk.Entry(self.window,  textvariable = self.number, font=('arial', 12))
            coordination_entry.pack()
            self._numbers_from_entry.append(self.number)



        button_take_numbers = tk.Button(self.window, text='Submit', command=self.take_values)
        button_take_numbers.pack()

        label_print = tk.Label(self.window, textvariable = self.coordinates_info, font=('arial', 12))
        label_print.pack()


    # def write_numbers_from_entry(self):

    def take_values(self):
        for i in self._numbers_from_entry:
            self.coordinates_list.append(i.get())
        self.coordinates_info.set(f'point is {self.coordinates_list}')

    def start(self):
        self.window.mainloop()


if __name__ == "__main__":
    list_of_points = [(1, 11), (2, 2), (5, 1), (1, 1)]
    backend = find_geo.GeometricCenter(list_of_points)
    app = GuiGeometric(backend)
    app.start()
    