from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from conexion_BD import Conexion_BD
from kivymd.app import MDApp
# importado para ir al enlace
import webbrowser
#importando la pantalla de navegacion
from navigation_screen import NavigationScreen


kv="""
<LoginScreen>:
    name:'login_screen'
    Screen:
        FitImage:
            source:'recursos/imagenes/fondo_1.jpg'
        
        FloatLayout:
            id:box
            size_hint:None,None
            width:500
            height:500
            pos_hint: {"center_x": .5,"center_y": .5 }
            padding:"30dp","15dp","30dp","30dp"
            spacing:'10dp'

            canvas:
                Color: 
                    rgba: 1,1,1, .5
                RoundedRectangle:
                    pos:self.pos
                    size:self.size
                    radius: 10,10,10,10

            MDLabel:
                pos_hint: {"center_x": .5,"center_y": .9 }
                text:'INICIO DE SESIÓN'
                bold:True
                theme_text_color:'Custom'
                text_color:0,0,0,1
                halign:'center'
                font_style:"H5"
            MDLabel:
                pos_hint: {"center_x": .5,"center_y": .8 }
                text:'Bienvenido'
                size_hint_x:.8
                bold:True
                font_style:"Subtitle1"
            MDLabel:
                pos_hint: {"center_x": .5,"center_y": .7 }
                size_hint_x:.8
                text:'Necesitamos que nos brindes algunos datos para poder hacer uso de este servicio'
                font_style:'Body1'

            MDTextFieldRound:
                pos_hint: {"center_x": .5,"center_y": .55 }
                size_hint_x:.8
                id:correo
                icon_left:'mail'
                normal_color: 1,1,1,.5
                icon_left_color: 0,0,0
            
            MDTextFieldRound:
                id:password
                icon_left:'lock'
                size_hint_x:.8
                pos_hint: {"center_x": .5,"center_y": .4 }
                normal_color: 1,1,1,.5
                icon_left_color: 0,0,0
                
            MDRaisedButton:
                text:'Iniciar Sesión'
                font_size: "15sp"
                pos_hint: {"center_x": .5,"center_y": .25 }
                on_release:root.iniciar_sesion()
            
            MDLabel:
                text:'Si no posee una cuenta,regístrese en el siguiente'
                pos_hint: {"center_x": .5,"center_y": .125 }
                halign:'center'
                size_hint_x:.8
                font_style:'Body1'
                pos_hint_x:.5

            MDFlatButton:
                pos_hint: {"center_x": .5,"center_y": .075 }
                text:'enlace'
                size_hint_y:.2
                text_color: 0, 0, .4, 1
                elevation: 0
                #md_bg_color:1,1,1,0
                font_size: "16sp"
                on_release: root.ir_enlace()
"""

class LoginScreen(MDScreen):
    Builder.load_string(kv)

    def __init__(self,**kw):
        super().__init__(**kw)
        self.app=MDApp.get_running_app()#
        self.mi_conexion=Conexion_BD()

        pantalla_navegacion=NavigationScreen()
        self.app.root.add_widget(pantalla_navegacion)

    
    def iniciar_sesion(self):
        if self.mi_conexion.inicio_sesion(self.ids.correo.text,self.ids.password.text) ==False:
            print('a ocurrido un error')
            self.ids.correo.text=''
            self.ids.password.text=''
        else:
            self.app.root.current='navigation_screen'
        # print(self.ids.correo.text)
        # print(self.ids.password.text)
        

    def ir_enlace(self):
        webbrowser.open('https://stark-spire-16180.herokuapp.com/reg_medico#')
        