# Compte-rendu de TP GLA
Le but de ce TP est d'obtenir une première approche du concept de test logiciel, plus précisément du concept de test unitaire.

De plus, nous verrons un paradigme de conception logicielle se basant sur le concept de test unitaire : TDD pour Test Driven Development.

# Exercie 1
Dans cette partie, nous avons réalisés un premier exemple des tests unitaires, fonctionnels et structurels.
## Coverage des tests unitaires
```
Name      Stmts   Miss  Cover   Missing
---------------------------------------
sort.py      14      0   100%
test.py      18      1    94%   34
---------------------------------------
TOTAL        32      1    97%
```

# Exercie 2
Dans cette partie, nous avons réalisés un code (la fonction main a été sciemment retiré pour des raisons de lisibilités) qui permet de réaliser un certain nombre d'opérations basiques.

De plus, nous avons réalisés les tests unitaires pour ce module en essayant de couvrir toutes les possibilités et tous le code.
## Coverage des tests unitaires
```
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
exo2.py           10      0   100%
test_exo2.py      29      1    97%   43
--------------------------------------------
TOTAL             39      1    97%
```

# Exercie 3
Dans cette partie, nous avons un avant-goût du concept de TDD.

L'approche pour réaliser cette partie est celle de [Robert C. Martin](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd). C'est cette approche que nous utiliserons pour écrire notre code.
## Coverage des tests unitaires
```
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
exercises.py     201      7    97%   8, 21, 64, 78, 140, 154, 474
--------------------------------------------
TOTAL            201      7    97%
```
