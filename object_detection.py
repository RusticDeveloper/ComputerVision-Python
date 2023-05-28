import cv2

# Inicializar el objeto de detección y seguimiento
tracker = cv2.TrackerCSRT_create()

# Inicializar la cámara web
video = cv2.VideoCapture(0)

# Leer el primer fotograma de la cámara
ret, frame = video.read()

if ret == False:
    video.release()
    cv2.destroyAllWindows()


# Seleccionar la región de interés (ROI) a seguir
roi = cv2.selectROI(frame, False)

# Inicializar el tracker con la ROI seleccionada
tracker.init(frame, roi)

# Bucle para procesar cada fotograma de la cámara
while True:
    # Leer el fotograma actual de la cámara
    ret, frame = video.read()

    # Actualizar el tracker con el nuevo fotograma
    success, box = tracker.update(frame)

    # Dibujar el objeto rastreado en el fotograma
    if success:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el fotograma resultante con el objeto rastreado
    cv2.imshow('Detección y Seguimiento de Objetos', frame)

    # Detener el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
video.release()
cv2.destroyAllWindows()
