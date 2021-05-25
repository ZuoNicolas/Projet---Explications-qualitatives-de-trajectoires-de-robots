# LIRE LE RAPPORT FINAL ! 
 
# Projet - Explications-qualitatives-de-trajectoires-de-robots
http://androide.lip6.fr/?q=node/622

### Etapes importantes de dev


1/ Générateur de scènes:

il s'agira de scènes 2D, générées à partir d'images. Vous pourrez commencer avec des objets constitués de formes simples (legos ou cartons de couleurs différentes). Les objets sont décrits selon plusieurs critères (au minimum deux, par exemple on peut facilement calculer la surface d'un objet, son contour et donc son périmètre (nombre de pixels du contour) et un indice de compacité; ou encore la couleur, qui pourront traduire des caractéristiques comme la fragilité ou la température des objets, dans le monde réel). A partir de ces images et en utilisant des outils comme scikit-images, vous devez pouvoir identifier les objets par combinaison des critères.
En sortie, une grille, avec les objets identifiés à leurs différentes positions.

Le format dépendra vraisemblablement des outils logiciels choisis (image, grille d'occupation, scène 2D compatible avec Tiled...)

 

2/ Langage de description de trajectoires:

On définit un langage de description des trajectoires dans le monde envisagé, à l'aide de descripteurs qualitatifs. On peut envisager les éléments descriptifs suivants :

* positionnement distanciel "[très loin, loin, proche, très proche] du carré vert"

* positionnement relatif par rapport à deux objets: "passer entre l'objet vert et l'objet jaune"

* positionnement relatif distance par rapport à deux: "passer plus près de l'objet rond que de l'objet carré"
* aspects séquentiel: "passer proche de l'objet A avant de passer très proche de l'obet B"

 

Produire une description sur la base d'une trajectoire pose déjà des problèmes complexes: comment choisir les descriptions les plus pertinentes en particulier?

Et dans le sens inverse: est-on capable sur la base de la description de reproduire une trajectoire ou un ensemble de trajectoires?


3/ Générateur de trajectoires:

Une trajectoire est un parcours entre un objet A et un objet B.

* Savoir générer le plus court chemin pour aller de A à B, passant éventuellement par un point C (revient à calculer deux trajectoires, de A à C et de C à B).

* Savoir générer une ou plusieurs trajectoires satisfiant une description linguistique.

 

 

4/ Langage de justification comparative:
On définit ici des objectifs de l'utilisateur.
On pourrait ici définir des degrés de satisfaction des critères, et les combiner pour pouvoir comparer deux trajectoires et dire laquelle est la meilleure au sens des critères définis.
 

### Cahier des charges

On donne ici des indications sur les versions envisagées pour les différentes versions [v0,v1...]
On souhaite au final la production d'un logiciel doté d'une interface permettant de:

 

* [v0] Charger une scène appartenant à une base existante, ou chargement d'une nouvelle image

* [v0] Entrer une trajectoire: par exemple, à la souris directement sur l'image, ou via un format donnant une séquence de positions

* [v0] éditer les descripteurs linguistiques (par exemple à quel seuil est-on très proche) 
 

* [v0] Desciption linguistique d'une trajectoire existante

* [v1] Génération d'un ensemble de trajectoires sur la base d'une description

 

* [v2] Sélection selon les objectifs de l'utilisateur: le logiciel choisit parmi des trajectoires (spécifiées par l'utilisateur, ou générées par le logiciel)
* [v3] Justification: après la sélection d'une trajectoire T, l'utilisateur peut sélectionner un autre T' dans l'ensemble de trajectoires, et le logiciel justifie pourquoi T a été préféré à T'  
