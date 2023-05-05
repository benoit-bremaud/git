import hashlib
a_string = "Azerty123@" #Ce texte contient des informations importantes et confidentielles"
a_string2 = "Ce texte contient egalement des informations importantes et confidentielles"

print("\n"+a_string)
print("\n"+a_string2+"\n")

print(str(a_string.encode("utf-8"))+"\n")
print("")
print(str(a_string2.encode("utf-8"))+"\n")
print("")
print(hashlib.sha256(a_string.encode("utf-8")).hexdigest())
print("")
print(hashlib.sha256(a_string2.encode("utf-8")).hexdigest())