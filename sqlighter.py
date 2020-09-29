import sqlite3

class SQLighter:

    def __init__(self, database_file):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscribtions(self, status = True):
        """Получаем всех активных подписчиков бота """
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'subscriptions'")
