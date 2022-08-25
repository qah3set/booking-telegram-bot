import psycopg2
import json


class Database:
    CONFIG_PATH = r'./config/database.json'
    
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
        query: str,
        binds: list,
        fetch: bool = False,
        commit: bool = True
    ) -> list:
        self.cursor.execute(query, binds)
        return self.cursor.fetchall()
        # def execute(self, query, bindings, should_fetch, should_commit=False):
        #     self.cursor.execute(query, bindings)
            
        #     if should_commit:
        #         self.connection.commit()
                
        #     if should_fetch:
        #         return self.cursor.fetchall()