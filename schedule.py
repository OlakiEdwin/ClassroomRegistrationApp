from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
Window.size = (310, 580)

KV = """
MDScreen:
    md_bg_color: 1, 1, 1, 1
    
    MDLabel:
        text: "Weekly Schedule"
        bold: True
        halign: "center"
        valign: "center"
        pos_hint: {"center_x": .5, "center_y": .95}
        
    MDLabel:
        text: "Monday"
        bold: True
        pos_hint: {"center_x": .6, "center_y": .90}
        
    MDIcon:
        icon: "star-box"
        pos_hint: {"center_x": 0.13, "center_y": .86}
        
        MDLabel:
            text: "8:00am - 10:00am"
            pos_hint: {"center_x": .5, "center_y": .80}
"""

class schedule(MDApp):

    def build(self):

        return Builder.load_string(KV)

if __name__ == "__main__":
    schedule().run()