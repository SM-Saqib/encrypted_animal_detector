


def encryption(path):
    try:
        fin = open(path, 'rb')
        
        # storing image data in variable "image"
        image = fin.read()
        fin.close()
        
        # converting image into byte array to
        # perform encryption easily on numeric data
        image = bytearray(image)
    
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key
    
        # opening file for writing purpose
        fin = open(path, 'wb')
        
        # writing encrypted data in image
        fin.write(image)
        fin.close()
        print('Encryption Done...')
    
        
    except Exception:
        print('Error caught : ', Exception.__name__)

def decryption(path):
    try:
        # open file for reading purpose
        fin = open(path, 'rb')
        
        # storing image data in variable "image"
        image = fin.read()
        fin.close()
        
        # converting image into byte array to perform decryption easily on numeric data
        image = bytearray(image)
    
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key
    
        # opening file for writing purpose
        fin = open(path, 'wb')
        
        # writing decryption data in image
        fin.write(image)
        fin.close()
        print('Decryption Done...')
 
 
    except Exception:
        print('Error caught : ', Exception.__name__)
