import cv2
import operator

# On précise le fichier cascade
face_cascade=cv2.CascadeClassifier(r"C:\Users\bbrem\OneDrive\Documents\OpenCV\L42Project\haarcascade_frontalface_alt2.xml")
profile_cascade=cv2.CascadeClassifier(r"C:\Users\bbrem\OneDrive\Documents\OpenCV\L42Project\haarcascade_profileface.xml")

# TRécupère l'entrée vidéo de la webcam, 0-> cam intégré, 1-> cam extérieur
cap=cv2.VideoCapture(0)

# on récupère la largeur de l'image 3-> largeur, 4-> hauteur
width=int(cap.get(3))

# marge entre 2 rectangles
marge=70

# Début de la boucle
while True:
    
    # Récupère les images de la webcam
    ret, frame=cap.read()
    
    # initialisation du tableau dans le quel sera stocké tous les visages
    tab_face=[]
    
    # prend des mesures de temps 
    tickmark=cv2.getTickCount()
    
    # transformer l'image en noir et blanc
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # appelle de la fonction 'detectMultiscale' appliquée à 'face_cascade' renvoi une liste de quadruplés
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
    
    for x,y,w,h in face:
        tab_face.append([x,y,x+w,y+h])
    
    face=profile_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
    
    for x,y,w,h in face:
        tab_face.append([x,y,x+w,y+h])
    
    # on effectue une symétrie 0-> axe horizontale, 1-> axe verticale
    gray2=cv2.flip(gray, 1)
    
    
    face=profile_cascade.detectMultiScale(gray2, scaleFactor=1.2, minNeighbors=4)

    for x,y,w,h in face:
        tab_face.append([width-x, y, width-(x+w), y+h])
    
    # on trie le tableau selon la colonne  (0,1) selon x et y   
    tab_face=sorted(tab_face, key=operator.itemgetter(0,1))
    
    index=0
    
    for x,y,x2,y2 in tab_face:
        if not index or (x-tab_face[index-1][0]>marge or y-tab_face[index-1][1]>marge):
            cv2.rectangle(frame, (x,y), (x2,y2), (0,0,255), 2)
        index+=1
        
            
    # fonction quitter le programme
    if cv2.waitKey(1)==ord('q'):
        break
    
    # prend une deuxième mesure de temps et calcule le frame rate
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    
    # affiche le nombre de frame frame_rate
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0),2)
    
    # affiche l'image avec les rectangles dessinés
    cv2.imshow('video', frame)

# libère toutes les resources
cap.release()

# détruit toutes les fenêtres qui ont été créées
cv2.destroyAllWindows()
