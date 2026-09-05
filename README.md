# PCE – PRONTO

Ce dépôt regroupe les travaux des projets **PRONTO** (1A) et **PCE** (2A), portant tous deux sur la simulation et la caractérisation de systèmes acoustiques/mécaniques (haut-parleurs à pavillon, pistons/cylindres).

## Structure

```
.
├── pronto/                  # Projet PRONTO (1A)
│   ├── 2_cylindres/         # Données et script de traitement — configuration à 2 cylindres
│   ├── 4_cylindres/         # Données et script de traitement — configuration à 4 cylindres
│   ├── comparaison/         # Données et script de comparaison entre configurations
│   ├── li/                  # Données et script de traitement — cas "LI"
│   └── Pronto_suivi_projet-3.pdf   # Suivi de projet
│
└── pce/                     # Projet PCE (2A)
    ├── cad/                 # Fichiers CAO (STEP) des pavillons HX150 / HX200
    ├── coax/                # Paramètres du driver coaxial + CAO de l'enceinte
    ├── essai_comsol/        # Paramètres d'essai COMSOL (haut-parleur à charge)
    ├── results/             # Résultats SPL (niveaux de pression acoustique) exportés
    ├── 6HX150_parameters.txt
    └── volumes.txt
```

## Remarques

- Les fichiers de simulation COMSOL (`.mph`, souvent > 100 Mo, jusqu'à ~1 Go) ont été **volontairement exclus** de ce dépôt : ils dépassent la limite de taille de fichier de GitHub et ne sont pas adaptés au versioning Git. Ils restent disponibles en local.
- Deux documents personnels sans rapport avec le contenu technique ont également été exclus.
- Les scripts Python (`Traitement_*.py`) traitent les fichiers `.txt` de données situés dans leur propre dossier.

## Prérequis pour les scripts Python

Les scripts de `pronto/` lisent des fichiers de données texte au format tabulaire — vérifier les chemins relatifs en tête de script avant exécution.
