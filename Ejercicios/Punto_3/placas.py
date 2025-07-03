import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Cargar la imagen
img_folder = 'Placas'

# Construir la ruta completa a la carpeta de imágenes
folder_path = os.path.join(current_dir, img_folder)

# Obtener la lista de archivos en la carpeta
file_list = os.listdir(folder_path)


# Iterar sobre cada archivo en la lista
for filename in file_list:
    if filename.endswith('.jpeg'):  # Filtrar por archivos con extensión .jpg (o la extensión que uses)
        img_path = os.path.join(folder_path, filename)
        image = cv2.imread(img_path)
        placa=[]
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        gray=cv2.blur(gray,(3,3))
        # Detección de bordes con Canny
        canny=cv2.Canny(gray,100,200)
        canny=cv2.dilate(canny,None, iterations=1 )

        contours,_ =cv2.findContours(canny,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        #Procesar los contornos encontrados
        for c in contours:

            area=cv2.contourArea(c)            
            
            x,y,w,h=cv2.boundingRect(c)
            epsilon=0.09*cv2.arcLength(c, True)
            approx=cv2.approxPolyDP(c, epsilon, True)
            if  len(approx)==4 and area< 41450 and area > 20000:


                

                cv2.drawContours(image,[c], 0, (0,255,0),2)
                placa=gray[y:y+h,x:x+w]

                # Lectura de texto con tesseract
                text=pytesseract.image_to_string(placa, config= '--psm 11')


                print('Placa', text)
                cv2.imshow('Imagen placa', placa)
                cv2.moveWindow('Imagen placa', 600,10)
             
                
           
        cv2.imshow('Imagen', image)

        cv2.moveWindow('Imagen', 45,10)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
