from operator import itemgetter
import re
import json
from datetime import datetime

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

                now = datetime.now()

                data.append({                    
                    'app_code': app_code,
                    'resultado': part[2],
                    'unidad': part[3],
                    'date': f'{now.year}-{now.month}-{now.day}' ,
                    'hour': f'{now.hour}:{now.minute}:{now.second}'
                })                                                

            salto = True
        
        _NIM = self.handle_get_nim()
        json_response = {
            'nim':_NIM,
            'resultados':data,
            'cadena':self.cadena
        }
        
        return json_response
        
        
        
        
    def  handle_get_nim(self):
        """
            el nim llega sobre el segmento O|            
        """
        separa = self.cadena.split('O|')        
        separa2 =separa[1].split('|')        
        segmenta = separa2[2].split('^')
        
        nim = segmenta[2]
        
        if nim == '':            
            for item in separa2:
                if item != '' and item.isdigit():                    
                    if len(item) >= 13 :
                        nim = item
                        break

                
                
        return nim
        

        
