from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, db, usuarios):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT id, username, password, Tipo_usuario, Nombre_completo FROM usuarios 
                WHERE username = '{}' """.format(usuarios.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                usuarios=User(row[0], row[1],User.check_password(row[2], usuarios.password),row[3] ,row[4])
                return usuarios
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
            
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, Tipo_usuario, Nombre_completo FROM usuarios WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1], None, row[2],  row[3])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)