from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
import json
from Travelling.components.places import Places


class Explore(MDScreen):
    def on_enter(self):
        self.list_places()

    def list_places(self):
        with open("components/places_data.json") as f:
            data = json.load(f)
            for place in data:
                self.ids.timeline.add_widget(Places(
                    name=place,
                    avatar=data[place]['avatar'],
                    post = data[place]['post'],
                    save = data[place]['save']
                ))