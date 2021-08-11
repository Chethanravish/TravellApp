from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.card import MDCard


class Places(MDCard):
    name = StringProperty()
    avatar = StringProperty()
    post = StringProperty()

    save = NumericProperty()

