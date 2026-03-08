import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Inicializar mediapipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Captura de cámara
cam = cv2.VideoCapture(0)

# Tamaño de pantalla
screen_w, screen_h = pyautogui.size()

while True:
    success, frame = cam.read()
    if not success:
        break

    # Voltear imagen
    frame = cv2.flip(frame, 1)

    frame_h, frame_w, _ = frame.shape

    # Convertir a RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar rostro
    output = face_mesh.process(rgb_frame)

    landmark_points = output.multi_face_landmarks

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Coordenadas del ojo derecho
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)

            cv2.circle(frame, (x, y), 3, (0,255,0))

            if id == 1:
                screen_x = int(screen_w * landmark.x)
                screen_y = int(screen_h * landmark.y)

                pyautogui.moveTo(screen_x, screen_y)

        # Parpadeo para click
        left = landmarks[145]
        right = landmarks[159]

        if (left.y - right.y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow("Eye Controlled Mouse", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()