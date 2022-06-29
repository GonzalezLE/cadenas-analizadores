from classes.parse import Parse
from settings.settings import CADENA,CADENA_NUEVA


if __name__ == '__main__':
    
    resultados = Parse(CADENA_NUEVA)
        
    respuesta = resultados.separa_cadena()
    
    print(respuesta)
    
    
    
    