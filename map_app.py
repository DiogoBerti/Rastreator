from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.mapview import MapView, MapMarker
import requests


Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Label:
            text: "Menu"
            size_hint_x: 0.5
            size_hint_y: 0.1
            pos_hint: {'x': 0.25, 'y': 0.85}
        Button:
            text: 'Goto Map'
            on_press: root.manager.current = 'map'
            size_hint_x: 0.5
            size_hint_y: 0.1
            pos_hint: {'x': 0.25, 'y': 0.65}
        Button:
            text: 'Quit'
            size_hint_x: 0.5
            size_hint_y: 0.1
            pos_hint: {'x': 0.25, 'y': 0.45}

<MarkerFind>:
    FloatLayout:
        Label:
            id: label1
            text: "Find a new Address"
            size_hint_x: 0.5
            size_hint_y: 0.1
            pos_hint: {'x': 0.25, 'y': 0.85}
        
        Label:
            id: label2
            text: "Adress: "
            size_hint_x: 0.2
            size_hint_y: 0.05
            pos_hint: {'x': 0.2, 'y': 0.65}
        
        
        TextInput:
            id: addressnew
            size_hint_x: 0.4
            size_hint_y: 0.05
            pos_hint: {'x': 0.4, 'y': 0.65}
        
        Button:
            id: menu_button2
            text: "Menu"
            on_press: root.manager.current = 'menu'
            size_hint_x: 0.1
            size_hint_y: 0.05
            pos_hint: {'x': 0.9, 'y': 0.95}
        
        Label:
            id: address_found
            text: ""
            size_hint_x: 0.2
            size_hint_y: 0.05
            pos_hint: {'x': 0.2, 'y': 0.45}
            
        Button:
            id: findaddressbutton
            text: "Find"
            on_press: root.address_find()
            size_hint_x: 0.1
            size_hint_y: 0.05
            pos_hint: {'x': 0.8, 'y': 0.65}
        
        Button:
            id: markerbutton
            text: "Go"
            on_press: root.add_marker()
            size_hint_x: 0.1
            size_hint_y: 0.05
            disabled: True
            pos_hint: {'x': 0.8, 'y': 0.10}
        

<MapScreen>:
    FloatLayout:
        canvas:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                size: self.size
                pos: self.pos

        Button:
            id: menu_button
            text: "Menu"
            on_press: root.manager.current = 'menu'
            size_hint_x: 0.1
            size_hint_y: 0.05
            pos_hint: {'x': 0.9, 'y': 0.95}
            
        Button:
            id: address_button
            text: "Find"
            on_press: root.manager.current = 'find'
            size_hint_x: 0.1
            size_hint_y: 0.05
            pos_hint: {'x': 0, 'y': 0.95}
        
        Button:
            id: my_button
            text: "Find Address"
            size_hint_x: 0.2
            size_hint_y: 0.05
            pos_hint: {'x': 0.6, 'y': 0.90}
            on_press: root.find_address()
        
        Label:
            text: "Address: "
            size_hint_x: 0.1
            size_hint_y: 0.05
            pos_hint: {'x': 0.0, 'y': 0.90}
            
        TextInput:
            id: address
            size_hint_x: 0.4
            size_hint_y: 0.05
            pos_hint: {'x': 0.1, 'y': 0.90}
        
        MapView:
            id: my_map_view
            lat: 50.6394
            lon: 3.057
            zoom: 14
            size_hint_y: 0.8
            size_hint_x: 1
            pos_hint: {'x': 0, 'y': 0}
            MapMarkerPopup:
                id: my_mark_pop_up
                lat: 50.6394
                lon: 3.057
                popup_size: dp(230), dp(130)
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class MarkerFind(Screen):

    def add_marker(self):
        mapscreen = self.manager.get_screen('map')

        address = self.ids['addressnew'].text
        final_address = ""
        new_address = address.split()
        for i in new_address:
            final_address += i + "+"

        google_search = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s' % final_address
        response = requests.get(google_search)
        resp_json_payload = response.json()
        location = resp_json_payload['results'][0]['geometry']['location']

        lat = location['lat']
        lon = location['lng']

        new_marker = MapMarker()
        new_marker.lat = lat
        new_marker.lon = lon
        mapscreen.ids['my_map_view'].add_widget(new_marker)
        mapscreen.ids['my_map_view'].center_on(lat,lon)
        mapscreen.ids['my_map_view'].zoom = 16
        self.manager.current = 'map'


    def address_find(self):
        address = self.ids['addressnew'].text
        final_address = ""
        new_address = address.split()
        for i in new_address:
            final_address += i + "+"

        google_search = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s' % final_address
        response = requests.get(google_search)
        resp_json_payload = response.json()
        location = resp_json_payload['results'][0]['formatted_address']
        if location != "":
            self.ids['markerbutton'].disabled = False
        else:
            self.ids['markerbutton'].disabled = True
        self.ids['address_found'].text = location



    pass

class MapScreen(Screen):

    def find_address(self):

        if self.ids['address'].text != "":
            address = self.ids['address'].text
            map_id = self.ids['my_map_view']
            marker_id = self.ids['my_mark_pop_up']
            final_address = ""
            new_address = address.split()
            for i in new_address:
                final_address += i + "+"

            google_search = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s' % final_address

            response = requests.get(google_search)
            resp_json_payload = response.json()
            location = resp_json_payload['results'][0]['geometry']['location']

            lat = location['lat']
            lon = location['lng']
            map_id.center_on(float(lat), float(lon))
            marker_id.lat = lat
            marker_id.lon = lon
        else:
            print "No address"

    def add_marker_location(self):
        pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MapScreen(name='map'))
sm.add_widget(MarkerFind(name='find'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()