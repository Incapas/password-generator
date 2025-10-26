import json
import random
from typing import List, Dict

import streamlit as st
import pyperclip

# ==============================================================================
# 🧩 LOGIQUE DU GÉNÉRATEUR (Fonctions de Callback)
# ==============================================================================

def generate_password() -> None:
    """
    Génère un mot de passe aléatoire basé sur les options sélectionnées.

    Gère la vérification qu'au moins un type de caractère est sélectionné
    et affiche une notification temporaire ('toast') si ce n'est pas le cas.
    """
    
    # Réinitialise le message d'erreur persistant (utilisé pour les erreurs JSON)
    st.session_state["error_message"] = ""

    # Vérifie si aucune des options de caractère n'est cochée
    if not (
        st.session_state["use_lowercase"] or
        st.session_state["use_uppercase"] or
        st.session_state["use_digits"] or
        st.session_state["use_symbols"]
        ):
        # Affiche un toast pour informer l'utilisateur qu'il manque des options
        st.toast("⚠️ Veuillez choisir au moins une option de caractère pour générer le mot de passe.")
        # Efface tout mot de passe précédent
        st.session_state["password_output"] = ""
        # Arrête l'exécution de la fonction
        return
    
    # Tente de charger les données des caractères à partir du fichier JSON
    try:
        # Ouvre le fichier de données en mode lecture
        with open("data.json", "r") as f:
            # Charge le contenu JSON dans la variable data (typé comme un dictionnaire générique)
            data: Dict[str, List[str]] = json.load(f)
    except Exception as e:
        # En cas d'erreur (fichier manquant, JSON invalide, etc.), définit le message d'erreur persistant
        st.session_state["error_message"] = f"Erreur de données: Impossible de charger 'data.json'. ({e})"
        # Efface tout mot de passe précédent
        st.session_state["password_output"] = ""
        # Arrête l'exécution
        return
        
    # Initialise une liste pour stocker tous les caractères possibles
    options: List[str] = []
    
    # Ajoute les lettres minuscules si l'option est cochée
    if st.session_state["use_lowercase"]:
        # Utilise .get() pour récupérer la liste, ou une liste vide si la clé n'existe pas
        options.extend(data.get("latin_lower_alphabet", []))

    # Ajoute les lettres majuscules si l'option est cochée
    if st.session_state["use_uppercase"]:
        options.extend(data.get("latin_upper_alphabet", []))

    # Ajoute les chiffres si l'option est cochée
    if st.session_state["use_digits"]:
        options.extend(data.get("arabic_numerals", []))

    # Ajoute les symboles si l'option est cochée
    if st.session_state["use_symbols"]:
        options.extend(data.get("punctuation_characters", []))

    # Vérifie si la liste des options est vide (erreur dans data.json malgré les options cochées)
    if not options:
        # Définit un message d'erreur spécifique pour les données (persistant)
        st.session_state["error_message"] = "Erreur de données : Les options sélectionnées ne contiennent aucun caractère valide dans data.json."
        # Efface tout mot de passe précédent
        st.session_state["password_output"] = ""
        # Arrête l'exécution
        return

    # Récupère la longueur désirée du mot de passe (typé comme un entier)
    lenght: int = st.session_state["password_length"]

    # Génère le mot de passe en tirant aléatoirement des caractères dans la liste `options`
    password: str = "".join(random.choices(options, k=lenght))

    # Met à jour le champ de sortie avec le mot de passe généré
    st.session_state["password_output"] = password

def copy_password() -> None:
    """
    Copie le mot de passe généré dans le presse-papiers et affiche un toast.
    """
    # Récupère le mot de passe s'il existe (typé comme une chaîne de caractères ou None)
    password_to_copy: str | None = st.session_state.get("password_output")

    # Vérifie si un mot de passe existe
    if password_to_copy:
        try:
            # Tente de copier le mot de passe
            pyperclip.copy(password_to_copy)
            # Affiche un message de succès (toast)
            st.toast("Mot de passe copié dans le presse-papiers! 📋", icon="✅")
        except pyperclip.PyperclipException:
            # Affiche un message d'erreur si la copie échoue
            st.toast("Impossible de copier dans le presse-papiers (Pyperclip non supporté).", icon="❌")
    else:
        # Affiche un avertissement si le champ est vide
        st.toast("Rien à copier : générez un mot de passe d'abord.", icon="ℹ️")

def reset_configuration() -> None:
    """
    Réinitialise toutes les options et le mot de passe généré aux valeurs par défaut et affiche un toast
    """
    # Réinitialise les lettres minuscules (coché)
    st.session_state["use_lowercase"] = True
    # Réinitialise les lettres majuscules (coché)
    st.session_state["use_uppercase"] = True
    # Réinitialise les chiffres (coché)
    st.session_state["use_digits"] = True
    # Réinitialise les symboles (coché)
    st.session_state["use_symbols"] = True
    # Réinitialise la longueur du mot de passe à 16
    st.session_state["password_length"] = 16
    # Efface le mot de passe affiché
    st.session_state["password_output"] = ""
    # Efface tout message d'erreur résiduel
    st.session_state["error_message"] = ""

    # Affiche un message de succès (toast)
    st.toast("Réinitialisation effectuée.", icon="👍")


# ==============================================================================
# 🖥️ INTERFACE STREAMLIT
# ==============================================================================

# Configure la page Streamlit
st.set_page_config(
    page_title="Générateur de Mot de Passe",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- INITIALISATION DES VARIABLES DU SESSION STATE ---
# C'est la solution pour éviter le conflit "default value vs Session State API".
# On initialise les valeurs par défaut si elles ne sont pas déjà présentes.

# Initialise l'état pour le message d'erreur
if "error_message" not in st.session_state:
    st.session_state["error_message"] = ""

# Initialise l'état des checkboxes (Doit correspondre aux valeurs par défaut souhaitées)
if "use_lowercase" not in st.session_state:
    st.session_state["use_lowercase"] = True
if "use_uppercase" not in st.session_state:
    st.session_state["use_uppercase"] = True
if "use_digits" not in st.session_state:
    st.session_state["use_digits"] = True
if "use_symbols" not in st.session_state:
    st.session_state["use_symbols"] = True
if "password_length" not in st.session_state:
    st.session_state["password_length"] = 16
if "password_output" not in st.session_state:
    st.session_state["password_output"] = ""
# ----------------------------------------------------

# Affiche le titre principal de l'application
st.title("🛡️ Générateur de Mot de Passe")

# Ajoute un séparateur visuel
st.divider()

# Affiche le sous-titre pour les options du mot de passe
st.subheader("Options du mot de passe")

# Crée un placeholder (conteneur vide) pour afficher le message d'erreur (pour les erreurs JSON/data.json)
message_placeholder: st.delta_generator.DeltaGenerator = st.empty()

# Crée deux colonnes pour aligner les checkboxes
col1, col2 = st.columns(2)

with col1:
    # Checkbox pour les minuscules. La valeur est tirée du Session State.
    st.checkbox("Lettres latines minuscules (a-z)", key="use_lowercase")
    # Checkbox pour les chiffres. La valeur est tirée du Session State.
    st.checkbox("Chiffres arabes (0-9)", key="use_digits")

with col2:
    # Checkbox pour les majuscules. La valeur est tirée du Session State.
    st.checkbox("Lettres latines majuscules (A-Z)", key="use_uppercase")
    # Checkbox pour les symboles. La valeur est tirée du Session State.
    st.checkbox("Caractères spéciaux (!@#...)", key="use_symbols")

# Si un message d'erreur est présent dans l'état de session, l'afficher dans le placeholder
if st.session_state["error_message"]:
    with message_placeholder.container():
        # Affiche le message d'erreur formaté par Streamlit
        st.error(st.session_state["error_message"])

# Ajoute un séparateur visuel
st.divider()

# Affiche le sous-titre pour la longueur du mot de passe
st.subheader("Longueur du mot de passe")

# Slider pour la sélection de la longueur du mot de passe.
st.slider(
    "lenght",
    min_value=12,
    max_value=100,
    step=1,
    key="password_length",
    label_visibility="collapsed" # Cache l'étiquette par défaut
)

# Ajoute un séparateur visuel
st.divider()

# Affiche le sous-titre pour le mot de passe généré
st.subheader("Mot de passe généré")

# Champ de texte pour afficher le mot de passe.
st.text_input(
    "password", 
    key="password_output", 
    type="password",
    label_visibility="collapsed" # Cache l'étiquette par défaut
)

# Ajoute un séparateur visuel
st.divider()

# Crée trois colonnes pour les boutons d'action
col_btn_1, col_btn_2 , col_btn_3= st.columns(3)

with col_btn_1:
    # Bouton Générer, appelle `generate_password` au clic
    st.button(
        "✨ Générer", 
        key="generate_button", 
        width="stretch", 
        type="primary", 
        on_click=generate_password
    )

with col_btn_2:
    # Bouton Copier, appelle `copy_password` au clic
    st.button(
        "📋 Copier", 
        key="copy_button", 
        width="stretch", 
        type="secondary", 
        on_click=copy_password
    )

with col_btn_3:
    # Bouton Réinitialiser, appelle `reset_configuration` au clic
    st.button(
        "🔧 Réinitialiser", 
        key="reset_button", 
        width="stretch", 
        type="secondary", 
        on_click=reset_configuration
    )