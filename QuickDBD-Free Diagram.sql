-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/e9FHzD
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "BecDePression" (
    "becDePressionID" int   NOT NULL,
    "marque" varchar(50)   NOT NULL,
    "CO2" bool   NOT NULL,
    "debitRobinnet" int   NOT NULL,
    "tempsMiseEnMarche" int   NOT NULL,
    "largeur" int   NOT NULL,
    "profondeur" int   NOT NULL,
    "hauteur" int   NOT NULL,
    "pression" int   NOT NULL,
    CONSTRAINT "pk_BecDePression" PRIMARY KEY (
        "becDePressionID"
     )
);

CREATE TABLE "Biere" (
    "biereID" int   NOT NULL,
    "typeBiere" int   NOT NULL,
    "brasserie" int   NOT NULL,
    "becUtilise" int   NOT NULL,
    "fournisseur" int   NOT NULL,
    "tauxAlcool" int   NOT NULL,
    "description" string   NOT NULL,
    "prixPinte" int   NOT NULL,
    "prixDemi" int   NOT NULL,
    "ibu" int   NOT NULL,
    CONSTRAINT "pk_Biere" PRIMARY KEY (
        "biereID"
     )
);

CREATE TABLE "Stockage" (
    "strockageID" int   NOT NULL,
    "idBiere" int   NOT NULL,
    "nbFut" int   NOT NULL,
    "prixFut" int   NOT NULL,
    "pressionUtilisation" int   NOT NULL,
    "tempratureUtilisation" int   NOT NULL,
    CONSTRAINT "pk_Stockage" PRIMARY KEY (
        "strockageID"
     )
);

CREATE TABLE "Ingredient" (
    "ingredientID" int   NOT NULL,
    "contenuDansBiere" int   NOT NULL,
    "nom" varcahr(50)   NOT NULL,
    "description" string   NOT NULL,
    "origine" varchar(20)   NOT NULL,
    CONSTRAINT "pk_Ingredient" PRIMARY KEY (
        "ingredientID"
     )
);

CREATE TABLE "Brasserie" (
    "brasserieID" int   NOT NULL,
    "nom" varchar(50)   NOT NULL,
    "originePays" varchar(20)   NOT NULL,
    "origineRegion" varchar(50)   NOT NULL,
    "description" string   NOT NULL,
    CONSTRAINT "pk_Brasserie" PRIMARY KEY (
        "brasserieID"
     )
);

CREATE TABLE "TypeDeBiere" (
    "typeDeBiereID" int   NOT NULL,
    "nom" varchar(20)   NOT NULL,
    "description" string   NOT NULL,
    CONSTRAINT "pk_TypeDeBiere" PRIMARY KEY (
        "typeDeBiereID"
     )
);

CREATE TABLE "Fournisseur" (
    "fournisseurID" int   NOT NULL,
    "nom" varchar(30)   NOT NULL,
    "adresse" varchar(200)   NOT NULL,
    "pays" varchar(30)   NOT NULL,
    "codePostak" varChar(10)   NOT NULL,
    "numTelephone" varchar(10)   NOT NULL,
    CONSTRAINT "pk_Fournisseur" PRIMARY KEY (
        "fournisseurID"
     )
);

ALTER TABLE "Biere" ADD CONSTRAINT "fk_Biere_typeBiere" FOREIGN KEY("typeBiere")
REFERENCES "TypeDeBiere" ("typeDeBiereID");

ALTER TABLE "Biere" ADD CONSTRAINT "fk_Biere_brasserie" FOREIGN KEY("brasserie")
REFERENCES "Brasserie" ("brasserieID");

ALTER TABLE "Biere" ADD CONSTRAINT "fk_Biere_becUtilise" FOREIGN KEY("becUtilise")
REFERENCES "BecDePression" ("becDePressionID");

ALTER TABLE "Biere" ADD CONSTRAINT "fk_Biere_fournisseur" FOREIGN KEY("fournisseur")
REFERENCES "Fournisseur" ("fournisseurID");

ALTER TABLE "Stockage" ADD CONSTRAINT "fk_Stockage_idBiere" FOREIGN KEY("idBiere")
REFERENCES "Biere" ("biereID");

ALTER TABLE "Ingredient" ADD CONSTRAINT "fk_Ingredient_contenuDansBiere" FOREIGN KEY("contenuDansBiere")
REFERENCES "Biere" ("biereID");

