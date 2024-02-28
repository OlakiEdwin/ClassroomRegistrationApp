from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp

Window.size = (310, 580)

KV = '''
MDScreen:
    md_bg_color: 1, 1, 1, 

    ScrollView:  
        MDBoxLayout:
            orientation: "vertical"
            spacing: "10dp"
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                text: "Edit Profile"
                halign: "center"
                valign: "center"
                bold: True
                size_hint_y: None
                height: "40dp"
                color: rgba(34, 34, 34, 255)

            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: None, None
                size: "290dp", "100dp"
                pos_hint: {"center_x": .5, "center_y": .85}

                Image:
                    source: "assets/boy.png"
                    size_hint: .5, .8
                    pos_hint: {"center_x": .5, "center_y": .85}

            MDButton:
                pos_hint: {"center_x": .5, "center_y": .68}

                MDButtonText:
                    text: "Edit profile photo"

            MDBoxLayout:
                orientation: "vertical"
                spacing: "7dp"
                adaptive_height: True
                size_hint_x: .9
                pos_hint: {"center_x": .5, "center_y": .3}

                MDLabel:
                    text: "Name"
                    bold: True
                    size_hint_y: None
                    height: "10dp"

                MDTextField:
                    mode: "outlined"

                MDLabel:
                    text: "Course"
                    bold: True
                    size_hint_y: None
                    height: "10dp"

                MDTextField:
                    mode: "outlined"

                MDLabel:
                    text: "Year of Study"
                    bold: True
                    size_hint_y: None
                    height: "10dp"

                MDTextField:
                    mode: "outlined"

                MDLabel:
                    text: "Registration Number"
                    bold: True
                    size_hint_y: None
                    height: "10dp"

                MDTextField:
                    mode: "outlined"

                MDLabel:
                    text: "Student Number"
                    bold: True
                    size_hint_y: None
                    height: "10dp"

                MDTextField:
                    mode: "outlined"

            MDButton:
                style: "filled"
                theme_width: "Custom"
                height: "40dp"
                size_hint: .66, .065
                pos_hint: {"center_x": .5, "center_y": .18}
                on_release:
                    root.manager.transition.direction = "left"
                    root.manager.current = ""

                MDButtonText:
                    id: text
                    text: "SUBMIT"
                    pos_hint: {"center_x": .5, "center_y": .5}
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

Example().run()

