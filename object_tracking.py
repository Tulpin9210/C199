import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

# Carga el rastreador 
tracker = cv2.TrackerCSRT_create()

# Lee el primer cuadro del video
returned, img = video.read()

# Selecciona el campo delimitador de la imagen
bbox = cv2.selectROI("Rastreando", img, False)

# Inicializa el rastreador en la imagen y el campo delimitador
tracker.init(img, bbox)

print(bbox)



while True:
    check,img = video.read()   

    cv2.imshow("resultado",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("¡Alto!")
        break


video.release()
cv2.destroyALLwindows()







