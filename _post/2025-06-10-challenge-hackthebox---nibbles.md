---
title: "Challenge HackTheBox - Nibbles"
date: 2025-06-10 00:00:00 +0200
categories: ['Actualités']
tags: ['CTF', 'HackTheBox', 'Web Exploit']
---

Challenge CTF réussi sur HackTheBox en exploitant une vulnérabilité RFI sur un CMS pour obtenir un reverse shell.


- 📝 [Write-up](### Accès initial
Scan Nmap → CMS détecté avec page `nibbleblog`.

### Exploit
Upload d’un fichier PHP via une vulnérabilité RFI.

### Escalade
Sudo mal configuré : root shell via exécution de script en tant qu’admin.
)
