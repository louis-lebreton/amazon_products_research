# -*- coding: utf-8 -*-

"""
FUNCTIONS
Part 2 : Content search

11/2023

Data products Amazon : https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products/code 

Goal : Search for products corresponding to the user's selection choices
We therefore filter the data frame of Amazon US products.

Packages
"""
import pandas as pd


# Partie 2 - Fonction 1

def recherche_1(df,Categorie,Nom,Critere):
    
    """
    Cette fonction permet à l'utilisateur de rentrer un nom de catégorie, de 
    produit et le type de recherche souhaitée. Elle lui affiche les résultats 
    correspondants à sa demande. 
    Input :
        ---Catégorie : str
        ---Nom : str
        ---Critère : str
        """
    
    #Nouveau DataFrame récoltant les inputs
    resultats_prod=df.loc[(df['category_name']==Categorie) & (df['title'].str.contains(Nom))]
    #Affichage du résultat en fonction du critère choisi par l'utilisateur
    if Critere=='Notes':
       # Tri en fonction des notes des produits 
       A=resultats_prod.sort_values(by='stars', ascending=False)
       return A.head(20)
    elif Critere=='Avis':
       # Tri en fonction des avis
       B=resultats_prod.sort_values(by='reviews', ascending=False)
       return B.head(20)
    elif Critere=='Prix':
       # Tri en fonction des prix
       C=resultats_prod.sort_values(by='price', ascending=False)
       return C.head(20)
          
   
# Partie 2 - Fonction 2

def recherche_2(df,Categorie,NoteMin,UniteVend,Type):
    
    """
    Cette fonction permet à l'utilisateur de rentrer un nom de catégorie, une note
    minimale, un nombre d'unités vendues minimales ainsi que le type de recherche
    souhaitée. Elle lui affiche les résultats correspondants à sa demande. 
    Input :
        ---Catégorie : str
        ---NoteMin : float
        ---UniteVend : int
        ---Critère : str
        """
        
    # Nouveau DataFrame récoltant les inputs
    resultats=df.loc[(df['category_name']==Categorie) & (df['stars']>=NoteMin) & (df['boughtInLastMonth']>=UniteVend)]
    # Affichage des résultats en fonction du critère choisi par l'utilisateur
    if Type=='Prix':
        # Tri en fonction des prix
        A=resultats.sort_values('price',ascending=False)
        return A.head(20)
    elif Type=='Notes':
        # Tri en fonction des notes
        B=resultats.sort_values('stars',ascending=False)
        return B.head(20)


# Partie 2 - Fonction 3

def recherche_3_unitaire(df,nom_prod,nom_cat,budget,note):
    
    """
    Fonction de filtrage selon un nom de produit, un nom de catégorie, un prix et une note
    """
    
    resultats = df.loc[df['category_name'].str.contains(nom_cat,case=False) & df['title'].str.contains(nom_prod,case=False) &
                       (df['price'] <= budget) & (df['stars'] >= note)]
    # case = False pour omettre les majuscules
    return resultats


# Partie 2 - Fonction 4

def recherche_3_liste(df,liste_prod,liste_categories,budget,note):
    
    """
    Fonction de filtrage.
    Renvoie un data frame selon les options de l'utilisateur : liste_prod, liste_categories, budget, note
    Pour rechercher plusieurs produits dans plusieurs catégories : 
    On utilise une boucle qui permet de rechercher chaque produit pour chaque catégorie
    On concatene donc chaque recherche sur 1 produit et 1 catégories issus des deux listes :
    liste_prod et liste_categories
    Triage final sur les variables 'isBestSeller','stars','reviews' par ordre décroissant.
    """
    
    df_final= pd.DataFrame() # data frame final vide
    
    for nom_cat in liste_categories :
        for nom_prod in liste_prod :
            df_ajout =recherche_3_unitaire(df,nom_prod,nom_cat,budget,note) # fonction de recherche unitaire réutilisée
            df_final =pd.concat([df_final, df_ajout]) # ajout des df_ajout au df_final
    
    # on place les best sellers en haut s'ils existent, notes en ordre decroissant, reviews en ordre decroisant
    df_final = df_final.sort_values(by=['isBestSeller','stars','reviews'],ascending=[False,False,False])
    # suppression des doublons
    df_final=df_final.drop_duplicates()
    
    return df_final
