import hashlib
a_string = "Ce texte contient des informations importantes et confidentielles"
a_string2 = "Ce texte contient également des informations importantes et confidentielles"

print("\n"+a_string)
print("\n"+a_string2+"\n")

val1 = hashlib.sha256(a_string.encode("utf-8")).hexdigest()
print(val1)
val2 = hashlib.sha256(a_string2.encode("utf-8")).hexdigest()
print(val2)

f = open("myfile1.txt", "w") # Création du fichier 'myfile3.txt'
f = open("myfile1.txt", "+a")
f.writelines("Now the file has more content!")
f.write(val1)
f.write(val2)
f.close()
f = open("myfile1.txt","r")
print(f.read())
