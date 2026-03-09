import mediapipe as mp
import pyautogui
import cv2

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh()

screen_w, screen_h = pyautogui.size()


def detectar_gestos(frame):

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:

        for face in results.multi_face_landmarks:

            iris = face.landmark[474]

            x = int(iris.x * screen_w)
            y = int(iris.y * screen_h)

            pyautogui.moveTo(x, y)

            ojo_sup = face.landmark[159]
            ojo_inf = face.landmark[145]

            if abs(ojo_sup.y - ojo_inf.y) < 0.01:
                pyautogui.click()