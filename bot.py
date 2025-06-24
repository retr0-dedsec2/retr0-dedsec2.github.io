import os
import yaml
from datetime import datetime
from pathlib import Path
from git import Repo  # pour GitPython


# Chemin du dépôt local (à adapter si besoin)
repo_path = Path(".").resolve()

# Charger le repo
repo = Repo(repo_path)

# Ajouter les nouveaux fichiers
repo.git.add(all=True)

# Faire un commit
commit_message = "Ajout automatique de nouveaux articles depuis projets.yaml"
repo.index.commit(commit_message)

# Pousser sur la branche par défaut (main ou master)
origin = repo.remote(name="origin")
origin.push()
