import json

class CrudHelper:
    def __init__(self, file_path='patients.json'):
        self.file_path = file_path
        
    def read_json(self):
        data = ""
        with open(self.file_path , 'r') as file:
            data = json.load(file)
        return data