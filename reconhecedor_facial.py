import cv2

import mediapipe as mp

# Inicializa o opencv e mediapipe
webcam = cv2.VideoCapture(0)

solucao_reconhecimento_rosto = mp.solutions.face_detection

reconhecedor_rosto = solucao_reconhecimento_rosto.FaceDetection()

desenho = mp.solutions.drawing_utils

while True:
    # Ler as informações da webcam
    verificador, frame = webcam.read()
    if not verificador:
        break

    # Reconhece todos os rostos do vídeo
    lista_rostos = reconhecedor_rosto.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto)


    cv2.imshow("Rostos na Webcam", frame)

    # Espera apertar uma tecla
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()