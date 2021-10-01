
class GeometricCenter():

    def __init__(self, list_of_points):
        self._list_of_points = list_of_points
        self._number_of_points = len(self._list_of_points)
        self.geometric_center = []
        self._list_of_all_coordinates = []
        self.check_number_of_dimensions()

    def check_number_of_dimensions(self):
        for i in self._list_of_points:
            self._dimension = len(i)
        return self._dimension

    def find_geometric_center(self):
        _summ_of_one_dimension_coordinates = 0
        _coordinate_of_geo_center = 0
        if self._list_of_points != None:
            for i in range(len(self._list_of_points)):
                self._list_of_all_coordinates += self._list_of_points[i]
        for x in range(self._dimension):
            for i in range(x, len(self._list_of_all_coordinates), self._dimension):
                _summ_of_one_dimension_coordinates += self._list_of_all_coordinates[i]
            _coordinate_of_geo_center = _summ_of_one_dimension_coordinates/(self._number_of_points)
            _summ_of_one_dimension_coordinates = 0
            self.geometric_center.append(round(_coordinate_of_geo_center, 3))
        return self.geometric_center

    def gui_communication(self, all_points, number_of_dimentions, number_of_points):
        self._list_of_all_coordinates = all_points
        self._dimension = number_of_dimentions
        self._number_of_points = number_of_points
        self._list_of_points = None
        if self._dimension == 0:
            self.check_number_of_dimensions()
        message_to_gui = self.find_geometric_center()
        return message_to_gui

    def __str__(self):
        return f'Your points are: \n{self._list_of_points} \nGeometric center is \n{self.geometric_center}'

if __name__ == "__main__":
    list_of_points = []
    submit = ''
    user_input = input('Put number of dimensions: ')
    number_of_dimentions = int(user_input)

    def add_point(number_of_dimentions):
        single_point = []
        for i in range(number_of_dimentions):
            user_input = input(f'Put coordinate N {i+1}: ')
            single_point.append(int(user_input))
        list_of_points.append(single_point)
        print(f'\nList of points is: {list_of_points}\n')

    while submit != 'n' or submit != 'N':
        add_point(number_of_dimentions)
        submit = input('Would you like to add another point? (y/n): ')
        if submit == 'y':
            continue
        elif submit == 'n':
            break

    program = GeometricCenter(list_of_points)
    program.check_number_of_dimensions()
    program.find_geometric_center()
    
    print('\n', program)
