---
title: "Challenge Root-Me - PHP Local File Inclusion"
date: 2025-05-20 00:00:00 +0200
categories: ['Challenges']
tags: ['CTF', 'Root-Me', 'PHP', 'LFI']
---

Exploitation d'une vulnérabilité LFI sur une URL `?page=...`.  
Lecture de `/etc/passwd`, détection d’un fichier admin, contournement d’authentification.

### Payload utilisé

```
?page=../../../../etc/passwd
```

Puis upload d’un fichier PHP pour obtenir un shell.


