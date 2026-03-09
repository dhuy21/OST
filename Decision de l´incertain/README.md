# TP OST – Décision dans l'incertain & Sécurité

Travaux pratiques sur les **algorithmes de bandit** (Multi-Armed Bandits) dans le cadre du cours **Ouvrage Sciences Technique (OST)** – Décision dans l'incertain & Sécurité (INSA CVL).

## Contenu

- Implémentation d’algorithmes de bandit stochastique : stratégie aléatoire, ε-greedy, ε-greedy décroissant, **UCB**.
- Environnement de bandit et mesure de performance (récompense cumulée, regret).
- Questions / parties du TP : comparaison d’algorithmes, visualisations (récompense cumulée, temps).

## Structure du projet

```
OST/
├── Decision de l´incertain/     # Dossier principal du TP Bandits
│   ├── main.py                 # Point d’entrée : lance une question du TP
│   ├── algorithmes_A.py        # Algorithmes (random, ε-greedy, UCB, etc.)
│   ├── bandit.py               # Environnement bandit
│   ├── environment.py          # Environnement de simulation
│   ├── question1.py            # Question 1
│   ├── question2.py            # Question 2
│   ├── question3.py            # Question 3
│   ├── partie2.py             # Partie 2
│   ├── rapport.tex             # Rapport LaTeX
│   ├── figures/                # Figures générées (PNG)
│   ├── slides-bandits.pdf      # Support de cours
│   └── tp-bandits.pdf         # Sujet du TP
├── .gitignore
└── README.md
```

## Prérequis

- Python 3 (testé avec 3.12)
- `numpy`, `matplotlib`

## Installation

```bash
cd "Decision de l´incertain"
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# ou: venv\Scripts\activate  # Windows
pip install numpy matplotlib
```

## Utilisation

Depuis le dossier `Decision de l´incertain` :

```bash
python3 main.py <question>
```

- `1`  → Question 1  
- `2`  → Question 2  
- `3`  → Question 3  
- `p2` → Partie 2  

Exemple :

```bash
python3 main.py 2
```

## Références

- Slides du cours : `slides-bandits.pdf`
- Sujet du TP : `tp-bandits.pdf`
- UCB-1 : Auer et al., Machine Learning Journal 2002
