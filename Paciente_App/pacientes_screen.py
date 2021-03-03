from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#Para el Banner
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.graphics import Color,RoundedRectangle
from functools import partial
from io import open
import time

from conexion_BD import MedicionesPacientes
from conexion_BD import Conexion_BD

kv="""
<PacientesScreen>:
    name:'pacientes_screen'
    BoxLayout:
        orientation:'vertical'
        FloatLayout:
            size_hint:(1,.3)
            Image:
                source:'recursos/imagenes/termometro.png'
                size_hint:(.25,.7)
                pos_hint:{'center_x':.2,'center_y':.5}
            Image:
                source:'recursos/imagenes/oxigeno.png'
                size_hint:(.25,.4)
                pos_hint:{'center_x':.5,'center_y':.5}
            Image:
                source:'recursos/imagenes/pulso.png'
                size_hint:(.25,.7)
                pos_hint:{'center_x':.8,'center_y':.5}

        FloatLayout:
            size_hint:(1,.2)
            MDRectangleFlatButton:
                text: "Medir temperatura"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                line_color: 0, 0, 1, 1
                pos_hint:{'center_x':.2,'center_y':.5}
            MDRectangleFlatButton:
                text: "Medir porcentaje de saturacion de oxigeno"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                line_color: 0, 0, 1, 1
                pos_hint:{'center_x':.5,'center_y':.5}
            MDRectangleFlatButton:
                text: "Medir pulso cardiaco"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                line_color: 0, 0, 1, 1
                pos_hint:{'center_x':.8,'center_y':.5}

        GridLayout:
            size_hint:(1,.2)
            cols:3
            MDLabel:
                text:'temperatura'
                halign:'center'
            MDLabel:
                text:'porcentaje de saturacion de oxigeno'
                halign:'center'
            MDLabel:
                text:'pulso'
                halign:'center'

        FloatLayout:
            size_hint:(1,.2)
            MDRectangleFlatButton:
                text: "Enviar datos"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                line_color: 0, 0, 1, 1
                pos_hint: {"center_x": .5,"center_y": .75 }
                halign:'center'
                valign:'center'
                on_release:root.enviar_mediciones()
        
"""


class PacientesScreen(MDScreen):
    Builder.load_string(kv)
    
    def __init__(self,**kw):
        super().__init__(**kw)
        
        self.insertar=Conexion_BD()
    
    def enviar_mediciones(self):
        f=open('info_paciente.txt','r')
        lineas_texto=f.readlines()
        f.close()
        dni=int(lineas_texto[2])
        fecha=time.strftime('%d/%m/%Y')
        fecha_int=int(time.strftime('%Y%m%d'))
        hora=time.strftime("%I:%M:%S %p")
        hora_int=int(time.strftime("%H%M%S")) 
        pulso=150#cambiar depende de sensor
        temperatura=36.5#cambiar depende de sensor
        oxigeno=80#cambiar depende de sensor
        self.mediciones=MedicionesPacientes(dni,fecha,fecha_int,hora,hora_int,pulso,temperatura,oxigeno)

        self.insertar.insertar_dato(self.mediciones.toCollection())
        
    # def on_pre_enter(self):
    #     funciones para antes q cargue la pantalla


