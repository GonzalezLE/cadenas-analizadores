import re
import json

class Parse():

    def __init__(self, cadena):
        self.cadena = cadena

    

    def separa_cadena(self):
        """
            Separo la cadena por los resultados la primera posicion no la tomo en cuenta por que es el header                        
        """
        conjuntos = self.cadena.split('R|')
        data = []        

        salto = False
        """
            creamos arreglo con los estudios
        """
        for part in conjuntos:
            if salto:
                part = part.split('|')

                app_code = re.sub(r'[^a-zA-Z0-9]', ' ', part[1])
                app_code = app_code.strip()

                data.append({                    
                    'app_code': app_code,
                    'resultado': part[2],
                    'unidad': part[3],
                })                                                

            salto = True
        
        _NIM = self.handle_get_nim()
        json_response = {
            'nim':_NIM,
            'resultados':data
        }
        
        json_response = rf"{json.dumps(json_response, separators=(',', ':'))}" 
        print(json_response)
        
        json_response.replace('"', '\\"')
        
        file = open(f"./doc/{_NIM}.json", "w")
        json.dump(json_response, file)
        file.close()
        
        
    def  handle_get_nim(self):
        """
            el nim llega sobre el segmento O|            
        """
        separa = self.cadena.split('O|')
        
        separa2 =separa[1].split('|')
        
        segmenta = separa2[2].split('^')
        
        return segmenta[2]        
        

        
