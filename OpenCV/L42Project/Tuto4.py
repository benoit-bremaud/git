"""
Programme de détection de couleur grave à openCV:

    1- Detection d'un objet grace à sa couleur, couleur différente du fond

    2- On va créer un masque entièrement noir sur le quel l'appareil à détection sera entièrement en pixel blanc
    
    3- Comment afficher les coordonnées de l'objet pour pouvoir écrire un texte juste à côté de l'objet
    
Espace colorimétrique :
La plus part du temps, losqu'on ouvre une image elle est dans un espace colorimétrique RGB (Red Green Blue) qui donne la proportion de Rouge, Vert et Bleu de chacun des pixels de l'image.

Ici, nous allons utiliser l'espace colorimètrique HSV :

Définition :
L'espace colorimétrique HSV, abréviation de Hue, Saturation, Value (teinte, saturation, valeur), est un modèle de représentation des couleurs en trois dimensions. Il est souvent utilisé dans le domaine de la vision par ordinateur, du graphisme et de la conception d'images pour exprimer les couleurs de manière plus intuitive que dans d'autres espaces colorimétriques.

Voici une brève explication des composantes de l'espace colorimétrique HSV :

1. **Teinte (Hue)** : C'est la propriété qui représente la couleur elle-même, définie par un angle sur le cercle des couleurs. Elle varie de 0 à 360 degrés, où 0 (ou 360) correspond au rouge, 120 correspond au vert et 240 correspond au bleu.

2. **Saturation (Saturation)** : Cela mesure la pureté de la couleur. Une saturation élevée signifie que la couleur est vive et intense, tandis qu'une saturation faible peut conduire à une teinte plus terne ou grise.

3. **Valeur (Value ou Brightness)** : C'est la luminosité de la couleur. Elle représente la quantité de lumière dans la couleur, variant de 0 (noir) à 100 (blanc). Elle permet de contrôler la clarté ou l'obscurité de la couleur.

En combinant ces trois composantes, on peut représenter une large gamme de couleurs de manière plus intuitive et souvent plus adaptée à certains types d'applications, comme la sélection de couleurs dans les logiciels de graphisme ou la détection de couleurs dans les applications de vision par ordinateur.


"""

# Début du programme
# Importation des modules nécessaires
import cv2  # Importation du module cv2, qui est une bibliothèque populaire pour le traitement d'images.

import numpy as np  # Importation du module numpy et aliasing avec "np". Numpy est couramment utilisé pour le calcul numérique et les opérations sur les tableaux multidimensionnels.


# Déclaration de constantes
# CONSTANTE1 = valeur1  # Description de la constante 1
# CONSTANTE2 = valeur2  # Description de la constante 2

# Déclaration de variables globales
# variable_globale1 = valeur1  # Description de la variable globale 1
# variable_globale2 = valeur2  # Description de la variable globale 2

# Définition des valeurs minimales pour le masque (teinte minimale, saturation minimale, valeur minimale)
lo = np.array([95, 100, 50])

# Définition des valeurs maximales pour le masque (teinte maximale, saturation maximale, valeur maximale)
hi = np.array([105, 255, 255])

# 
color_infos=(0, 255, 255)

"""
Ces lignes définissent les valeurs minimales (lo) et maximales (hi) pour la création du masque HSV. En HSV, la teinte varie de 0 à 179, la saturation de 0 à 255 et la valeur de 0 à 255. Ainsi, ces valeurs indiquent le seuil pour la couleur que vous souhaitez extraire. La teinte est dans l'intervalle [95, 105], la saturation est dans l'intervalle [100, 255] et la valeur est dans l'intervalle [50, 255]. Ces plages peuvent être ajustées en fonction de la couleur que vous souhaitez extraire du frame HSV.
"""


# # Définition de fonctions
# def fonction1(parametre1, parametre2):
#     """
#     Cette fonction effectue une tâche particulière.
    
#     Args:
#         parametre1 (type): Description du premier paramètre.
#         parametre2 (type): Description du deuxième paramètre.
    
#     Returns:
#         type: Description de la valeur de retour.
#     """
#     # Instructions de la fonction
#     pass

# def fonction2():
#     """
#     Cette fonction effectue une autre tâche.
    
#     No args.
    
#     Returns:
#         type: Description de la valeur de retour.
#     """
#     # Instructions de la fonction
#     pass

# Partie principale du programme
if __name__ == "__main__":
    # Instructions pour l'exécution principale
    # Cette structure permet de définir la logique qui doit être exécutée lorsque le fichier Python est exécuté directement en tant que script.
    # if __name__ est une variable spéciale en Python qui contient le nom du module actuel.
    # Lorsque ce fichier est exécuté directement, __name__ est défini comme "__main__".
    # Ainsi, les instructions placées ici seront exécutées uniquement si ce fichier est le script principal.
    # Initialisation de la capture vidéo à partir de la caméra avec l'indice 1 (la deuxième caméra)
    cap = cv2.VideoCapture(0)
    #  Initialisation de la capture vidéo à partir de la caméra avec l'indice 1 (généralement la deuxième caméra, 0 étant souvent la caméra intégrée à l'ordinateur).

    # Boucle infinie pour capturer en continu depuis la caméra
    while True:
        # Lecture d'un frame depuis la caméra
        ret, frame = cap.read() # Lecture d'une image (frame) depuis la caméra. ret indique si la lecture est réussie, et frame contient l'image capturée.
        

        # Conversion du frame capturé de l'espace de couleur BGR à HSV
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #  Conversion du frame capturé de l'espace de couleur BGR (couleur par défaut dans OpenCV : Bleu, Vert, Rouge) à HSV (teinte, saturation, valeur).

        # Application d'un masque basé sur les valeurs de couleur (lo et hi)
        mask = cv2.inRange(image, lo, hi) # Création d'un masque à partir de l'image HSV en utilisant les valeurs de couleur minimale (lo) et maximale (hi).
        image = cv2.blur(image, (7,7))
        
        # Réduction du bruit et fermeture des trous dans le masque
        mask = cv2.erode(mask, None, iterations=4) # Cette ligne utilise la fonction cv2.erode() pour réduire le bruit et diminuer la taille des zones blanches dans le masque. L'érosion est un processus qui "érode" les bords des objets blancs (régions à détecter) dans le masque. Elle est souvent utilisée pour réduire le bruit ou pour séparer les objets connectés.

        # Expansion du masque pour combler les zones "trouées"
        mask = cv2.dilate(mask, None, iterations=4) # Cette ligne utilise la fonction cv2.dilate() pour dilater le masque, c'est-à-dire pour agrandir les zones blanches. Cela peut être utile pour combler les trous dans les objets blancs ou pour regrouper des parties disjointes d'un objet. Dans ce cas, elle est utilisée pour fermer les trous dans le masque et assurer une détection plus complète.


        # Application du masque pour extraire certaines parties du frame original
        image2 = cv2.bitwise_and(frame, frame, mask=mask)
        
        # Recherche des contours dans le masque
        elements = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        # La fonction findContours de OpenCV est utilisée pour détecter les contours dans l'image du masque. 
        # Elle renvoie une liste de contours trouvés.

        # Vérification s'il y a des contours détectés
        if len(elements) > 0:
            # Sélection du contour avec la plus grande aire
            c = max(elements, key=cv2.contourArea)
            # La fonction max() est utilisée pour obtenir le contour avec la plus grande aire.
            # Ici, l'aire du contour est déterminée par cv2.contourArea().

            # Obtention du cercle d'encadrement minimal pour le contour
            ((x, y), rayon) = cv2.minEnclosingCircle(c)
            # La fonction minEnclosingCircle() est utilisée pour obtenir le cercle d'encadrement minimal pour un contour donné.

            # Vérification du rayon du cercle minimal
            if rayon > 30:
                # Affichage du cercle d'encadrement minimal sur l'image traitée
                cv2.circle(image2, (int(x), int(y)), int(rayon), color_infos, 2)
                # La fonction circle() est utilisée pour dessiner un cercle avec le rayon obtenu autour de l'objet détecté.
                
                # Affichage d'un point au centre du cercle
                cv2.circle(frame, (int(x), int(y)), 5, color_infos, 10)
                # Cela ajoute un point au centre du cercle pour marquer le centre de l'objet détecté.
                
                # Dessin d'une ligne du centre du cercle vers l'extérieur
                cv2.line(frame, (int(x), int(y)), (int(x) + 150, int(y)), color_infos, 2)
                # Ceci dessine une ligne du centre du cercle vers l'extérieur pour indiquer une direction.
                
                # Affichage du texte "Objet !!!" près de l'objet détecté
                cv2.putText(frame, "Objet !!!", (int(x) + 10, int(y) - 10), cv2.FONT_HERSHEY_DUPLEX, 1, color_infos, 1, cv2.LINE_AA)
                # La fonction putText() est utilisée pour afficher un texte à proximité de l'objet détecté.

# Ce bloc de code traite les contours détectés, encadre l'objet avec un cercle, marque le centre, trace une ligne et affiche un texte si le rayon du cercle minimal est supérieur à 30.

        # Affichage du frame original (en couleurs)
        cv2.imshow('Camera', frame) # Affichage image brute

        # Affichage de l'image avec le masque appliqué
        cv2.imshow('image2', image2)

        # Affichage du masque
        cv2.imshow('Mask', mask)
        
        # Attendre une touche (ici, la touche 'q') pour quitter la boucle
        if cv2.waitKey(1) == ord('q'):
            break

    # Libération des ressources de la caméra
    cap.release()

    # Fermeture de toutes les fenêtres d'affichage
    cv2.destroyAllWindows()
            

    pass
