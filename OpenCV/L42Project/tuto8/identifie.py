# !/usr/bin/env python
import cv2
import pickle
import numpy as np
import common as c  # Importez le module "common" (s'il existe) pour des valeurs constantes

# Chargez le classificateur en cascade pour la détection de visages
face_cascade = cv2.CascadeClassifier(r"C:\Users\bbrem\Desktop\git\OpenCV\L42Project\tuto8\haarcascade_frontalface_alt2.xml")

# Créez un reconnaisseur de visage LBPH (Local Binary Pattern Histogram)
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Chargez le modèle d'entraînement préalablement enregistré
recognizer.read(r"C:\Users\bbrem\Desktop\git\OpenCV\L42Project\tuto8\photos\trainner.yml")

# Variables pour la gestion de l'affichage et de l'identification
id_image = 0
color_info = (255, 255, 255)  # Couleur du texte d'information
color_ko = (0, 0, 255)        # Couleur pour les visages non reconnus
color_ok = (0, 255, 0)        # Couleur pour les visages reconnus

# Définir la largeur et la hauteur souhaitées pour la nouvelle résolution
nouvelle_largeur = 640  # Remplacez par la largeur désirée
nouvelle_hauteur = 480  # Remplacez par la hauteur désirée

# Chargez les étiquettes de correspondance des identifiants de visage
with open(r"C:\Users\bbrem\Desktop\git\OpenCV\L42Project\tuto8\photos\labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}  # Inversez les étiquettes (id -> nom)

# Capture vidéo à partir d'un fichier
cap = cv2.VideoCapture(r"C:\Users\bbrem\Desktop\git\OpenCV\L42Project\tuto8\production.mp4")

while True:
    ret, frame = cap.read()  # Capturez une image du flux vidéo
    
    # Redimensionner le cadre à la nouvelle résolution
    frame = cv2.resize(frame, (nouvelle_largeur, nouvelle_hauteur))
    
    tickmark = cv2.getTickCount()  # Mesurez le temps écoulé pour chaque image

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertissez l'image en niveaux de gris

    # Détection des visages dans l'image en utilisant le classificateur en cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(c.min_size, c.min_size))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]  # Région d'intérêt (visage) en niveaux de gris

        # Utilisez le reconnaisseur pour prédire l'identité du visage
        # id_ : identifiant de l'utilisateur, conf : score de confiance de la prédiction
        id_, conf = recognizer.predict(roi_gray)

        if conf <= 95:  # Si le score de confiance est inférieur à 95 (peut être ajusté)
            color = color_ok  # Utilisez la couleur de confirmation (vert)
            name = labels[id_]  # Obtenez le nom correspondant à l'identifiant
        else:
            color = color_ko  # Sinon, utilisez la couleur pour les visages non reconnus (rouge)
            name = "Inconnu"

        label = name + " " + '{:5.2f}'.format(conf)  # Créez une étiquette avec le nom et le score de confiance
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, color_info, 1, cv2.LINE_AA)

        # Dessinez un rectangle autour du visage
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - tickmark)  # Calculez le nombre d'images par seconde (FPS)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color_info, 2)

    cv2.imshow('L42Project', frame)  # Affichez la vidéo en temps réel
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # Appuyez sur 'q' pour quitter
        break

    if key == ord('a'):  # Appuyez sur 'a' pour avancer rapidement dans la vidéo (facultatif)
        for cpt in range(100):
            ret, frame = cap.read()

cv2.destroyAllWindows()  # Fermez

# Affichez un message de fin
print("Fin")
