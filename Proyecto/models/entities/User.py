from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, username, password, Tipo_usuario, Nombre_completo="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.Tipo_usuario = Tipo_usuario
        self.Nombre_completo = Nombre_completo
        
    @classmethod
    def check_password(self, hashed_password, password):
            return check_password_hash(hashed_password, password)
            
