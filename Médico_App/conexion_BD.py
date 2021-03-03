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

    def obtener_pacientes(self,centro):
        db=self.get_db()
        pacientes=db.pacientes.find({'centro':centro},{'_id':0,'nombres':1,'apellidos':1,'email':1,'celular':1,'edad':1,'direccion':1,'departamento':1,'ciudad':1,'dni':1})
        lista_pacientes=list(pacientes)
        # for paciente in pacientes:
        #     print(paciente)
        #print(centro)
        return lista_pacientes


    def inicio_sesion(self,email,password):
        db=self.get_db()
        dato=db.medicos.find_one({'email':email,'password':password},{'_id':0,'nombres':1,'apellidos':1,'colegiatura':1,'centro':1})
        if dato==None:
            #a=('no existe la cuenta')
            return False
        else:
            nombre=dato['nombres'];apellido=dato['apellidos'];num_colegiatura=str(dato['colegiatura']);trabajo=dato['centro']
            #print(nombre+'\n'+apellido+'\n'+num_colegiatura+'\n'+trabajo)

            archivo_texto=open('info_medico.txt','w')
            datos_recibidos=nombre+'\n'+apellido+'\n'+num_colegiatura+'\n'+trabajo
            archivo_texto.write(datos_recibidos)
            archivo_texto.close()
            return True

        

    def verificar_mi_conexion(self,nombre,apellido,num_colegiatura,centro_trabajo):
        db=self.get_db()
        dato=db.medicos.find({"nombres":nombre,'apellidos':apellido,'colegiatura':num_colegiatura,'centro':centro_trabajo},{'_id':0,"nombres":1})#
        if dato==None:
                print('ir a login')
        else:
            print('ir al navigation')
        