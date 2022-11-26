"""
User Authentification Functionality
"""

from str_builder import *

complete_app_builder += """
<Login>:
   name: 'login'
   Screen:
      MDBoxLayout:
         pos_hint: {"center_x": 0.5, "center_y": 0.5}
         padding: 25
         spacing: 25
         orientation: 'vertical'
         
         Image:
            source: 'Icons\ShannonLogo.png'
            pos_hint: {"center_x": 0.5}

         MDLabel:
            id: welcome_label
            text: "Login"
            font_size: 22
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

         MDTextField:
            id: user
            hint_text: "Email"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}


         MDTextField:
            id: password
            hint_text: "Password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True

         MDLabel:
            id: warning_label
            text: " "
            font_size: 12
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]

         MDRoundFlatButton:
            text: "Log In"
            font_size: 20
            pos_hint: {"center_x": 0.5}
            on_press: app.logger()

         MDFlatButton:
            text: "Create account"
            font_size: 12
            pos_hint: {"center_x": 0.5}
            on_release: root.manager.current = "create"

         MDFlatButton:
            text: "Forgot Password"
            font_size: 10
            pos_hint: {"center_x": 0.5}
            on_press: root.manager.current = "forgot"

"""




