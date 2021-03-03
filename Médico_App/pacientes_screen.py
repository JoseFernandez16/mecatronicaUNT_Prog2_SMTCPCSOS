from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#Para el Banner
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDIconButton
from kivy.graphics import Color,RoundedRectangle
from functools import partial
#
from kivymd.app import MDApp
from historial_screen import HistorialScreen
#
from conexion_BD import Conexion_BD
from io import open

class Banner(FloatLayout):
    
    def __init__(self,apellidos,nombre, **kwargs):
        self.apellidos=str(apellidos)
        self.nombres=str(nombre)
        self.inicial='f'

        #agregar para la funcion


        super().__init__()
        with self.canvas.before:
            Color(rgba=(0,.5,1,.1))
            self.rect=RoundedRectangle(radius=[(15.0,15.0),(15.0,15.0),(15.0,15.0),(15.0,15.0)])
        
        self.bind(pos=self.update_rect,size=self.update_rect)

        #etiquetas del banner
        self.title_apellidos=MDLabel(text=self.apellidos,pos_hint={'center_x': .37, 'center_y':.5},size_hint=(.45,.3),halign='center')
        self.title_nombres=MDLabel(text=self.nombres,pos_hint={'center_x': .7, 'center_y':.5},size_hint=(.45,.3),halign='center')
        self.icono=MDIcon(icon='alpha-'+self.inicial+'-circle',pos_hint={'center_x': .09, 'center_y':.5},size_hint=(.1,.3),halign='center')
        self.visual=MDIconButton(icon='eye',pos_hint={'center_x': .95, 'center_y':.5},on_release=kwargs['on_release'])
        #agregar widget
        self.add_widget(self.icono)
        self.add_widget(self.title_apellidos)
        self.add_widget(self.title_nombres)
        self.add_widget(self.visual)
    
    def update_rect(self,*args):
        self.rect.pos=self.pos
        self.rect.size=self.size

kv="""
<PacientesScreen>:
    name:'pacientes_screen'
    BoxLayout:
        BoxLayout:
            ScrollView:
                id:Scroll
                GridLayout:
                    id:grid_banner
                    cols:1
                    padding:[20,20,20,20]
                    size_hint_y:None
                    height:self.minimum_height
                    row_default_height:50
                    padding:'10dp'
                    spacing:'10dp'
        # BoxLayout:
        #     ScrollView:
        #         id:Scroll
        #         GridLayout:
        #             id:ficha
        #             cols:1
        #             padding:[20,20,20,20]
        #             size_hint_y:None
        #             height:self.minimum_height
        #             row_default_height:50
        #             padding:'10dp'
        #             spacing:'10dp'

        #             MDLabel:
        #                 text:'ga'

"""

class PacientesScreen(MDScreen):
    Builder.load_string(kv)
    
    def __init__(self,**kw):
        super().__init__(**kw)
        self.app=MDApp.get_running_app()
        self.vez=0
        self.filas_pacientes=Conexion_BD()
    
    def on_pre_enter(self):
        f=open('info_medico.txt','r')
        linea_texto=f.readlines()
        f.close()
        centro=str(linea_texto[3])
        self.grid=self.ids['grid_banner']
        self.lista_pacientes=self.filas_pacientes.obtener_pacientes(centro)
        #print(self.lista_pacientes)
        #añadiendo al scroll
        

        if self.vez==0:
            self.vez=1
        else:
            for i in range(len(self.lista_pacientes)-1):
                self.grid.remove_widget(self.grid.children[0])
        
        for i in self.lista_pacientes:
            self.banner=Banner(i['apellidos'],i['nombres'],on_release=partial(self.ver_ficha,i))#,i['email'],i['celular'],i['edad'],i['direccion'],i['departamento'],i['ciudad'],i['dni']
            self.grid.add_widget(self.banner)
    def on_enter(self):
        pantalla_historial=HistorialScreen()
        self.app.root.add_widget(pantalla_historial)

    def ver_ficha(self,dato,base_widget):
        
        nombre=dato['nombres'];apellido=dato['apellidos'];num_dni=str(dato['dni'])
            #print(nombre+'\n'+apellido+'\n'+num_colegiatura+'\n'+trabajo)
        archivo_texto=open('mi_paciente.txt','w')
        datos_recibidos=nombre+'\n'+apellido+'\n'+num_dni
        archivo_texto.write(datos_recibidos)
        archivo_texto.close()
        self.app.root.current='historial_screen'
        #self.ficha=self.ids['ficha']
        #self.ficha.remove_widget(self.grid.children[0])
        #print(fila)