from operator import itemgetter
from pickle import TRUE
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
                    'hour': f'{now.hour}:{now.minute}:{now.second}',
                    'bandera':True
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
        try:
            
            cadena = self.cadena
            cadena = cadena.rstrip('\n')
            separa = self.cadena.split('O|',1)   
            
            dataset =  separa[1].split('|')
            
            nim = ''
            for element in dataset:
                # limpiamos la cadena para que solo queden numeros
                element = re.sub(r"[^0-9]","",element)
                # si la cadena llega a tener espacios o saltos de linea los quitamos
                element = element.strip()
                # si la cadena es un digito y el numero de caracteres en 9 lo tomamos en cuenta como el nim y rompemos el siclo
                if element.isdigit() and len(element) > 9:
                    nim = element
                    break


            if nim == '':
                nim = 'na'

                            
            return nim
        except Exception as e:
            print(e)
            return 'na'
        
        

        
