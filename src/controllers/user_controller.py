from src.models.user_model import UserModel
from src.utils.security import Security

class UserController:
    def __init__(self):
        pass

    def get_users(self):
        # Iniciamos la clase UserModel y llamamos al metodo read_users
        return UserModel().read_users()

    def create_user(self, data:dict):
        pass
if __name__ == '__main__':
    # Iniciamos el objeto UserController para poder llamar el metodo get_users -> Si quiero hacer una prueba solo descomentar
    # user_controller = UserController()
    # print(user_controller.get_users())

    pass