from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
Window.size = (310, 580)

KV = """
MDScreen:
    md_bg_color: 1, 1, 1, 1
    
    MDButton:
        theme_width: "Custom"
        height: "70dp"
        size_hint: .66, .065
        pos_hint: {"center_x": .5, "center_y": .50} 
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = " "
            
        MDButtonText:
            id: text
            text: "Click to Register!"
            bold: True
            pos_hint: {"center_x": .5, "center_y": .5}
            
"""

class schedule(MDApp):

    def build(self):

        return Builder.load_string(KV)

if __name__ == "__main__":
    schedule().run()