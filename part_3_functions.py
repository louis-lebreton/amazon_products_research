
"""
Partie 3 : FUNCTIONS

11/2023

Data products Amazon : https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products/code 

Part 3: Graphical interface under Tkinter
Goal: Search for products corresponding to the user's selection choices
This interface must include the following elements:
- Possibility for the user to enter the different criteria
- Display results

Packages
"""
import pandas as pd
import tkinter as tk
from tkinter import ttk
import webbrowser # pour ouvrir des liens URL
from deep_translator import GoogleTranslator # module pour réaliser des traductions


###### Fonction qui recherche un produits dans le data frame
###### selon les options choisies par l'utilisateur

def recherche_prod(df,nom_prod,nom_cat,prix_min,prix_max,note_min,note_max,ventes_min,ventes_max,best_seller,tri='prix',ordre_tri="Croissant"): 
    """
    Fonction de filtrage qui renvoie un data fame filtré selon les choix de l'utilisateur
    """
    
    # tri = prix ou notes ou nb_avis
    
    # trouver produit et categorie
    # transformation en liste
    liste_prod = nom_prod.split(';') 
    liste_categories = nom_cat.split(';')
    
    # traduction des éléments des deux listes en anglais
    # objet traducteur de fr à eng
    translator = GoogleTranslator(source='fr', target='en')
    
    df_select= pd.DataFrame() # data frame final vide
    # boucle sur les noms de produit et catégories pour avoir l'ensemble de la sélection de l'utilisateur (produit cartesien)
    for nom_cat in liste_categories :
        nom_cat=translator.translate(nom_cat) # traduction du nom de categorie
        for nom_prod in liste_prod :
            nom_prod=translator.translate(nom_prod) # traduction du nom de produit
            df_ajout =df[df['title'].str.contains(nom_prod,case=False)& df['category_name'].str.contains(nom_cat,case=False)]
            # case=False pour omettre les majuscules
            df_select =pd.concat([df_select, df_ajout]) # ajout des df_ajout au df_final
    # suppression des doublons
    df_select=df_select.drop_duplicates()
    
    # prix min et max
    if prix_min!='':
        df_select = df_select[df_select['price']>=float(prix_min)]
    if prix_max!='':
        df_select = df_select[df_select['price']<=float(prix_max)]

    # note min et max
    if note_min!='':
        df_select = df_select[df_select['stars']>=float(note_min)]
    if note_max!='':
        df_select=df_select[df_select['stars']<=float(note_max)]

    # ventes min et max
    if ventes_min!='':
        df_select = df_select[df_select['boughtInLastMonth']>=float(ventes_min)]
    if ventes_max!='':
        df_select = df_select[df_select['boughtInLastMonth']<=float(ventes_max)]
    # best seller
    if best_seller:
        df_select = df_select[df_select['isBestSeller']==True]
    # tri
    if tri=='Reviews':
        tri='reviews'
    elif tri=='Notes':
        tri='stars'
    elif tri=='Ventes':
        tri='boughtInLastMonth'
    else:
        tri='price'
        
    # ordre de tri
    if ordre_tri=="Décroissant":
        df_select = df_select.sort_values(by=tri,ascending=False)
    else:
        df_select = df_select.sort_values(by=tri)
    
    
    return df_select.reset_index() # pour remettre les index dans le bon sens
    

###### Fonction d'affichage du dataframe dans un frame

def affichage_df(df,frame1):
    """
    Fonction d'affichage d'un dataframe dans une frame Tkinter
    """
    # style des noms de colonnes
    # Code couleur d'Amazon : https://www.color-hex.com/color-palette/26593
    style = ttk.Style()
    style.configure("Treeview.Heading",foreground="#232f3e", font=('Microsoft Sans Serif',9,'bold'))
    
    # tableau qui affiche le dataframe
    tab=ttk.Treeview(frame1,columns=list(df.columns)) # dans le frame 1
    # style des noms de lignes (2 à 2) : gris pour ligne paire, blanc pour ligne impaire
    tab.tag_configure("ligne_paire",background="lightgray",font=('Microsoft Sans Serif', 8))
    tab.tag_configure("ligne_impaire",background="white",font=('Microsoft Sans Serif', 8))
    
    tab.grid(row=1,column=0,sticky=(tk.W, tk.E, tk.N,tk.S))
    
    # fonction pour ouvrir les URLs des liens et images des produits
    def click_URL(event): # event = evenement de click
        item = tab.identify('item', event.x, event.y) # ligne sur laquelle on a cliqué
        col = tab.identify('column', event.x, event.y) # colonne sur laquelle on a cliqué
        
        if col in ['#4','#5']: # colonnes ayant un URL
            url = tab.item(item,'values')[int(col[1:]) - 1]  # extraction de la valeur de la ligne
            webbrowser.open(url) # ouverture de l'url
            
    # liaison de l'evenement de click à la fonction click_URL
    tab.bind('<Button-1>', click_URL)
    
    
    # COLONNES
    for c in df.columns:
        tab.heading(c,text=c) # affichage des titres des colonnes
        tab.column(c,stretch=tk.NO,width=95,anchor="center") # centrage du texte des celulles + étirage des colonnes en fct du nom de la col
    tab.column("#0", width=0, stretch=tk.NO)  # cache la 1ere colonne vide
        
    # LIGNES
    for i,row in df.iterrows():
        tag="ligne_paire" if i%2==0 else "ligne_impaire"
        
        tab.insert("","end",values=list(row),tags=(tag,)) # ajout du tag pair/impair
        
        
###### Fonction executée lorsque l'utilisatuer appuie sur 'Rechercher'


def rechercher(frame1,var_nom_prod,var_nom_cat,var_tri,var_ordre_tri,var_prix_min,var_prix_max,var_note_min,var_note_max,var_ventes_min,var_ventes_max,var_best_seller):
   """
   Fonction executée lorsque l'utilisatuer appuie sur 'Rechercher'.
   Execute la fonction "affichage" en prenant en compte les options de l'utilisateur
   Cette fonction fait la liaison entre les choix entrés sur l'interface (inputs) et le filtrage de nos données (variables)
   """
    
    # récupération des inputs de l'utilisteur issues des Widgets
   nom_prod = var_nom_prod.get()
   nom_cat = var_nom_cat.get()
   tri = var_tri.get()
   ordre_tri = var_ordre_tri.get()
   prix_min=var_prix_min.get()
   prix_max=var_prix_max.get()
   note_min=var_note_min.get()
   note_max=var_note_max.get()
   ventes_min=var_ventes_min.get()
   ventes_max=var_ventes_max.get()
   best_seller=var_best_seller.get()
    
   ## Importation des données 
   df=pd.read_csv('../Data/out/amazon_data.csv')
    
   # execution de la fonction recherche_prod()
   df_select = recherche_prod(df,nom_prod,nom_cat,prix_min,prix_max,note_min,note_max,ventes_min,ventes_max,best_seller,tri,ordre_tri)
   affichage_df(df_select,frame1) # reutilisation de la fct affichage




