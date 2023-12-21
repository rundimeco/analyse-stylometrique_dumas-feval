# Expérience sur le corpus Dumas-Féval

Ce projet s'inscrivait dans le cadre du mémoire de M2 d'Anaëlle Baledent, 

NB: Le dossier data contient le corpus déjà taggé

## Prérequis
Pour l'étiquetage du Corpus:
* [Java](https://www.java.com/fr/download/) -
* [Stanford tagger](https://nlp.stanford.edu/software/tagger.shtml) - Étiqueteur morphosyntaxique

POur le reste :
* [Python3](https://www.python.org/downloads/) - 
* [NLTK](http://www.nltk.org/) - 
* [Numpy](http://www.numpy.org/) - 
* [Scikit-Learn](https://scikit-learn.org/) - Classification non-supervisée
* [Scipy](https://www.scipy.org/) - Dendrogramme
* [Mathplotlib](https://matplotlib.org/) - Affichage des graphiques



## POur reproduire simplement le clustering
```python3 01_extract_pattern.py```

```python3 02_get_frequences.py patterns/patt_dumas_feval_min=4_max=5.json```

```python3 06_tests_clustering.py patterns/patt_dumas_feval_min=4_max=5.json_freq.json```

## Préparation du corpus

Chapitres :
```for i in corpus/*/* ; do python cut_chapter.py $i ; done```

### Format des données

Le corpus doit être au format brut `.txt`.


### Stanford
settings.json doit contenir :
base 	: le répertoire du stanford tagger
jarname: le nom du fichier jar 
On peut s'inspirer de settings.json.example


```python Stanford_Corpus.py expe_Dumas_feval/corpus2/Dumas/acte_chapter1.txt```

```for i in expe_Dumas_feval/corpus2/*/* ; do python Stanford_Corpus.py $i ; done```

À titre indicatif, le temps d'éxécution est le suivant :

| # lignes  | Temps d'exécution |
| --------- | ----------------- |
| 10  | 0m12.364s  |
| 100  | 1m13.538s  |
| 1000 | 12m53.592s |


## Extraction des séquences syntaxiques
```python3 01_extract_pattern.py```
```python3 02_get_frequences.py patterns/patt_dumas_feval_min\=4_max\=5.json```


Pour obtenir les fréquences, il faut lancer cette ligne :

### Loi de Zipf

### Séquences discriminantes
```python3 03_get_GR.py ```
```python3 04_patt_to_corpus.py res_minsupp\=200 retour_au_texte_min\=4_max\=5.json```

### Exemples

## Classification non supervisée
```python3 06_tests_clustering.py patterns/patt_dumas_feval_min\=4_max\=5.json_freq.json```

### Dendrogramme

```pythonw 07_tests_dendogram.py patterns/patt_dumas_feval_min\=4_max\=5.json_freq.json```

##Travail sur les cChapitres

```python 01_extract_pattern.py```
```python 02_get_frequences.py patterns/patt_dumas_les-trois-mousquetaires_min\=4_max\=5.json```
```python3 06_tests_clustering.py patterns/patt_dumas_les-trois-mousquetaires_min\=4_max\=5.json_freq.json```
```b```

## Authors 

* **Anaëlle BALEDENT** - [AnaelleBaledent](https://github.com/AnaelleBaledent)
* **Gaël LEJEUNE** - [rundimeco](https://github.com/rundimeco)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used

# analyse-stylometrique_dumas-feval
