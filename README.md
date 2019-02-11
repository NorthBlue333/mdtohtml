# mdtohtml
`conversion.py` est un petit programme en python permettant la conversion de tous les fichiers .md (markdown) d'un répertoire (et de ses sous-dossiers) vers un autre répertoire (qui héritera des sous-dossiers).

Afin d'utiliser le programme, il faut ouvrir une invite de commande et exécuter le script python, avec les arguments suivants :
* `-i` ou `--input-directory` qui est **obligatoire** et qui permet de renseigner le répertoire contenant les fichiers .md
* `-o` ou `--output-directory` qui est **obligatoire** et qui permet de renseigner le répertoire qui contiendra les fichiers .htmlfile (si le dossier existe déjà il sera supprimé !)


**ATTENTION**


Veillez à ne pas oublier les guillemets autour du chemin d'accès s'il contient des caractères spéciaux.


* `-k` ou `--kikoo-lol` qui est **optionnel** et qui permet d'ajouter des kikoo lol (ne prend pas de paramètres)
* `-a` ou `--achtung` qui est **optionnel** et qui permet de transformer des lettres pour la compréhension allemande (ne prend pas de paramètres)


Support des balises :
* h1, h2, h3, h4, h5, h6
* lists
* em, strong
* img, url
