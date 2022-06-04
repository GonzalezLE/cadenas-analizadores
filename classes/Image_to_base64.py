import base64

class Image_to_base64(object):
    
    def __init__(self, route_image = ''):
        self.route_image = route_image
    
    
    def conver(self):
        """conver  esta función regresa el nombre de la imagen en base64
            
            Toma en cuenta el atributo route_image para convertir la imagen

        Returns:
            str: imagen en base 64
        """
        try:
            with open(self.route_image) as img:
                data = img.read()
                base64_data = base64.b64encode(data)
                base64_data_str = base64_data.decode('utf-8')
                return base64_data_str
            
        except Exception as err:
            print(err)
            return ''