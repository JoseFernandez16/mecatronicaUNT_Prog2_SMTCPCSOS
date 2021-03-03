from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#from login_screen import LoginScreen
import webbrowser

kv="""
<InformacionScreen>:
    name:'information_screen'
    Screen:
        FitImage:
            source:'recursos/imagenes/fondo_2.jpg'
        BoxLayout:
            id:box
            orientation: 'vertical'
            size_hint: None,None
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
                text:"Funcionamiento de la aplicacion"
                font_style:"H6"
                size_hint:1,.1
            MDLabel:
                id:indicaciones
                font_style:"Body1"
            MDRaisedButton:
                pos_hint: {"center_x": .5,"center_y": .5 }
                text: "Regístrese aquí"
                text_color: 0,0,.4,1
                md_bg_color: 1, 1, 1, 1
                on_release:root.enviar_al_enlace()
"""

class InformacionScreen(MDScreen):
    Builder.load_string(kv)

    def on_pre_enter(self, *args):
        self.ids["indicaciones"].text="""La siguiente app se conecta a una placa arduino la cual por medio de sensores permite que el paciente sea capaz de obtener los valores de tres de sus variables fisiológicas: Saturación de Oxígeno, Temperatura y Frecuencia Cardiaca.\n
        De esta manera, el paciente envía los valores de las variables en diversos instantes del día durante el periodo de tiempo que sea determinado por el especialista, para asi tener un registro y monitoreo del estado médico del paciente.\n
        Así mismo, el paciente es capaz de verificar el historial de sus registros, ordenados por fecha y hora en la que fueron agregados a la base de datos."""

    def enviar_al_enlace(self):
        webbrowser.open('https://stark-spire-16180.herokuapp.com/reg_medico#')
        