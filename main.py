import cv2

from utils.camara import iniciar_camara
from age_model.age_predict import estimar_edad_emocion
from gestures.face_gestures import detectar_gestos


def main():

    cap = iniciar_camara()

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        edad, emocion = estimar_edad_emocion(frame)

        detectar_gestos(frame)

        if edad is not None:
            cv2.putText(frame, f"Edad: {edad}", (20,40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

        if emocion is not None:
            cv2.putText(frame, f"Emocion: {emocion}", (20,80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

        cv2.imshow("AI Vision Control", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()