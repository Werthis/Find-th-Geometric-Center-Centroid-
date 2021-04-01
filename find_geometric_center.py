import math

class GeometricCenter():

    def __init__(self, list_of_points):
        self._list_of_points = list_of_points
        self._number_of_points = len(self._list_of_points)
        self.check_number_of_dimensions()
        self.geometric_center = []

    def check_number_of_dimensions(self):
        for i in self._list_of_points:
            self.dimension = len(i)
        return self.dimension

    def find_geometric_center(self):
        _list_of_all_coordinates = []
        _summ_of_one_dimension_coordinates = 0
        _coordinate_of_geo_center = 0

        for i in range(len(self._list_of_points)):
            _list_of_all_coordinates += self._list_of_points[i]
        for x in range(self.dimension):
            for i in range(x, len(_list_of_all_coordinates), self.dimension):
                _summ_of_one_dimension_coordinates += _list_of_all_coordinates[i]
            _coordinate_of_geo_center = _summ_of_one_dimension_coordinates/(self._number_of_points)
            _summ_of_one_dimension_coordinates = 0
            self.geometric_center.append(round(_coordinate_of_geo_center, 3))
        return self.geometric_center

    def __str__(self):
        return f'Geometric center of points: {self._list_of_points} is {self.geometric_center}'


if __name__ == "__main__":
    list_of_points = [(1,1), (2, 2), (3, 1)]
    program = GeometricCenter(list_of_points)
    program.find_geometric_center()
    print(program)
