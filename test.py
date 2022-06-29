
from codecs import unicode_escape_decode, unicode_escape_encode
from classes.Image_to_base64 import Image_to_base64

if __name__ == '__main__':
    
    IMAG = unicode_escape_decode("C:\Users\GonzalezLE\Pictures\haha\podcast-banner.jpg")
    
    
    obj = Image_to_base64(IMAG)
    
    

        
    file = open("./doc/filename.txt", "w")
    file.write(obj.conver())
 
    file.close()
    
    
    
    
    
    









