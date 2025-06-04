---
layout: tags
icon: fas fa-tags
order: 4
---
🛡️ Projet Cyber : Système de Contrôle Parental Réseau avec C++ & IA
Présentation du projet

Dans le cadre de mon apprentissage et de mon intérêt pour la cybersécurité, j’ai développé avec l’aide de ChatGPT un système de contrôle parental pour réseau local. L’objectif principal était de permettre à un parent de surveiller et contrôler l’accès à certains sites web depuis n’importe quel appareil du réseau, sans matériel supplémentaire.
Objectifs

    Surveiller l’activité Internet sur le réseau local.
    Bloquer/Débloquer certains sites à distance via une interface parentale.
    Assurer la sécurité et la confidentialité des échanges entre les applications “parent” et “enfant”.

Stack technique

    C++ : Développement de l’application principale (client + serveur).
    Sockets TCP/IP : Communication réseau locale sécurisée.
    JSON : Échange de commandes et statuts.
    ChatGPT : Assistance sur l’architecture, le code, et la sécurisation.

Fonctionnement

    Application Enfant (Serveur) : S’installe sur l’ordinateur de l’enfant, surveille la navigation, reçoit et exécute des commandes (blocage/déblocage).
    Application Parent (Client) : Permet d’envoyer à distance des ordres (bloquer/débloquer des sites) via le réseau local.
    Protocole Sécurisé : Les échanges sont chiffrés, limités au réseau local, et chaque commande est authentifiée.

Étapes de développement

    Conception de l’architecture (échanges avec ChatGPT pour le schéma client-serveur).
    Développement du serveur (C++ : écoute réseau, gestion des commandes).
    Développement du client (interface de commande pour le parent).
    Ajout des règles de blocage (modification du fichier hosts ou usage de proxy local).
    Sécurisation (filtrage des IP, chiffrement des messages).
    Tests et améliorations (retours réguliers avec ChatGPT pour debug, optimisation et nouvelles idées).

Résultats

    👨‍👩‍👧 Contrôle parental efficace sans achat de matériel supplémentaire.
    ⚡ Temps réel : blocage/déblocage immédiat depuis l’application parent.
    🛡️ Sécurité renforcée des échanges et du contrôle.

Mon retour d’expérience

Ce projet m’a permis de :

    Approfondir mes compétences en C++ et en réseau.
    M’initier à la sécurité des communications (authentification, chiffrement).
    Optimiser mon workflow grâce à l’assistance d’une IA (ChatGPT), qui m’a aidé pour la résolution de bugs, l’amélioration du design, et la sécurisation globale.

Si tu veux voir le code source, le schéma d’architecture, ou discuter des choix techniques, contacte-moi ! 🚀
