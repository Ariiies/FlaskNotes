#from user2 import User
from .entities.user import User

class ModelUser:

    @classmethod
    def login(self,cursor,user):
        try:
            sql =f"SELECT id, nombre, apellidos,  username, email, pass FROM user WHERE nombre = '{user.name}'"
            row = cursor(sql)
            if row != None:
                user = User(row[0][0], row[0][1], row[0][2],row[0][3],row[0][4],User.check_password(row[0][5],user.password))
                return user
            else:
                return None
        except Exception as e:
            return None
       
        
    @classmethod
    def get_by_id(self, cursor, id):
        try:
            sql =f"SELECT id, nombre, apellidos,  username, email FROM user WHERE nombre = '{id}'"
            row = cursor(sql)
            if row != None:
                user = User(row[0][0], row[0][1], row[0][2],row[0][3],row[0][4],None)
                return user
            else:
                return None
        except Exception as e:
            return type(e).__name__
        
        