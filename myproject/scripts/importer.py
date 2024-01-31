import json
import re

def importer_json_data(file_path='/Data/import - pilotlog_mcc.json'):
    with open("import - pilotlog_mcc.json","r") as file:
        content=file.read()
        format_content=re.sub(r'\\\"', '"', content)
        data=json.loads(format_content)
        return data
        
        
if __name__=="__main__":
    imported_data=importer_json_data()
    
    if imported_data:
        print(imported_data)
    
    
 

