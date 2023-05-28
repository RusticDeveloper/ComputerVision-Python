import cv2  as cv2

# obtener images de la mcamara
captura = cv2.VideoCapture(0)

while True:
    # Leer el frame de la cámara
    ret, frame = captura.read()

    # Mostrar el frame en una ventana
    cv2.imshow('Cámara', frame)

    # Esperar hasta que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Liberar los recursos de la cámara
captura.release()

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()
