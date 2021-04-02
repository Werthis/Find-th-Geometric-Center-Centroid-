import tkinter as tk
# from tkinter import *
import find_geometric_center as find_geo

class GuiGeometric():

    def __init__(self, backend):
        self._backend = backend
        self._numbers_from_entry = []    
        self.coordinates_list = []
        self.list_of_points = []

        self.window = tk.Tk()
        self.window.title('Geometric Center Finder')

        self.coordinates_info = tk.StringVar()
        self.dimentions_number = tk.StringVar()

        info_label = tk.Label(self.window, text='Geometric Center Finder', font=('arial', 14))
        label_dimentions_question = tk.Label(self.window, text='Write number of dimentions', font=('arial', 12))
        entry_number_of_dimentions = tk.Entry(self.window, textvariable=self.dimentions_number, font=('arial', 12))
        button_confirm_dimentions = tk.Button(self.window, text='confirm', font=('arial', 12), command = self.make_new_widgets)

        info_label.pack()
        label_dimentions_question.pack()
        entry_number_of_dimentions.pack()
        button_confirm_dimentions.pack()

    def get_number_of_dimentions(self):
        self.str_number_of_dimentions = self.dimentions_number.get()
        self.number_of_dimentions = int(self.str_number_of_dimentions)

    def make_new_widgets(self):
        self.get_number_of_dimentions()

        self.put_two_numbers = tk.Label(self.window, text='put coordinates here:', font=('arial', 12))
        self.put_two_numbers.pack()

        for i in range(1, self.number_of_dimentions + 1):
            coordinates_label = tk.Label(self.window, text=f'Dimension {i}', font=('arial', 12))
            coordinates_label.pack()

            self.number = tk.StringVar()
            coordination_entry = tk.Entry(self.window,  textvariable = self.number, font=('arial', 12))
            coordination_entry.pack()
            self._numbers_from_entry.append(self.number)


        button_take_numbers = tk.Button(self.window, text='Add point', command=self.take_values)
        button_take_numbers.pack()

        label_print = tk.Label(self.window, textvariable = self.coordinates_info, font=('arial', 12))
        label_print.pack()

        self.listbox_of_coordinates = tk.Listbox(self.window, height=5)
        self.listbox_of_coordinates.pack()

        button_send_all_to_backend = tk.Button(self.window, text='Submit', command=self.backend_communication)
        button_send_all_to_backend.pack()


    def take_values(self):
        for i in self._numbers_from_entry:
            self.coordinates_list.append(int(i.get()))
            i.set('')
        self.list_of_points += self.coordinates_list
        self.coordinates_info.set(f'new point is {self.coordinates_list}')
        print(self.list_of_points)
        self.listbox_of_coordinates.insert(0, self.coordinates_list)
        self.coordinates_list.clear()
        return self.list_of_points

    def backend_communication(self):
        print(self.list_of_points)
        number_of_points = (len(self.list_of_points)/self.number_of_dimentions)

        list_for_backend = self._backend.gui_communication(all_points = self.list_of_points, number_of_dimentions = self.number_of_dimentions, number_of_points= number_of_points)
        print(list_for_backend)

        return list_for_backend

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    list_of_points = [(1, 11), (2, 2), (5, 1), (1, 1)]
    backend = find_geo.GeometricCenter(list_of_points)
    app = GuiGeometric(backend)
    app.start()
