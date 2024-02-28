from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (310, 580)

KV = '''
ScreenManager:
    MainScreen:
    WelcomeScreen:
    LoginScreen:
    ResetScreen:
    SignupScreen:

<MainScreen>
    name: "main"
    MDScreen:
        md_bg_color: 1, 1, 1, 
        
        MDLabel:
            text: "Choose your Role!"
            halign: "center"
            valign: "center"
            bold: True
            pos_hint: {"center_x": .5, "center_y": .93}
            color: rgba(34, 34, 34, 255)
            
        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: None, None
            size: "200dp", "200dp"
            pos_hint: {"center_x": .5, "center_y": .7}
    
            Image:
                source: "assets/boy.png"
                size_hint: .5, .8
                pos_hint: {"center_x": .5, "center_y": .85}
                
            MDButton:
                pos_hint: {"center_x": .5}
                on_release:
                    root.manager.transition.direction = "left"
                    root.manager.current = "welcome"
    
                MDButtonText:
                    text: "Student" 
    
        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: None, None
            size: "200dp", "200dp"
            pos_hint: {"center_x": .5, "center_y": .3}
    
            Image:
                source: "assets/teacher.png"
                size_hint: .5, .8
                pos_hint: {"center_x": .5, "center_y": .85}
                
            MDButton:
                pos_hint: {"center_x": .5}
                on_release:
                    root.manager.transition.direction = "left"
                    root.manager.current = "welcome"
    
                MDButtonText:
                    text: "Lecturer" 
                    
<WelcomeScreen>:
    name: "welcome"
    
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
            
        MDButton:
            style: "filled"
            theme_width: "Custom"
            height: "40dp"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .18}
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "login"
            
            MDButtonText:
                id: text
                text: "LOGIN"
                pos_hint: {"center_x": .5, "center_y": .5}
                
        MDButton:
            style: "outlined"
            theme_width: "Custom"
            height: "40dp"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .09}
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "signup"
            
            MDButtonText:
                id: text
                text: "SIGNUP"
                pos_hint: {"center_x": .5, "center_y": .5} 
                
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
                root.manager.current = "welcome"  
                
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
                
        MDButton:
            theme_width: "Custom"
            height: "40dp"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .34}
            
            MDButtonText:
                id: text
                text: "LOGIN"
                pos_hint: {"center_x": .5, "center_y": .5} 
            
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
            
        MDButton:
            theme_width: "Custom"
            height: "40dp"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .10}
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "reset"  
            
            MDButtonText:
                id: text
                text: "Reset"
                pos_hint: {"center_x": .5, "center_y": .5}
                
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
            
<ResetScreen>:                  
    name: "reset"
    
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
                root.manager.current = "login"  
                
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
            pos_hint: {"center_x": .5, "center_y": .65}
            
            TextInput:
                hint_text: "New Password"
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
                pos_hint: {"center_x": .45, "center_y": .0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)
            
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {"center_x": .5, "center_y": .5}
            
            TextInput:
                hint_text: "Confirm Password"
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
                
        MDButton:
            theme_width: "Custom"
            height: "40dp"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .34}
            
            MDButtonText:
                id: text
                text: "Reset"
                pos_hint: {"center_x": .5, "center_y": .5}

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
                root.manager.current = "welcome"
                
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
                
        MDButton:
            theme_width: "Custom"
            height: "40dp"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": .3} 
            
            MDButtonText:
                id: text
                text: "SIGNUP"
                pos_hint: {"center_x": .5, "center_y": .5}
                
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
            
        MDButton:
            theme_width: "Custom"
            height: "40dp"
            size_hint: .66, .065
            pos_hint: {"center_x": .5, "center_y": 0.07}
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "login"
            
            MDButtonText:
                id: text
                text: "SIGN IN"
                pos_hint: {"center_x": .5, "center_y": .5}
'''

class MainScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class ResetScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class ClassCheckInApp(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="main"))
        screen_manager.add_widget(WelcomeScreen(name="welcome"))
        screen_manager.add_widget(LoginScreen(name="login"))
        screen_manager.add_widget(ResetScreen(name="reset"))
        screen_manager.add_widget(SignupScreen(name="signup"))

        return Builder.load_string(KV)


ClassCheckInApp().run()

