import json


class Token:
    TOKEN_PATH = r'./config/bot.json'
    
    def __init__(self) -> None:
        file = open(self.TOKEN_PATH, 'r')
        self.contents = file.read()
        file.close()
    
    def get(self) -> str:
        return json.loads(self.contents)['token']