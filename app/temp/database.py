import psycopg
from .model.user import User


class Database:
    def __init__(self, url: str):
        assert isinstance(url, str)
        self.connection = psycopg.connect(url)
        self.cursor = self.connection.cursor()

    def insert(self, command: str, var: tuple | None = None):
        assert isinstance(command, str)
        assert isinstance(var, None) or isinstance(var, tuple)
        if var is not None:
            self.cursor.execute(command, var)
        else:
            self.cursor.execute(command)
        self.cursor.commit()

    def fetch(self, command, fetch_all: bool = False):
        assert isinstance(command, str)
        assert fetch_all in [0, 1]
        self.cursor.execute(command)
        return self.cursor.fetchall() if fetch_all else self.cursor.fetchone()[0]