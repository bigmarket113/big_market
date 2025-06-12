#!/bin/bash

echo "Liste des fichiers dans big_market :"
ls -l big_market

echo
echo "Statut git :"
git status

echo
echo "Ajout des fichiers big_market au commit..."
git add big_market/

echo "Création du commit..."
git commit -m "Ajout ou mise à jour des fichiers du dossier big_market"

echo "Push vers la branche main..."
git push origin main

echo "Terminé. Vérifie sur GitHub si les fichiers sont bien là."
