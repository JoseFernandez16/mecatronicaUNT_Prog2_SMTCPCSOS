from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder

#Para la conexion con la BD
from conexion_BD import Conexion_BD

#importando pantallas
from navigation_screen import NavigationScreen
from login_screen import LoginScreen
#transicion
from kivy.clock import Clock
#trabajar con txt
from io import open

kv="""
<SplashScreen>
    name: "splash_screen"
    md_bg_color:1,1,1,1
    Image:
        source:'recursos/imagenes/logo2.png'
        size_hint:(.9,.9)
        pos_hint:{'center_x':.5,'center_y':.5}
"""
class SplashScreen(MDScreen):
    Builder.load_string(kv)

    def __init__(self,**kw):
        super().__init__(**kw)
        self.app=MDApp.get_running_app()
        self.mi_conexion=Conexion_BD()
        

    def on_enter(self):
        pantalla_navegacion=NavigationScreen()
        pantalla_inicio=LoginScreen()
        self.app.root.add_widget(pantalla_navegacion)
        self.app.root.add_widget(pantalla_inicio)
        try:
            with open("info_paciente.txt","r") as f:
                lineas_texto=f.readlines()
                nombre=lineas_texto[0];apellido=lineas_texto[1];num_dni=lineas_texto[2];centro=lineas_texto[3]
                f.close()
                self.mi_conexion.verificar_mi_conexion(nombre,apellido,num_dni,centro)
                Clock.schedule_once(lambda dt:self.cargar_navegacion(),2)

        except:
            Clock.schedule_once(lambda dt:self.cargar_login(),2)
            #print('cambiar al login')
    
    def cargar_navegacion(self):
        self.app.root.current='navigation_screen'
    
    def cargar_login(self):
        self.app.root.current='login_screen'
