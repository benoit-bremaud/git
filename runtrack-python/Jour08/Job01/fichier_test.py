
# test = "7508dde48bb5e43cf0e4e5d183e5b97dc9f337f5d5b36c6f8caf2a8d77a54fb3"
# with open("Jour08/Job01/myfile.txt", "r") as file:
#     for i in file.readlines():
#         if i.rstrip("\n") == test:
#             print(i)
#             print(test)
#             print("ok")
#         print(i)

import maskpass

pwd = maskpass.askpass()
print(pwd)

