import psycopg2
import json
import os


class Database:
    CONFIG_PATH = os.path.dirname(os.path.realpath(__file__)) + r'/config/database.json'
    
    def __init__(self) -> None:
        file = open(self.CONFIG_PATH, 'r')
        config = json.loads(file.read())
        file.close()
        
        self.connection = psycopg2.connect(
            dbname=config['database'],
            user=config['username'],
            password=config['password'],
            host=config['host'],
            port=config['port']
        )
        self.cursor = self.connection.cursor()
    
    def execute(
        self,
        query: str,
        binds: list
    ) -> None:
        self.cursor.execute(query, binds)
        
    def commit(self) -> None:
        self.connection.commit()
        
    def fetchall(self) -> list:
        return self.cursor.fetchall()