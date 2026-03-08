Face Control PC (UAV)

Sistema de reconocimiento facial para controlar el computador utilizando movimientos de los ojos y gestos faciales, además de estimar la edad del usuario mediante visión por computadora.

Descripción

Este proyecto utiliza visión por computadora para interactuar con el sistema operativo sin necesidad de teclado o mouse físico.

El sistema permite:

Detectar el rostro en tiempo real

Mover el cursor del mouse usando el iris del ojo

Realizar clics mediante parpadeos

Estimar la edad del usuario mediante inteligencia artificial

Tecnologías utilizadas

Python

OpenCV

MediaPipe

TensorFlow

PyAutoGUI

NumPy

Instalación

Clonar el repositorio

git clone https://github.com/usuario/face-control-pc.git

Entrar al proyecto

cd face-control-pc

Instalar dependencias

pip install -r requirements.txt
Uso

Ejecutar el archivo principal:

python main.py

El sistema activará la webcam y comenzará a detectar el rostro.

Funcionalidades actuales

Detección facial

Seguimiento del iris

Control del mouse con los ojos

Click con parpadeo

Funcionalidades futuras

Reconocimiento facial para autenticación

Control completo del sistema operativo

Interfaz gráfica

Mejora del modelo de estimación de edad

Soporte para múltiples usuarios

Estructura del proyecto
face_control_pc/
│
├── main.py
├── requirements.txt
├── README.md
│
├── models/
│
├── modules/
│
└── utils/
Autor

Proyecto académico de visión por computadora.