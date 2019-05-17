from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

kv = """
<MainScreen>:
    orientation: 'vertical'
    spacing: 20
    BoxLayout:
        spacing: 20
        canvas:
            Color:
                rgba: 0, 0, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        size_hint: 1, .5
        Button:
            size_hint: .25, .5
            pos_hint: {'x':.0, 'y':.0}
            text: '1'
        Button:
            size_hint: .25, .5
            pos_hint: {'center_x':.5, 'y':.0}
            text: '2'
        Button:
            size_hint: .25, .5
            pos_hint: {'right':1, 'y':.0}
            text: '3'

    FloatLayout:
        padding: [10, 10, 10, 10]
        size_hint: 1, .5
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Button:
            size_hint: .25, .5
            pos_hint: {'x':.0, 'y':.0}
            text: '1'
        Button:
            size_hint: .25, .5
            pos_hint: {'center_x':.5, 'y':.0}
            text: '2'
        Button:
            size_hint: .25, .5
            pos_hint: {'right':1, 'y':.0}
            text: '3'
"""
Builder.load_string(kv)

class MainScreen(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()