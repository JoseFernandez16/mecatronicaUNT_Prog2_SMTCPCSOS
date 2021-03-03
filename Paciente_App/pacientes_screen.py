from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
# Para el Banner
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.graphics import Color, RoundedRectangle
from functools import partial
from kivy.properties import NumericProperty
from io import open
import time
import serial
from conexion_BD import MedicionesPacientes
from conexion_BD import Conexion_BD
ser = serial.Serial("COM6", 115200)

kv = """
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
                on_release:root.Temperatura()
            MDRectangleFlatButton:
                text: "Medir porcentaje de saturacion de oxigeno"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                line_color: 0, 0, 1, 1
                pos_hint:{'center_x':.5,'center_y':.5}
                on_release:root.SPO2()
            MDRectangleFlatButton:
                text: "Medir pulso cardiaco"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                line_color: 0, 0, 1, 1
                pos_hint:{'center_x':.8,'center_y':.5}
                on_release:root.heart()

        GridLayout:
            size_hint:(1,.2)
            cols:3
            MDLabel:
                id:TEMPERATURA
                text:""
                halign:'center'
            MDLabel:
                id:SPO2
                text:''
                halign:'center'
            MDLabel:
                id:PULSO
                text:''
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
    valTemp = NumericProperty()
    valSO2 = NumericProperty()
    valPulso = NumericProperty()

    def __init__(self, **kw):
        super().__init__(**kw)

        self.insertar = Conexion_BD()

    def enviar_mediciones(self):
        f = open('info_paciente.txt', 'r')
        lineas_texto = f.readlines()
        f.close()
        dni = int(lineas_texto[2])
        fecha = time.strftime('%d/%m/%Y')
        fecha_int = int(time.strftime('%Y%m%d'))
        hora = time.strftime("%I:%M:%S %p")
        hora_int = int(time.strftime("%H%M%S"))
        pulso = self.valPulso  # cambiar depende de sensor
        temperatura = self.valTemp
        oxigeno = self.valSO2  # cambiar depende de sensor
        self.mediciones = MedicionesPacientes(
            dni, fecha, fecha_int, hora, hora_int, pulso, temperatura, oxigeno)

        self.insertar.insertar_dato(self.mediciones.toCollection())

    def Temperatura(self):

        ser.write(chr(49).encode('ascii'))
        cc2 = ""
        sal = 0
        tempLista = []
        while True:
            cc = str(ser.readline())
            # print(str(cc[2:][:-5]))

            while cc[2:][:-5] == "49":
                cc2 = str(ser.readline())
                if cc2[2:][:-5] != "a":
                    tempLista.append(float(cc2[2:][:-5]))
                    ptemp = sum(tempLista)/len(tempLista)
                    # print(tempLista)
                    print(ptemp)

                    # print(str(cc2[2:][:-5]))

                if cc2[2:][:-5] == "a":
                    sal = 1
                    break
            if sal == 1:
                break
        self.valTemp = round(ptemp, 2)
        self.ids['TEMPERATURA'].text = str(round(ptemp, 2))

    def SPO2(self):

        ser.write(chr(50).encode('ascii'))
        cc2 = ""
        sal = 0
        tempLista = []
        while True:
            cc = str(ser.readline())
            # print(str(cc[2:][:-5]))

            while cc[2:][:-5] == "50":
                cc2 = str(ser.readline())
                if cc2[2:][:-5] != "a" and cc2[2:][:-5] != "-999":
                    tempLista.append(float(cc2[2:][:-5]))
                    ptemp = sum(tempLista)/len(tempLista)
                    # print(tempLista)
                    print(ptemp)
                    # print(str(cc2[2:][:-5]))
                elif len(tempLista) == 0:
                    ptemp = 0

                if cc2[2:][:-5] == "a":
                    sal = 1
                    break
            if sal == 1:
                break
        self.valSO2 = round(ptemp, 2)
        self.ids['SPO2'].text = str(round(ptemp, 2))

    def heart(self):

        ser.write(chr(51).encode('ascii'))
        cc2 = ""
        sal = 0
        tempLista = []
        while True:
            cc = str(ser.readline())
            # print(str(cc[2:][:-5]))

            while cc[2:][:-5] == "51":
                cc2 = str(ser.readline())
                if cc2[2:][:-5] != "a" and cc2[2:][:-5] != "-999":
                    tempLista.append(float(cc2[2:][:-5]))
                    ptemp = sum(tempLista)/len(tempLista)
                    # print(tempLista)
                    print(ptemp)
                    # print(str(cc2[2:][:-5]))
                elif len(tempLista) == 0:
                    ptemp = 0
                if cc2[2:][:-5] == "a":
                    sal = 1
                    break
            if sal == 1:
                break
        self.valPulso = round(ptemp, 2)
        self.ids['PULSO'].text = str(round(ptemp, 2))
    # def on_pre_enter(self):
    #     funciones para antes q cargue la pantalla
