import json
import os 

class Token:
    TOKEN_PATH = os.path.dirname(os.path.realpath(__file__)) + r'/config/bot.json'
    
    def __init__(self) -> None:
        file = open(self.TOKEN_PATH, 'r')
        self.contents = file.read()
        file.close()
    
    def get(self) -> str:
        return json.loads(self.contents)['token']