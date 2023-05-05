print("""\nProgramme Jour 4 - Job12
      \nÉcrire un programme qui trie dans l'ordre croissant une liste passés en paramètre."""
      )

L=[8,24,27,48,2,16,9,102,7,84,91]

# ranger la liste par ordre croissant
print("Liste avant classement")
print(L)
end_index=len(L)
for i in range(len(L)):
    num = L[0]
    end_index = (len(L)-i)
    print(num)
    print(end_index)
    for nbr in range(len(L[i:end_index:])):
        if nbr > num:
            num = nbr
    L[-1+i]=num
    
print(L)