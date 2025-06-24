import os
import yaml
from datetime import datetime
from pathlib import Path
from git import Repo

# === CONFIGURATION ===
PROJECTS_FILE = "projets.yaml"
POSTS_DIR = "_posts"
COMMIT_MESSAGE = "Ajout automatique de nouveaux articles depuis projets.yaml"

# === INITIALISATION ===
print("📄 Génération des articles...")
Path(POSTS_DIR).mkdir(parents=True, exist_ok=True)

try:
    with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
        projets = yaml.safe_load(f)
except FileNotFoundError:
    print(f"❌ Fichier {PROJECTS_FILE} introuvable.")
    exit(1)

created_count = 0

# === GÉNÉRATION DES POSTS ===
for projet in projets:
    title = projet["title"]
    date_str = projet["date"]
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    slug = title.lower().replace(" ", "-").replace(":", "").replace("/", "-")
    filename = f"{POSTS_DIR}/{date_str}-{slug}.md"

    if os.path.exists(filename):
        continue

    content = f"""---
title: "{title}"
date: {date_obj.strftime('%Y-%m-%d %H:%M:%S')} +0200
categories: {projet.get("categories", ["Projets"])}
tags: {projet.get("tags", [])}
---

{projet.get("description", "")}

"""

    if "github" in projet:
        content += f"- 🔗 [Code source]({projet['github']})\n"

    if "writeup" in projet:
        content += f"- 📝 [Write-up]({projet['writeup']})\n"

    with open(filename, "w", encoding="utf-8") as md_file:
        md_file.write(content)

    print(f"✅ Nouveau post créé : {filename}")
    created_count += 1

if created_count == 0:
    print("✅ Aucun nouveau post à créer.")
else:
    print(f"✅ {created_count} post(s) généré(s).")

# === GIT AUTOMATIQUE ===
print("\n📁 Commit Git...")
try:
    repo_path = Path(".").resolve()
    repo = Repo(repo_path)

    repo.git.add(all=True)
    repo.index.commit(COMMIT_MESSAGE)
    print("✅ Commit effectué.")

    print("📤 Push vers GitHub...")
    origin = repo.remote(name="origin")
    origin.push()
    print("✅ Push réussi ! 🎉")

except Exception as e:
    print(f"❌ Erreur Git : {e}")
