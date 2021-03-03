from pymongo import MongoClient
from io import open


class Conexion_BD():

    def get_db(self):
        try:
            self.client=MongoClient("mongodb+srv://WilliamHuaman:MUfbSr5qOCkXJWur@proyectoprogramacion.u4hsj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            self.db=self.client.ProyectoProgramacion
        except ConnectionError:
            print('Error de conexion')
        return self.db

    def inicio_sesion(self,email,password):
        db=self.get_db()
        dato=db.pacientes.find_one({'email':email,'password':password},{'_id':0,'nombres':1,'apellidos':1,'dni':1,'centro':1})
        if dato==None:
            #a=('no existe la cuenta')
            return False
        else:
            nombre=dato['nombres'];apellido=dato['apellidos'];num_dni=str(dato['dni']);centro=dato['centro']
            #print(nombre+'\n'+apellido+'\n'+num_colegiatura+'\n'+trabajo)

            archivo_texto=open('info_paciente.txt','w')
            datos_recibidos=nombre+'\n'+apellido+'\n'+num_dni+'\n'+centro
            archivo_texto.write(datos_recibidos)
            archivo_texto.close()
            return True

        
    def verificar_mi_conexion(self,nombre,apellido,num_dni,centro):
        db=self.get_db()
        dato=db.pacientes.find({"nombres":nombre,'apellidos':apellido,'colegiatura':num_dni,'centro':centro},{'_id':0,"nombres":1})#
        if dato==None:
                print('ir a login')
        else:
            print('ir al navigation')
    
    def insertar_dato(self,dato):
        db=self.get_db()
        db.mediciones_pacientes.insert_one(dato)
    
    # def consultar_historial(self,dni):
    #     db=self.get_db()
    #     mediciones=db.mediciones_pacientes.find({'dni':dni},{'_id':0,'fecha':1,'hora':1,'pulso':1,'temperatura':1,'oxigeno':1}).sort('fecha_int',1)
    #     # for medicion in mediciones:
    #     #     print(type(medicion))
        

class MedicionesPacientes:
    def __init__(self,dni,fecha,fecha_int,hora,hora_int,pulso,temperatura,oxigeno):
        self.dni=dni
        self.fecha=fecha
        self.fecha_int=fecha_int
        self.hora=hora
        self.hora_int=hora_int
        self.pulso=pulso
        self.temperatura=temperatura
        self.oxigeno=oxigeno
    
    def toCollection(self):
        return{
            'dni':self.dni,
            'fecha':self.fecha,
            'fecha_int':self.fecha_int,
            'hora':self.hora,
            'hora_int':self.hora_int,
            'pulso':self.pulso,
            'temperatura':self.temperatura,
            'oxigeno':self.oxigeno
        }

        