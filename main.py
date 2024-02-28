from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (310, 580)

KV = """
ScreenManager:
    MainScreen:
    LoginScreen:
    SignupScreen:
    ResetScreen:

<MainScreen>:
    name: "main"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        Image:
            source: "assets/graduated.png"
            size_hint: .8, .8
            pos_hint: {"center_x": .5, "center_y": .65}
        MDLabel:
            text: "H e l l o !"
            font_size: "23sp"
            pos_hint: {"center_y": .38}
            halign: "center"
            color: rgba(34, 34, 34, 255)
        MDLabel:
            text: "Best place to write life stories"
            font_size: "13sp"
            pos_hint: {"center_x": .5, "center_y": .3}
            halign: "center"
            color: rgba(127, 127, 127, 255)   
        Button:
            text: "LOGIN"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .18}
            background_color: 0, 0, 0, 0   
            on_release:
                root.manager.transition.direction = "left" 
                root.manager.current = "login" 
            canvas.before:
                Color:
                    rgb: rgba(255, 165, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]       
        Button:
            text: "SIGNUP"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .09}
            background_color: 0, 0, 0, 0   
            color: rgba(255, 165, 0, 255)
            on_release:
                root.manager.transition.direction = "left" 
                root.manager.current = "signup" 
            canvas.before:
                Color:
                    rgb: rgba(255, 165, 0, 255)
                Line:
                    width: 1.2
                    rounded_rectangle: self.x, self.y, self.width, self.height, 5, 5, 5, 5, 100       

<LoginScreen>:                  
    name: "login"
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
                root.manager.current = "main"  
        MDLabel:
            text: "W e l c o m e !"
            font_size: "26sp"
            pos_hint: {"center_x": .6, "center_y": .85}
            color: rgba(0, 0, 59, 255)    
        MDLabel:
            text: "Sign in to continue"
            font_size: "18sp"
            pos_hint: {"center_x": .6, "center_y": .79}
            color: rgba(255, 200, 130, 255)      
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {"center_x": .5, "center_y": .63}
            TextInput:
                hint_text: "Email"
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
            pos_hint: {"center_x": .5, "center_y": .5}
            TextInput:
                hint_text: "Password"
                size_hint_y: .75
                pos_hint: {"center_x": .43, "center_y": .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: "14sp"
                cursor_width: "2sp"
                multiline: False
                password: True
            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)  
        Button:
            text: "LOGIN"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .34}
            background_color: 0, 0, 0, 0  
            canvas.before:
                Color:
                    rgb: rgba(255, 165, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]    
        MDButtonText
            text: "Forgot Password?"
            pos_hint: {"center_x": .5, "center_y": .28}
            color: rgba(68, 78, 138, 255)
            font_size: "12sp"             
        MDLabel:
            text: "or"
            color: rgba(255, 165, 0, 255)
            pos_hint: {"center_y": .22}
            font_size: "13sp"
            halign: "center"
        MDFloatLayout: 
            md_bg_color: rgba(178, 178, 178, 255)
            size_hint: .3, .002
            pos_hint: {"center_x": .3, "center_y": .218}   
        MDFloatLayout: 
            md_bg_color: rgba(178, 178, 178, 255)
            size_hint: .3, .002
            pos_hint: {"center_x": .7, "center_y": .218}  
        MDLabel:
            text: "Forgot your password?"
            font_size: "13sp"
            halign: "center"
            pos_hint: {"center_y": .16}
            color: rgba(135, 133, 193, 255) 
            
        MDButtonText:
            text: "Reset"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  
            md_bg_color: 1, 0.647, 0, 1   
            radius: [0, 0, 0, 0]
            pos_hint: {"center_x": .5, "center_y": 0.10}
            size_hint: .25, .065
            
        MDLabel:
            text: "Don't have an account?"
            font_size: "11sp"
            pos_hint: {"center_x": .63, "center_y": .04}
            color: rgba(135, 133, 193, 255)
        MDButtonText: 
            pos_hint: {"center_x": .75, "center_y": .04}
            size_hint: None, None
            text: "Sign Up"
            font_size: "12sp"
            theme_text_color: "Custom"
            text_color: 1, 0.647, 0, 1

<SignupScreen>:  
    name: "signup"
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
                root.manager.current = "main"
        MDLabel:
            text: "H i !"
            font_size: "26sp"
            pos_hint: {"center_x": .6, "center_y": .85}
            color: rgba(0, 0, 59, 255)    
        MDLabel:
            text: "Create a new account"
            font_size: "18sp"
            pos_hint: {"center_x": .6, "center_y": .79}
            color: rgba(255, 200, 130, 255) 
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {"center_x": .5, "center_y": .68}
            TextInput:
                hint_text: "Username"
                size_hint_y: .75
                pos_hint: {"center_x": .43, "center_y": .68}
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
            pos_hint: {"center_x": .5, "center_y": .56}
            TextInput:
                hint_text: "Email"
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
            pos_hint: {"center_x": .5, "center_y": .44}
            TextInput:
                hint_text: "Password"
                size_hint_y: .75
                pos_hint: {"center_x": .43, "center_y": .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: "14sp"
                cursor_width: "2sp"
                multiline: False
                password: True
            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)
        Button:
            text: "SIGNUP"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .3}
            background_color: 0, 0, 0, 0  
            canvas.before:
                Color:
                    rgb: rgba(255, 165, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]  
        MDLabel:
            text: "or"
            color: rgba(255, 165, 0, 255)
            pos_hint: {"center_y": .22}
            font_size: "13sp"
            halign: "center"
        MDFloatLayout: 
            md_bg_color: rgba(178, 178, 178, 255)
            size_hint: .3, .002
            pos_hint: {"center_x": .3, "center_y": .218}   
        MDFloatLayout: 
            md_bg_color: rgba(178, 178, 178, 255)
            size_hint: .3, .002
            pos_hint: {"center_x": .7, "center_y": .218}  
        MDLabel:
            text: "Already have an account?"
            font_size: "11sp"
            pos_hint: {"center_x": .70, "center_y": .15}
            color: rgba(135, 133, 193, 255)
        MDButtonText:
            text: "Sign In"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  
            md_bg_color: 1, 0.647, 0, 1   
            radius: [0, 0, 0, 0]
            pos_hint: {"center_x": .5, "center_y": 0.07}
            size_hint: .25, .065
            
<ResetScreen>:                  
    name: "login"
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
                root.manager.current = "main"  
        MDLabel:
            text: "Reset your password!"
            font_size: "26sp"
            pos_hint: {"center_x": .6, "center_y": .85}
            color: rgba(0, 0, 59, 255)    
        MDLabel:
            text: "Please enter your new password"
            font_size: "18sp"
            pos_hint: {"center_x": .6, "center_y": .79}
            color: rgba(255, 200, 130, 255)      
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {"center_x": .5, "center_y": .5}
            TextInput:
                hint_text: "Password"
                size_hint_y: .75
                pos_hint: {"center_x": .43, "center_y": .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: "14sp"
                cursor_width: "2sp"
                multiline: False
                password: True
            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)  
        Button:
            text: "RESET"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .34}
            background_color: 0, 0, 0, 0  
            canvas.before:
                Color:
                    rgb: rgba(255, 165, 0, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]    
        MDButtonText
            text: "Forgot Password?"
            pos_hint: {"center_x": .5, "center_y": .28}
            color: rgba(68, 78, 138, 255)
            font_size: "12sp"             
        
"""


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass

class ResetScreen(Screen):
    pass


class ClassroomCheckIn(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="main"))
        screen_manager.add_widget(LoginScreen(name="login"))
        screen_manager.add_widget(SignupScreen(name="signup"))
        screen_manager.add_widget(ResetScreen(name="reset"))

        return Builder.load_string(KV)


if __name__ == "__main__":
    ClassroomCheckIn().run()