# groupe MIASHS 1
# Akram AMRAOUI
# Paul ROUILLIER
# Hajar ZAAZOUA 
# https://github.com/uvsq22106749/Projet-Taquin

import tkinter as tk
from random import choice


mat_init=[i for i in range(1,16)]

#case vide
mat_init.append(0)
mat=mat_init
historique=[]
def grille():
    global mat
    print(mat[0:4])
    print(mat[4:8])
    print(mat[8:12])
    print(mat[12:16])

def mouvement(nombre):
    print(nombre)
    global mat,historique
    espace= mat.index(0)
    nb = mat.index(nombre)
    #teste si 0 et le nombre sont sur la même ligne
    if espace//4 == nb//4:
        #test s'ils sont à coté
        if abs(espace-nb)==1:
            historique.append(nombre)
            mat[espace]=nombre
            mat[nb]=0
    #teste si 0 et le nombre sont sur la même colonne
    elif espace%4 == nb%4:
        #test s'ils sont à coté
        if abs(espace//4-nb//4)==1:
            historique.append(nombre)
            mat[espace]=nombre
            mat[nb]=0
def derniermouvement():
    global historique
    print(historique,historique[-1])
    if len(historique)>0:
        mouvement(historique[-1])
        #supprime de l'historique le dernier mouvement
        historique.pop()
        #et du mouvement qu'on vient d'effectuer
        historique.pop()
        dessingrille()
    print(historique)
def clic(event):
    global mat
    #indice dans la grille correspondant à l'endroit ou le clic a eu lieu
    indice=(event.x//100)+(event.y//100)*4
    print(mat[indice])
    mouvement(mat[indice])
    dessingrille()
def dessingrille():
    global taquin,mat
    for i in range(4):
        for j in range(4):
            #On calcule la taille du carré pour chaque tuile, c'est  dire les coordonnées
            A, B=(100*j, 100*i), (100*j+100, 100*i+100)
            #On calcule les coordonnées du point ou sera positionné le texte (au centre du carré)
            C= (100*j+50, 100*i+50)
            if mat[4*i+j]==0:
                taquin.create_rectangle(A, B, fill="white")
            else:
                taquin.create_rectangle(A, B, fill="yellow")
                taquin.create_text(C, text=mat[4*i+j], fill="blue",font=FONT)
a = str(input("Voulez-vous continuer la dernière partie? (O/N) "))
if a=="O":
    #on ouvre le fichier texte
    fichier = open("dernierepartie.txt", "r")
    #sur la premiere ligne est ecrite la matrice
    f =fichier.readlines()[0].split(",")
    fichier.close()
    mat = [int(i) for i in f]
else:
    #on mélange la matrice en reproduisant des mouvements aléatoires, un grand nombre de fois car certaines configurations ne sont pas resolvables
    for i in range(1,500):
        mouvement(choice([i for i in range(1,16)]))

FONT=('Ubuntu', 27, 'bold')
#on crée la fenetre
racine=tk.Tk()
#on lui donne un titre
racine.title("Jeu du Taquin")
#dans la fenetre on dessine le jeu (400x400, c'est plus simple pour les calculs car chaque carré fera 100x100)
taquin=tk.Canvas(racine, width=400, height=400, bg='white')
taquin.bind('<Button-1>', clic)
#on l'affiche
taquin.pack()
B = tk.Button(racine, text ="Dernier Mouvement", command=derniermouvement)
B.pack()
dessingrille()
#on affiche la fenetre
racine.mainloop()
#on sauvegarde la partie
fichier = open("dernierepartie.txt", "w")
fichier.write(','.join([str(i) for i in mat]))
fichier.close()
