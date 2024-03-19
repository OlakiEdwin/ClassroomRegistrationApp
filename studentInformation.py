import sqlite3
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.button import MDButton

Window.size = (310, 580)

kv_string = '''
MDScreen:
    md_bg_color: 1, 1, 1, 1

    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26, 24, 58, 255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "welcome"  
                
        MDLabel:
            text: "W e l c o m e !"
            bold: True
            font_size: "26sp"
            pos_hint: {"center_x": .8, "center_y": .95}
            color: rgba(0, 0, 59, 255)    
            
        MDLabel:
            text: "Enter your details below to continue!"
            bold: True
            font_size: "18sp"
            pos_hint: {"center_x": .6, "center_y": .88}
            color: rgba(255, 200, 130, 255)      
            
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {"center_x": .5, "center_y": .78}
            
            TextInput:
                hint_text: "Full Names"
                size_hint_y: .75
                pos_hint: {"center_x": .43, "center_y": .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: "14sp"
                cursor_width: "2sp"
                multiline: False
                
            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)
                
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {"center_x": .5, "center_y": .65}
            
            TextInput:
                hint_text: "Course and Year of Study"
                size_hint_y: .75
                pos_hint: {"center_x": .43, "center_y": .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: "14sp"
                cursor_width: "2sp"
                multiline: False
                
            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)
                
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {"center_x": .5, "center_y": .52}
            
            TextInput:
                hint_text: "Registration Number"
                size_hint_y: .75
                pos_hint: {"center_x": .43, "center_y": .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: "14sp"
                cursor_width: "2sp"
                multiline: False
                
            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)
                
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {"center_x": .5, "center_y": .38}
            
            TextInput:
                hint_text: "Student Email"
                size_hint_y: .75
                pos_hint: {"center_x": .43, "center_y": .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: "14sp"
                cursor_width: "2sp"
                multiline: False
                
            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)  
                
        MDButton:
            theme_width: "Custom"
            height: "40dp"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .20}
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = " "
            
            MDButtonText:
                id: text
                text: "SUBMIT"
                pos_hint: {"center_x": .5, "center_y": .5}
'''

class StudentInfoApp(MDApp):

    def build(self):
        self.conn = sqlite3.connect('student_info.db')
        self.cur = self.conn.cursor()
        self.create_table()
        screen = Builder.load_string(kv_string)
        return screen

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS students
                            (id INTEGER PRIMARY KEY,
                            fullNames TEXT,
                            courseAndYearOfStudy STRING,
                            registrationNumber STRING,
                            studentEmail STRING)''')
        self.conn.commit()

    def submit_info(self):
        fullNames = self.root.ids.txt_fullNames.text
        courseAndYearOfStudy = self.root.ids.txt_courseAndYearOfStudy.text
        registrationNumber = self.root.ids.txt_registrationNumber.text
        studentEmail = self.root.ids.txt_studentEmail.text


        if fullNames.strip() == "" or courseAndYearOfStudy.strip() == "" or registrationNumber.strip() == "" or studentEmail.strip() == "":
            self.show_alert("Error", "Please fill in all fields.")
        else:
            self.show_alert("Success", f"Student {fullNames} with courseAndYearOfStudy {courseAndYearOfStudy} with registrationNumber {registrationNumber} with studentEmail {studentEmail} added successfully.")

        def show_alert(self, title, message):
            alert = MDDialog(title=title, text=message, size_hint=(0.7, 0.3))
            alert.open()

        def on_stop(self):
            self.conn.close()

if __name__ == '__main__':
    StudentInfoApp().run()
