import find_geometric_center as center
import kivy_gui_find_geometric_center as kivy


if __name__ == '__main__':
    list_of_points = [(1, 1), (1, 1)]
    backend = center.GeometricCenter(list_of_points)
    app = kivy.GeometricCenterApp(backend)
    app.start_app()
