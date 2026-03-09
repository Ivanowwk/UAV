import cv2

def iniciar_camara():

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("No se pudo abrir la camara")

    return cap