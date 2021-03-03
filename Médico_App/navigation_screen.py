from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem,IconLeftWidget
from kivymd.app import MDApp
from functools import partial
import sys
class ListIcon(OneLineIconListItem):
    def __init__(self,**kw):
        super().__init__()
        self.text=kw['text']
        self.icon=IconLeftWidget(icon=kw['icon'])
        self.add_widget(self.icon)
        self.on_release=kw['on_release']



kv="""
<NavigationScreen>
    name:'navigation_screen'
    NavigationLayout:
        id:nav_layout
        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:tool_bar
                        title:'Medic-App'
                        left_action_items:[["menu",lambda x: nav_drawer.set_state()]]
                    ScreenManager:
                        id:screen_manager
        
        MDNavigationDrawer:
            id:nav_drawer
            MDBoxLayout:
                orientation:'vertical'
                padding: "8dp"
                spacing: "8dp"

                Image:
                    size_hint_y: .3
                    source:'recursos/imagenes/logo1.jpg'

                ScrollView:
                    MDList:
                        id:nav_list
                        OneLineIconListItem:
                            text:'Cerrar Sesión'
                            on_release:app.cerrar_sesion()

                            IconLeftWidget:
                                icon:"home-variant"

"""
class NavigationScreen(MDScreen):
    Builder.load_string(kv)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app=MDApp.get_running_app()
        #lista de las pantallas (id,titulo[text],icono)
        from login_screen import LoginScreen
        from pacientes_screen import PacientesScreen
        from informacion_screen import InformacionScreen
        from pacientes_screen import HistorialScreen

        self.list_screen = {
            InformacionScreen:('information_screen','Información','settings'),
            PacientesScreen:('pacientes_screen','Pacientes','settings')
            
        }

    def on_enter(self, *args):
        for screen,details in self.list_screen.items():
            identification,text,icon=details
            self.ids.screen_manager.add_widget(screen(name=identification))
            self.ids.nav_list.add_widget(ListIcon(text=text,icon=icon,on_release=partial(self.button_list_actions,text,identification)))  
        
    def button_list_actions(self,title,identification):
        self.ids.tool_bar.title=title
        self.ids.screen_manager.current=identification
        self.ids.nav_drawer.set_state()
    
    
    def cerrar_sesion(self):
        archivo_texto=open('info_paciente.txt','w')
        archivo_texto.write('')
        archivo_texto.close()
        sys.exit()
