import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.garden.mapview import MapView, MapMarker

from kivy.properties import NumericProperty

kivy.require('1.10.0')

class MapView_new(FloatLayout):


    def button_press(self, id):
        latitude_map = self.ids['latitude_map']
        longitude_map = self.ids['longitude_map']
        my_mark_pop_up = self.ids['my_mark_pop_up']
        my_mark_pop_up.lat = -23.5356222
        my_mark_pop_up.lon = -46.7913312
        #marker = MapMarker(lon=float(longitude_map.text), lat=float(latitude_map.text))
        print my_mark_pop_up
        id.center_on(float(latitude_map.text),float(longitude_map.text))
        #my_mark_pop_up.center_on(float(latitude_map.text),float(longitude_map.text))
        #id.add_widget(marker)

    pass


class RastreatorApp(App):

    def build(self):
        return MapView_new()
        # self.lati = -23.5356201
        # self.long = -46.7913307
        # self.f = FloatLayout()
        # self.marker = MapMarker(lat=self.lati + 0.0005, lon = self.long + 0.03)
        # self.mapview = MapView(zoom=11, lat=self.lati, lon=self.long,
        #                        pos_hint={'x': 0, 'y': 0}, size_hint=(1, 0.7))
        # b = Button(text='New Button to press',
        #             pos_hint={'x': 0, 'center_y': .8}, size_hint=(0.3, None))
        # b.bind(on_press=self.change_x)
        # c = Button(text='second Button to press',
        #            pos_hint={'x': 0.7, 'center_y': .8}, size_hint=(0.3, None))
        # c.bind(on_press=self.change_y)
        #
        #
        # label = Label(text='Rastreator',
        #         pos_hint = {'x': 0.4, 'center_y': 0.95}, size_hint = (None, None))
        #
        # self.mapview.add_widget(self.marker)
        # self.f.add_widget(label)
        # self.f.add_widget(b)
        # self.f.add_widget(c)
        # self.f.add_widget(self.mapview)
        #
        # print("** inside build()")
        # return self.f


if __name__ == '__main__':
    rastreator = RastreatorApp().run()