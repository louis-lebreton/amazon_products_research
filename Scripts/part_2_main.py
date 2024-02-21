#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAIN
Part 2 : Content search

11/2023

Data products Amazon : https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products/code 

Goal : Search for products corresponding to the user's selection choices
We therefore filter the data frame of Amazon US products.

Packages
"""
import pandas as pd
import part_2_functions as p2f

######## Import du data frame
df=pd.read_csv('../Data/out/amazon_data.csv')

######## Partie 2 - Exercice 1

### inputs de l'utilisateur 

# Choix de l'utilisateur    
Categorie=input("Quelle catégorie souhaitez-vous ? : ")
Nom=input("Quel est le nom de l'article souhaité ? : ")
Critere=input("Quel types de filtres voulez-vous : Notes/Avis/Prix ? : ")


# affichage du data frame filtré
print(p2f.recherche_1(df,Categorie,Nom,Critere))

######## Partie 2 - Exercice 2

# Choix de l'utilisateur
Categorie=input("Entrez la catégorie souhaitée : ")
NoteMin=float(input("Entrez la note minimale souhaitée : "))
UniteVend=int(input("Entrez le nombre minimale d'unités vendues : "))
Type=input("Quel type de filtre voulez vous : Prix/Notes ? : ")

# affichage du data frame filtré
print(p2f.recherche_2(df,Categorie,NoteMin,UniteVend,Type))


######## Partie 2 - Exercice 3

# inputs de l'utilisateur 
Noms=input("Noms des produits séparés par des point-virgules : ")
liste_prod = Noms.split(';') # transformation en liste

Categories = input("Noms des categories séparés par des point-virgules : ")
liste_categories = Categories.split(';') # transformation en liste

budget=float(input("Quel est votre budget maximal ? :"))
note=float(input("Quelle note moyenne souhaitez-vous au minima ? : "))

# affichage du data frame filtré
print(p2f.recherche_3_liste(df,liste_prod,liste_categories,budget,note))