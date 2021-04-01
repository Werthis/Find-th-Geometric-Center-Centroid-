import tkinter as tk
# from tkinter import *
# from tkinter.ttk import *
import find_geometric_center as find_geo

class MainWindow():

    def __init__(self, backend):
        self._backend = backend

        self.root = tk.Tk()
        self.root.geometry('200x200')
        self.root.title('How many dimentions do you need?')

        self.dimentions_number = tk.StringVar()


        label_dimentions_question = tk.Label(self.root, text='Write number of dimentions', font=('arial', 12))
        entry_number_of_dimentions = tk.Entry(self.root, textvariable=self.dimentions_number, font=('arial', 12))
        button_confirm_dimentions = tk.Button(self.root, text='confirm', font=('arial', 12), command = self.open_new_window)

        label_dimentions_question.pack()
        entry_number_of_dimentions.pack()
        button_confirm_dimentions.pack()

    def get_number_of_dimentions(self):
        self.number_of_dimentions = self.dimentions_number.get()

    def open_new_window(self):
        self.get_number_of_dimentions()
        self.program = SecondWindow(self.number_of_dimentions)

    def start(self):
        self.root.mainloop()


class SecondWindow():

    def __init__(self, number_of_dimentions):
        self.number_of_dimentions = int(number_of_dimentions)
        self._numbers_from_entry = []    
        self.coordinates_list = []

        self.window = tk.Tk()
        self.window.title('Geometric Center Finder')
        self.window.geometry('400x400')

        self.coordinates_info = tk.StringVar()

        label_info = tk.Label(self.window, text='Geometric Center Finder', font=('arial', 14))

        label_put_number = tk.Label(self.window, text='put coordinates here:', font=('arial', 12))

        label_info.pack()
        label_put_number.pack()

        for i in range(1, self.number_of_dimentions + 1):
            coordinates_label = tk.Label(self.window, text=f'Dimension {i}', font=('arial', 12))
            coordinates_label.pack()

            self.number = tk.StringVar()
            coordination_entry = tk.Entry(self.window,  textvariable = self.number, font=('arial', 12))
            coordination_entry.pack()
            self._numbers_from_entry.append(self.number)
        print(self._numbers_from_entry)

        button_take_numbers = tk.Button(self.window, text='Submit', command=self.take_values)
        button_take_numbers.pack()

        label_print = tk.Label(self.window, textvariable = self.coordinates_info, font=('arial', 12))
        label_print.pack()

        self.window.mainloop()

    def take_values(self):
        for i in self._numbers_from_entry:
            self.coordinates_list.append(i.get())
        print(self.coordinates_list)

        self.coordinates_info.set(f'point is {self.coordinates_list}')


if __name__ == "__main__":
    list_of_points = [(1, 11), (2, 2), (5, 1), (1, 1)]
    backend = find_geo.GeometricCenter(list_of_points)
    app = MainWindow(backend)
    app.start()
    