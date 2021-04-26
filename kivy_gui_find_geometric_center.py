import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ObjectProperty

import find_geometric_center as find_geo

class MyLabel(Label):
    pass

class Button(Button):
    pass

class MyTextInput(TextInput):

    def update_padding(self, text_input, *args):
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached
        )
        text_input.padding_x = (text_input.width - text_width)/2


class Invoice(Screen):

    dimentions_number = ObjectProperty(None)
    one_point_numbers = StringProperty()
    geometric_center = StringProperty()
    button_text = StringProperty()

    def __init__(self, backend, *args, **kwargs):
        super(Invoice, self).__init__(*args, **kwargs)
        self._backend = backend
        self._list_of_textinputs = []
        self._list_of_points = []
        self._list_of_all_coordinates = []
        self.number_of_points = 0


    def change_button_text(self, state):
        texts = {'normal' : 'Submit', 'pressed' : 'Put dimensions:'}
        self.button_text = texts.get(state, '')
    
    def get_number_of_dimentions(self):
        self.number_of_dimentions = self.dimentions_number.text
        return self.number_of_dimentions

    def add(self):
        self.get_number_of_dimentions()
        try:        
            self.number_of_dimentions = int(self.number_of_dimentions)
            layout = self.ids['dimensions']
            for i in range(self.number_of_dimentions):
                _text_input = MyTextInput(text='', multiline=False)
                self._list_of_textinputs.append(_text_input)
                layout.add_widget(_text_input)
        except:
            pass
        return self.number_of_dimentions

    def get_coordinates(self):
        _list = []
        for i in self._list_of_textinputs:
            coordinate = i.text
            if coordinate == '':
                pass
            else:
                coordinate = int(coordinate)
                _list.append(coordinate)
                self._list_of_all_coordinates.append(coordinate)
            i.text = ''
        self._list_of_points.append(_list)
        self.number_of_points += 1
        self.one_point_numbers = str(self._list_of_points)

        points_labels = self.ids['points']
        _point_label = Label(text= str(_list))
        points_labels.add_widget(_point_label)

        return self.number_of_points, self._list_of_points

    def request(self):
        self.geometric_center_to_find = self._backend.gui_communication(all_points= self._list_of_all_coordinates, number_of_dimentions= self.number_of_dimentions, number_of_points= float(self.number_of_points))
        self.geometric_center = 'The geometric center is: ' + str(self.geometric_center_to_find)

class GeometricCenterApp(App):

    def __init__(self, backend):
        super(GeometricCenterApp, self).__init__()
        self._backend = backend

    def build(self):
        _app_ = Invoice(self._backend)
        _app_.change_button_text('normal')
        return _app_

    def start_app(self):
        GeometricCenterApp(self._backend).run()                


if __name__ == '__main__':
    list_of_points = [(1, 11), (2, 2), (5, 1), (1, 1)]
    backend = find_geo.GeometricCenter(list_of_points)
    app = GeometricCenterApp(backend)
    app.start_app()
