# -*- coding: utf-8 -*-
"""
Partie 3 : MAIN (Tkinter)

11/2023

Data products Amazon : https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products/code 

Part 3: Graphical interface under Tkinter
Goal: Search for products corresponding to the user's selection choices
This interface must include the following elements:
- Possibility for the user to enter the different criteria
- Display results

Packages
"""
import tkinter as tk
from tkinter import ttk,font
from part_3_functions import rechercher # derniere fonction de notre module

### Root
root=tk.Tk()

root.title('Amazon Smart Research')
root.configure(bg='white') # couleur background
root.geometry("1315x530") # taille de la fenêtre

# centrage de la fenetre
largeur_ecran =root.winfo_screenwidth()
hauteur_ecran= root.winfo_screenheight()
x= int((largeur_ecran/2)-(1315/2))
y= int((hauteur_ecran/2)-(530/2))

# position de la fenetre
root.geometry("+{}+{}".format(x, y-30)) # -30 pour mieux centrer


### Variables associées aux inputs
var_nom_prod=tk.StringVar()
var_nom_cat=tk.StringVar()
var_tri=tk.StringVar()
var_ordre_tri=tk.StringVar()
var_prix_max=tk.StringVar()
var_prix_min=tk.StringVar()
var_note_min=tk.StringVar()
var_note_max=tk.StringVar()
var_ventes_min=tk.StringVar()
var_ventes_max=tk.StringVar()
var_best_seller=tk.BooleanVar()


### FRAME 1 d'affichage des resultats.
texte="Produits trouvés\nNaviguez sur amazon.com en cliquant sur les URLs"
frame1=ttk.LabelFrame(root, text=texte, padding="10")
frame1.grid(row=1,column=0,padx=10,pady=10)
frame1.grid_columnconfigure(0, weight=1)


### FRAME 0 qui contient les choix / options de l'utilisateurs
frame0=ttk.Frame(root)
frame0.grid(row=0,column=0)

## WIDGETS DU FRAME 0

# style des widgets
style = ttk.Style()
# couleur background labels
style.configure("TLabel", background="#232f3e", foreground="#ff9900")
# couleur background boutons
style.configure("TButton", background="#232f3e", foreground="#232f3e")


# ROW 0 : Texte
bold_font = font.Font(weight='bold') # police avec gras
label_texte = ttk.Label(frame0, text="                Amazon Smart Research\nRecherchez un produit & Cliquez sur un URL",font=bold_font)
label_texte.grid(row=0, column=2,columnspan=2,pady=(0,20))

# ROW 1 : Produit & Prix Min & Prix Max
# produit
ttk.Label(frame0,text="Produits (séparation: point-virgule)").grid(row=1,column=0)
ttk.Entry(frame0, textvariable=var_nom_prod, width=44).grid(row=1,column=1)
# prix min
ttk.Label(frame0, text="Prix Min").grid(row=1, column=2)
ttk.Entry(frame0, textvariable=var_prix_min, width=51).grid(row=1, column=3)
# prix max
ttk.Label(frame0, text="Prix Max").grid(row=1, column=4)
ttk.Entry(frame0, textvariable=var_prix_max, width=54).grid(row=1, column=5)

# ROW 2 : Categorie & Note Min & Note Max
# categorie
ttk.Label(frame0,text="Catégories (séparation: point-virgule)").grid(row=2,column=0)
ttk.Entry(frame0, textvariable=var_nom_cat, width=44).grid(row=2,column=1)
# note min
ttk.Label(frame0, text="Note Min").grid(row=2, column=2)
ttk.Entry(frame0, textvariable=var_note_min, width=51).grid(row=2, column=3)
# note max
ttk.Label(frame0, text="Note Max").grid(row=2, column=4)
ttk.Entry(frame0, textvariable=var_note_max, width=54).grid(row=2, column=5)

# ROW 3 : Tri & Ventes min & Ventes max
# tri
ttk.Label(frame0,text="Tri").grid(row=3,column=0)
ttk.Combobox(frame0, textvariable=var_tri,values=['Notes','Prix','Reviews','Ventes'], width=44).grid(row=3, column=1)
# ventes min
ttk.Label(frame0, text="Ventes Min").grid(row=3, column=2)
ttk.Entry(frame0, textvariable=var_ventes_min, width=51).grid(row=3, column=3)
# ventes max
ttk.Label(frame0, text="Ventes Max").grid(row=3, column=4)
ttk.Entry(frame0, textvariable=var_ventes_max, width=54).grid(row=3, column=5)

# ROW 4 : Ordre de tri & Best Seller
# ordre de tri
ttk.Label(frame0,text="Ordre de tri").grid(row=4,column=0)
ttk.Combobox(frame0, textvariable=var_ordre_tri,values=['Croissant','Décroissant'], width=44).grid(row=4, column=1)
# best seller
ttk.Label(frame0, text="Best Seller").grid(row=4, column=2)
ttk.Checkbutton(frame0, variable=var_best_seller).grid(row=4, column=3)

# ROW 5 : Bouton de recherche qui active la fonction recherche()
ttk.Button(frame0, text="Rechercher", command=lambda: rechercher(frame1,var_nom_prod,var_nom_cat,var_tri,var_ordre_tri,var_prix_min,var_prix_max,var_note_min,var_note_max,var_ventes_min,var_ventes_max,var_best_seller)).grid(row=5,column=2,columnspan=2,pady=18)



root.mainloop() # boucle pour reaction aux evenements 