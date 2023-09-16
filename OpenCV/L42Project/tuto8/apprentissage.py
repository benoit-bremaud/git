import cv2
import os
import numpy as np
import pickle

image_dir=r"C:\Users\bbrem\Desktop\git\OpenCV\L42Project\tuto8\photos"
current_id=0
label_ids={}
x_train=[]
# x_train = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
y_labels=[]

# Créez une liste pour stocker les images redimensionnées
resized_images = []

for root, dirs, files in os.walk(image_dir):
    if len(files): # s'il y a des images
        label=root.split("\\")[-1] # récupérer le nom de la personne, on récupère le dernier argument du tableau
        for file in files: # on pourcours tout le tableau "files"
            if file.endswith("png"): # on récupère les fichiers qui se terminent par "*.png"
                path=os.path.join(root, file) # on concatène "root" + "files"
                if not label in label_ids: # est ce que le "label" est déjà présent dans le "label_ids"
                    label_ids[label]=current_id # Si ce n'est pas le cas, on l'ajoute
                    current_id+=1
                id_=label_ids[label]
                image=cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                
                # Redimensionnez l'image ici
                height, width = 100, 100  # Mettez les dimensions souhaitées ici
                resized_image = cv2.resize(image, (width, height))

                # Ajoutez l'image redimensionnée à la liste
                resized_images.append(resized_image)
                
                x_train.append(image) # Un tableau
                y_labels.append(id_) # Un autre tableau



with open(r"C:\Users\bbrem\Desktop\git\OpenCV\L42Project\tuto8\photos\labels.pickle", "wb") as f:
    pickle.dump(label_ids, f)

# Fonction d'apprentissage
# print(x_train)
# x_train=np.array(x_train)

# Convertissez la liste d'images redimensionnées en un tableau NumPy
x_train_resized = np.array(resized_images)

y_labels=np.array(y_labels)

recognizer=cv2.face.LBPHFaceRecognizer_create()
# recognizer=cv2.face.LBPHFaceRecognizer()
# recognizer = cv2.createLBPHFaceRecognizer()
# recognizer = cv2.face.createLBPHFaceRecognizer()

recognizer.train(x_train, y_labels)
recognizer.save(r"C:\Users\bbrem\Desktop\git\OpenCV\L42Project\tuto8\photos\trainner.yml")
