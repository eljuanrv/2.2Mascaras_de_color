# 2.2Mascaras_de_color
Es la segunda tarea del Segundo Parcial de mi materia de Análisis y Procesamiento de Imágenes

## *INSTRUCCIONES*

1. Elegir una pieza de color uniforme que tengan en su casa (de preferencia que sea rojo, verde o azul)
2. Capturar un video formado por frames en un while del objeto en un fondo sólido
3. Mostrar (en ventanas) los resultados del frame original y de la máscara aplicada al objeto
Nota: En en el paso anterior se debe apreciar completamente negro el entorno y blanco el objeto.

Entregables:
1. imagen jpg con los 2 frames tomados
1. código py
```
import cv2
import numpy as np


cap = cv2.VideoCapture(0)


azulClaro = np.array([90,0,0],np.uint8) #237,241,73
azulOscuro = np.array([130,255,255],np.uint8)
while(True):
    ret,frame = cap.read()


    if (ret == True):
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV,azulClaro,azulOscuro)
        cv2.imshow('maskAzul',mask)        
        cv2.imshow('frame',frame)
        if( cv2.waitKey(1) & 0xFF == ord('s')):
            break
cap.release()
cv2.destroyAllWindows()
```
