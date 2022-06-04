import base64

class Image_to_base64(object):
    
    def __init__(self, route_image = ''):
        route_image = route_image
        self.route_image = route_image
    
    
    def conver(self):
        """conver  esta función regresa el nombre de la imagen en base64
            
            Toma en cuenta el atributo route_image para convertir la imagen

        Returns:
            str: imagen en base 64
        """
        try:        
            image = open(self.route_image, 'rb')
            image_read = image.read()
            image_64_encode = base64.encodestring(image_read)
            return image_64_encode.decode()
            
        except Exception as err:
            print(err)
            return ''