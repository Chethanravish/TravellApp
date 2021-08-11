from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from Travelling.explore import Explore



Window.size = (350,600)
class TravelApp(MDApp):
    def build(self):
        self.load_all_kv_files()
        return Explore()

    def load_all_kv_files(self):
        Builder.load_file("explore.kv")
        Builder.load_file("components/places.kv")

if __name__== '__main__':
    TravelApp().run()