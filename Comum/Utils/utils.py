import json as json_lib

class JSONTool:
    json_data: str
    
    def __init__(self, json_data: str):
        self.json_data = json_data

    def get(self, campo):
        try:
            return json_lib.loads(self.json_data)[campo]
        except Exception as e:
            raise ValueError(f"Não foi possível retornar o conteúdo do JSON {self.json_data}\n{str(e)}")

class FileTool:
    file_name: str
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def save(self, text):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write(text)
    
    def load(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
            return f.read()