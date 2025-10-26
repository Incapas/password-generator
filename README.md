# 🛡️ Générateur de Mot de Passe Sécurisé (Streamlit)

## Description du Projet

Ce projet est une application web simple et interactive développée avec **Streamlit** en Python. Son objectif est de générer des mots de passe robustes et hautement aléatoires basés sur les critères définis par l'utilisateur (longueur, présence de majuscules, minuscules, chiffres et symboles).

L'interface utilise l'état de session (`st.session_state`) pour gérer les configurations utilisateur et l'affichage des messages dynamiques. L'application est conçue pour être minimaliste, efficace, et immédiatement fonctionnelle via une interface web.

## ✨ Fonctionnalités Clés

  * **Génération Personnalisée :** Choix de la **longueur** du mot de passe (12 à 100 caractères) et des **types de caractères** inclus.
  * **Sécurité Assurée :** Utilisation de la bibliothèque standard `random` pour une sélection aléatoire uniforme des caractères.
  * **Gestion des Options :** Logique pour empêcher la génération si **aucune** option de caractère n'est sélectionnée (message d'erreur via `st.toast`).
  * **Copie Facile :** Bouton de copie du mot de passe généré dans le presse-papiers (`pyperclip`).
  * **Réinitialisation Rapide :** Bouton pour remettre toutes les options de configuration à leurs valeurs par défaut.
  * **Structure Robuste :** Gestion propre de l'état des widgets via l'initialisation du `st.session_state` pour éviter les erreurs de conflit de valeurs par défaut.

-----

## 👥 Contributions au Projet

### 👩 Développeur Initial

Contribution résidant dans l'**initiative**, la **conception de l'interface utilisateur (UI)** et l'**établissement du squelette fonctionnel** de l'application.

| Catégorie | Description de la contribution |
| :--- | :--- |
| **Squelette de l'Application** | 🎯 **Conception Initiale :** Définition de l'objectif (générateur de mot de passe) et choix de l'outil (Streamlit). |
| | 🖼️ **Mise en Page (Layout) :** Structuration de l'interface (titres, séparateurs, colonnes). |
| | ⚙️ **Définition des Widgets :** Création des `st.checkbox`, `st.slider`, et `st.text_input` avec leurs clés de session (`key`). |
| **Logique de Base** | 📝 **Fonction `generate_password` :** Définition du flux de base pour lire les options, charger les données JSON, et générer la chaîne aléatoire. |
| | 📋 **Fonctions `copy_password` et `reset_configuration` :** Implémentation de la logique initiale pour copier et réinitialiser les états. |
| | 📦 **Dépendance JSON :** Utilisation d'un fichier `data.json` externe pour la source des caractères. |

### 🧑 Assistant IA Gemini

Contribution axée sur l'**amélioration de la qualité du code**, sa **documentation** et l'**augmentation de la robustesse** de l'application Streamlit.

| Catégorie | Description de la Contribution |
| :--- | :--- |
| **Documentation & Clarté** | 📑 **Documentation du Code :** Ajout de *docstrings* clairs pour chaque fonction et de commentaires détaillés ligne par ligne. |
| | 🏷️ **Annotations de Type :** Ajout des *type hints* (`-> None`, `: List[str]`, etc.) pour la clarté et la maintenabilité du code. |
| **Fiabilité Streamlit** | 🐞 **Résolution du Conflit Session State :** Implémentation de l'initialisation conditionnelle des variables de session (`if "key" not in st.session_state:`) pour prévenir l'erreur de valeur par défaut lors de la réinitialisation. |
| | 🔔 **Amélioration du Feedback Utilisateur :** Utilisation de **notifications temporaires (`st.toast`)** pour les actions réussies ou les avertissements, améliorant l'expérience utilisateur. |
| **Robustesse de la Logique** | 🛑 **Vérification d'Option Obligatoire :** Intégration de la logique de vérification qui empêche la génération si aucune option n'est cochée. |
| | 🐛 **Gestion des Erreurs Data :** Renforcement de la gestion des erreurs de chargement ou de décodage du fichier `data.json`. |

-----

## 🛠️ Prérequis

Pour lancer cette application en local, vous devez avoir :

1.  **Python 3.x**
2.  Un fichier `data.json` contenant les listes de caractères (minuscules, majuscules, chiffres, symboles) à la racine du projet.

## 🚀 Démarrage

1.  Installez les dépendances Python :
    ```bash
    pip install -r requirements.txt
    ```
2.  Exécutez l'application en lançant le fichier principal :

```bash
streamlit run main.py
```

## 📝 Guide d'Utilisation

1.  **Configuration :** Ajustez la **Longueur du mot de passe** et cochez/décochez les types de caractères souhaités.
2.  **Générer :** Cliquez sur **"✨ Générer"** pour obtenir un nouveau mot de passe.
3.  **Copier :** Cliquez sur **"📋 Copier"** pour le mettre dans votre presse-papiers (un toast confirmera l'action).
4.  **Réinitialiser :** Cliquez sur **"🔧 Réinitialiser"** pour revenir aux options par défaut (longueur 16, toutes les options cochées).