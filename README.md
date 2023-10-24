# API_IPA

API pour simuler la gestion des becs de pression d'un bar

datas :
nombre de bec -> caractéristques des becs 
    - faire des recherhce sur le fonctionement précis
    - id
    - marque
    - CO2 ou compresseur
    - débit du robinnet (L/H)
    - temps mise en marche (min)
    - dimension (L/P/H)
    - poids (kg)
    - pression (bar)
type de bières : -> caractéristques des bières (coté produit et coté stockage)
  - coté produit :
    - id
    - type de bières (IPA, Blonde, Brune, Sour, Stout, Rousse)
    - taux d'alcool
    - ingrédients
    - description sommaire
    - nom de la brasserie
    - prix a la pinte
    - prix au demi (....)
    - IBU
    - id bec utilisé
  - coté stockage :
    - id
    - nombre de fût
    - taille de fût
    - prix du fût
    - pression nécessaire pour utilisation
    - température (°C)
  - liste ingrédient :
    - id
    - nom
    - description
    - origine (optionnel)
  - brasserie :
    - id
    - nom
    - origine (pays, région)
    - description
  - type de bières:
      - id
      - nom
      - description/ caractéristiques
