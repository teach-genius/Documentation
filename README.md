# Documentation criteria_performance

---

# **criteria-performance**

`criteria-performance` est un package Python conçu pour calculer et visualiser les critères de performance des modèles de classification. Il fournit des outils pour générer et analyser des courbes ROC, PR, DET, ainsi que des métriques telles que le taux de faux positifs (FPR), le taux de vrais positifs (TPR) et l'Equal Error Rate (EER).

## **Installation**

Pour installer le package, utilisez la commande suivante :

```bash
pip install criteria-performance
```

## **Utilisation**

### **Initialisation avec un fichier CSV**

Le package permet de charger un fichier CSV contenant les résultats de classification. Ce fichier doit comporter au minimum deux colonnes : une pour les classes réelles et une autre pour les scores prédits.

```python
from criteria import PerformanceCriteria

# Initialisation avec un fichier CSV
pc = PerformanceCriteria("chemin_vers_votre_données.csv")
```

### **Initialisation avec un DataFrame Pandas**

Il est également possible d'initialiser la classe à partir d'un DataFrame Pandas.

```python
import pandas as pd
from criteria import PerformanceCriteria

# Créez un DataFrame avec les classes réelles et les scores prédits
data = {
    'class': [1, 1, 1, -1, -1],
    'score': [0.9, 0.1, 0.8, 0.3, 0.6]
}
df = pd.DataFrame(data)

# Initialisation avec un DataFrame Pandas
pc = PerformanceCriteria(df)
```

## **Fonctionnalités Principales**

### **Calcul des métriques de performance**

#### **ppv() et pnv()**

Ces méthodes retournent les valeurs prédictives positives (PPV) et négatives (PNV).

```python
ppv, pnv = pc.get_ppv(), pc.get_pnv()
```

#### **get_seuil()**

Génère une liste de seuils à partir des scores prédits.

```python
seuils = pc.get_seuil()
```

#### **get_fp() et get_tp()**

Retourne les faux positifs (FP) et les vrais positifs (TP) en fonction des seuils.

```python
fp, tp = pc.get_fp(), pc.get_tp()
```

#### **get_tfp() et get_ttp()**

Calcule les taux de faux positifs (TFP) et les taux de vrais positifs (TTP).

```python
tfp, ttp = pc.get_tfp(), pc.get_ttp()
```

#### **get_fnr() et get_fpr()**

Retourne les taux de faux négatifs (FNR) et de faux positifs (FPR).

```python
fnr, fpr = pc.get_fnr(), pc.get_fpr()
```

#### **getEER()**

Calcule et retourne l'Equal Error Rate (EER) et le seuil associé où FNR = FPR.

```python
eer_threshold, eer_value = pc.getEER()
```

### **Visualisation des résultats**

#### **Courbes ROC**

Affiche la courbe ROC (Receiver Operating Characteristic) :

```python
pc.dispROC(title="Courbe ROC", grid=True)
```

*Exemple de visualisation :*

![Exemple de Courbe ROC](https://raw.githubusercontent.com/teach-genius/Documentation/main/courbe_ROC.png)

#### **Courbes PR (Précision-Rappel)**

Affiche la courbe Précision-Rappel :

```python
pc.dispPR(title="Courbe Précision-Rappel", grid=True)
```

*Exemple de visualisation :*

![Exemple de Courbe PR](https://raw.githubusercontent.com/teach-genius/Documentation/main/courbe_P-R.png)

#### **Courbes DET**

Affiche la courbe DET (Detection Error Tradeoff) :

```python
pc.dispDET(title="Courbe DET", grid=True)
```

*Exemple de visualisation :*

![Exemple de Courbe DET](https://raw.githubusercontent.com/teach-genius/Documentation/main/courbe_DET.png)

```python
pc.dispOldDET(title="Courbe DET")
```

*Ou DET :*

![Exemple de Courbe DET](https://raw.githubusercontent.com/teach-genius/Documentation/main/courbe_hold-DET.png)

#### **Visualisation combinée**

Vous pouvez afficher plusieurs courbes ensemble et choisir de sauvegarder l'image :

```python
from criteria import PerformanceCriteria, Opentxt

data = Opentxt("Score_Sys_1.txt")

criter = PerformanceCriteria(data=data)
criter.displaygraphe(save=True, point=True, cp="red")
criter.show()
```

```python
pc.displaygraphe(taille=(15, 8), save=True, name="criteres_performance")
```

![Exemple de Courbe DET](https://raw.githubusercontent.com/teach-genius/Documentation/main/criteres_performance.png)

#### **Graphique interactif**

Ajoutez des curseurs interactifs sur le graphique pour naviguer à travers les points de données :

```python
pc.show()
```

### **Résumé des Performances**

La méthode `descriptionEER()` génère une description textuelle du seuil associé à l’EER, avec une interprétation contextuelle pour des applications comme la biométrie ou la détection de fraude.

```python
print(pc.descriptionEER())
```

## **Fonctions Utilitaires**

### **asarray2D(arrayA, arrayB)**

Cette fonction prend deux tableaux Numpy et les combine en un tableau 2D.

```python
from criteria import asarray2D

array_2D = asarray2D(arrayA, arrayB)
```

### **asDataFrame(array2D)**

Convertit un tableau 2D en DataFrame Pandas.

```python
from criteria import asDataFrame

df = asDataFrame(array_2D)
```

### **Opentxt(url)**

Cette fonction charge un fichier texte au format `.txt` et renvoie un DataFrame. Les données sont filtrées et organisées en deux groupes : les classes égales à `1` et celles différentes de `1`.

```python
from criteria import Opentxt

# Charger un fichier .txt et obtenir un DataFrame
df = Opentxt("chemin_vers_votre_fichier.txt")
```

**Code d'initialisation :**

```python
from criteria import PerformanceCriteria

# Initialisation avec le DataFrame précédent
pc = PerformanceCriteria(df)
```

---

## **Dépendances**
- `numpy`
- `pandas`
- `matplotlib`
- `mplcursors`

---

## **Exemple d'Utilisation**

Voici un exemple d'utilisation avec des données simulées :

```python
import numpy as np
import pandas as pd
from criteria import PerformanceCriteria

# Simuler des données
data = {
    'class': np.random.choice([1, -1], size=100),
    'score': np.random.random(100)
}
df = pd.DataFrame(data)

# Initialiser la classe avec le DataFrame
pc = PerformanceCriteria(df)

# Visualiser les courbes
pc.displaygraphe(taille=(10, 6), point=True)
```

---
