#import turtle
from ast import Break


print("\n")

print("------------Bienvenue dans l'application des calculs de la moyenne des notes d'un étudiant------------- \n")
ListeMat=[]
ListeNote=[]
while True:    
    try:
        fristname=input(" Veuillez saisir le nom de famille de l'étudiant \n")
        fristname=int(fristname)
        print("Le nom de Famille ne contient pas de chriffre SVP !!! \n")
        
    except ValueError:
        break
while True:    
    try:
        lastname=input(" Veuillez saisir le Prénom de l'étudiant \n")
        lastname=int(lastname)
        print("Le Prénom ne contient pas de chriffre SVP !!! \n")
        
    except ValueError:
        
        #print(f"L'étudiant enregistré est : {fristname.upper()} {lastname.title()} \n")
        break
classe=input(f"Saisir la classe de l'étudiant {fristname.upper()} {lastname.title()} \n")
print("------------------------------------------------------------------------------------------------------------------------")
print(f"L'étudiant(e) enregistré(e) est : {fristname.upper()} {lastname.title()} en {classe.upper()} \n")
print("------------------------------------------------------------------------------------------------------------------------\n")


while True:
    try:
        Nbmat=int (input(f"Saisir le nombre de matière(s) fait par l'étudiant(e) {fristname.upper()} {lastname.title()} \n"))
        print(" ")
        if(Nbmat<=0):
            print("Le nombre de matière doit être supérieur à zéro")
            continue
        else:
            break
    except ValueError:
        print(" Le nombre de matière saisi est invalide \n ")
        continue

Nbnom=Nbmat

for i in range(Nbmat):
    try:
        i+=1
        while Nbnom>0:
            Nmat=input(f"Ecrire le nom de la {i} matière \n")
            Nmat=int (Nmat)
            print("Le nom de la matière ne contient pas que des chiffres SVP !!! \n")
    except ValueError:
        Nbnom-=1
        ListeMat.extend([Nmat.upper()])
        continue
print(f"Voici la liste des Matières enregistrées : {ListeMat} \n")

  
Nbnote=Nbmat
for Nmat in ListeMat:
    while Nbnote>0:
        try:
            
            Notemat=int (input(f" Entrez la note de la matière  qui est {Nmat} \n"))
        except ValueError:
            print(f" La note de la matière {Nmat} est invalide ")
            continue
        if(Notemat<0):
            print(f"La note de la matière {Nmat} doit être supérieure à 0 ")
            continue
        elif(Notemat<=0 or Notemat<=20):
            
                Nbnote-=1
                ListeNote.extend([Notemat])
                break 
        else:
            print(f"La note de la matière {Nmat} doit être inférieure à 20")
            continue

print(f"Voici la liste des Notes enregistrées : {ListeNote} \n")

for Notemat in ListeNote:
    Som=sum(ListeNote)
print(f"La Somme totale des notes de l'étudiant {fristname} {lastname} vaut : {Som}\n ")


Moy=Som/Nbmat
print(f"La Moyenne de l'étudiant {fristname} {lastname} est : {Moy} \n")
if(Moy>=0 and Moy<10):
    print("Moyenne Insuffisante\n")
    print(f"---L'étudiant {fristname} {lastname} est Echoué(e). \u2639---\n ")
elif(Moy>=10 and Moy<12):
    print("Mention : Passable\n")
    print(f"---L'étudiant {fristname} {lastname} est Admis(e). \u2705---\n ")
elif(Moy>=12 and Moy<15):
    print("Mention : Assez-bien\n")
    print(f"---L'étudiant {fristname} {lastname} est Admis(e). \u2705---\n ")
elif (Moy>=15 and Moy<17):
    print("Mention : Bien\n")
    print(f"---L'étudiant {fristname} {lastname} est Admis(e). \u2705---\n ")
elif (Moy>=17 and Moy<19):
    print("Mention : Très-Bien\n")
    print(f"---L'étudiant {fristname} {lastname} est Admis(e). \u2705--- \n")
elif (Moy>=19 and Moy<=20):
    print("Mention : Excellente\n")
    print(f"---L'étudiant {fristname} {lastname} est Admis(e). \u2705--- \n")

    
print("-------------------------------------------------------------------------------------------------------------------")

print("Merci d'avoir Utilisé ce programme de Calcul de Moyenne d'un étudiant.")
print("A Très Bientôt !!!")

print("-------------------------------------------------------------------------------------------------------------------")
