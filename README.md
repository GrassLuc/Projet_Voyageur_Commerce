# Projet_Arbre_Courant
Une solution approchée consiste à faire une heuristique calculant d’abord un arbre couvrant de poids minimal passant par les villes (A_1, … A_n), et offrir comme solution de visite un parcours en profondeur d’abord de l’arbre.

## TP 1-4
## Projet
### Preparation
- On fait ce projet par binôme. Donc pour partager les ficher et noter les modifications, on remplace JupyterLab par Atom Avec Atom on peut modifier le code à même temps et soumettre les codes sur Github. Dans les branches on peut rester les versions différences.

### Installer
#### Atom
- On peut installer Atom sur : https://atom.io/
- Elle est un éditeur multiplateforme. Atom fonctionne sur tous les systèmes d'exploitation. Utilisez-le sur OS X, Windows ou Linux.
#### Python
- En raison d'on a déjà eu l'environnement de Anaconda pour JupyterLab, on n'a pas besoin de reinstaller Python. Sinon on peut installer sur : https://www.python.org/ . Et sur Mac on doit installer python par Homebrew et utilisez - brew install python3
- Après on doit vérifier dans cmd si on a bien installé Python et pip par command:
  - python (si il affiche la version de python ctd bien installé, sinon resseyez python3 ou reinstallez )
  - ^Z (Sortie de mode python)
  - pip (pip est une source important, on a besoin après et normalement il installe avec python automatiquement)
  - python -m pip install python-language-server[all](pour installer un chose necessaire)
#### Packages
- Dans Atom on doit installer certains Packages.
  - language-python(normalment deja existe)
  - teletype(Pour modifer à même temps)
  - atom-ide-ui
  - ide-python
  - atom-python-run(pour fonctionner le code par F5, sur mac il faut change vers python3 dans setting de package)
#### Bibliothèque
- Sous cmd et il faut utiliser pip
- Numpy; Scipy; Matplotlib
  - python -m pip install numpy scipy matplotlib
- linfitxy
  - python -m pip install python-usbtmc tpp7
- Python Graph Libraries(i dont know which one is better so i install python-igraph, NetworkX, EasyGraph from : https://wiki.python.org/moin/PythonGraphLibraries. i prefer NetworkX)
  - python -m pip install python-igraph NetworkX Python-EasyGraph
