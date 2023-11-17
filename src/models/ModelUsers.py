from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, fullname, usertype):
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.usertype = usertype

class ModelUsers:
    @classmethod
    def login(cls, db, user):
        try:
            cursor = db.connection.cursor()
            cursor.execute("call sp_verifyIdentity(%s, %s)", (user.username, user.password))
            row = cursor.fetchone()
            if row and len(row) >= 5:
                logged_user = User(row[0], row[1], row[2], row[3], row[4])
                return logged_user
            else:
                return None
        except Exception as ex:
            print("Error en el modelo de usuarios:", ex)
            raise Exception(ex)
        finally:
            cursor.close()

    @classmethod
    def get_by_id(cls, mysql, id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT id, username, usertype, fullname FROM users WHERE id = %s", (id,))
            row = cursor.fetchone()
            if row:
                user = User(row[0], row[1], '', row[3], row[2])
                return user
            else:
                return None
        except Exception as ex:
            print("Error al obtener usuario por ID:", ex)
            raise Exception(ex)
        finally:
            cursor.close()
