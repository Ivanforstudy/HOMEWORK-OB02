class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'  # Уровень доступа для обычных сотрудников

    # Геттеры
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администраторов
        self.__users_list = []  # Список пользователей

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User):
            self.__users_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: добавляемый объект не является пользователем.")

    # Метод для удаления пользователя
    def remove_user(self, user_id):
        for user in self.__users_list:
            if user.get_user_id() == user_id:
                self.__users_list.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Ошибка: пользователь с таким ID не найден.")

    # Геттер для списка пользователей
    def get_users_list(self):
        return [user.get_name() for user in self.__users_list]

# Пример использования
if __name__ == "__main__":
    # Создаем администраторов и пользователей
    admin = Admin(user_id=1, name="Admin1")
    user1 = User(user_id=2, name="User 1")
    user2 = User(user_id=3, name="User 2")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)

    # Выводим список пользователей
    print("Список пользователей:", admin.get_users_list())

    # Администратор удаляет пользователя
    admin.remove_user(user_id=2)

    # Выводим обновленный список пользователей
    print("Обновленный список пользователей:", admin.get_users_list())

Найти еще