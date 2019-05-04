from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from decimal import Decimal


class Spinner(BoxLayout):
    def __init__(self, **kwargs):
        super(Spinner, self).__init__(**kwargs)
        self.orientation="horizontal"
        self.label = Label(text=str(0.0))
        self.add_widget(self.label)
        self.buttons = BoxLayout(orientation="vertical", size_hint=(.3, 1))
        self.buttons.add_widget(Button(text=">", on_press=self.up_pressed))
        self.buttons.add_widget(Button(text="<", on_press=self.down_pressed))
        self.add_widget(self.buttons)

    def up_pressed(self, instance):
        self.label.text = str(Decimal(self.label.text) + Decimal('0.1'))

    def down_pressed(self, instance):
        self.label.text = str(Decimal(self.label.text) - Decimal('0.1'))

    @property
    def value(self):
        return float(self.label.text)


class MyClassApp(App):
    def __init__(self):
        super(MyClassApp, self).__init__()

    def build(self):
        self.title = 'Saipis'
        grid_layout = GridLayout(cols=3, padding=10, spacing=10)
        grid_layout.add_widget(Spinner())
        grid_layout.add_widget(Spinner())
        grid_layout.add_widget(Spinner())
        grid_layout.add_widget(Spinner())
        grid_layout.add_widget(Spinner())
        grid_layout.add_widget(Spinner())
        return grid_layout


if __name__ == "__main__":
    MyClassApp().run()
