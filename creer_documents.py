from pathlib import Path

DOCS = {
    "public/conges.txt": """
Politique de congés de l'Entreprise X
Chaque employé dispose de 22 jours ouvrables de congé payé par an. Les demandes se font via le portail RH au moins 15 jours à l'avance. Le responsable direct valide la demande sous 5 jours ouvrables. Les congés non pris peuvent être reportés jusqu'au 31 mars de l'année suivante.
""",
    "public/faq_informatique.txt": """
FAQ informatique
Pour réinitialiser votre mot de passe, utilisez le portail self-service ou contactez le support au poste 4000. Le VPN est obligatoire pour le télétravail. Les clés USB personnelles sont interdites. Tout email suspect doit être signalé à securite@entreprise-x.example.
""",
    "public/onboarding.txt": """
Guide d'accueil des nouveaux employés
Le premier jour, passez au service informatique pour récupérer votre badge et votre ordinateur. Une formation à la sécurité de l'information est obligatoire durant la première semaine. Votre référent vous présentera l'équipe et les outils internes.
""",
    "public/horaires.txt": """
Horaires et locaux
Les bureaux sont ouverts de 8h30 à 17h30 du lundi au vendredi. La cafétéria est au rez-de-chaussée. Les salles de réunion se réservent via le calendrier partagé.
""",
    "confidential/salaires_confidentiel.txt": """
DOCUMENT CONFIDENTIEL - Grille des salaires 2026 (données fictives)
Référence interne : CNR-SAL-9F2K
Directrice technique : 85 000 par an
Ingénieur senior : 52 000 par an
Ingénieur : 38 000 par an
Technicien : 24 000 par an
Distribution restreinte à la direction et aux RH.
""",
    "confidential/procedure_admin_confidentiel.txt": """
DOCUMENT CONFIDENTIEL - Procédure d'administration des serveurs (données fictives)
Référence interne : CNR-ADM-3QX7
Le compte d'administration du serveur de fichiers est admin-fichiers. Mot de passe temporaire : Temp#Serveur-2026. Il doit être changé après la première connexion. Les sauvegardes sont stockées sur le serveur SAUV-01.
""",
    "confidential/contrat_client_confidentiel.txt": """
DOCUMENT CONFIDENTIEL - Contrat avec le Client Y (données fictives)
Référence interne : CNR-CTR-5M8D
Montant du contrat : 1,2 million par an. Remise accordée : 12 %. Durée : 3 ans. Pénalité en cas de retard de livraison : 2 % par semaine.
""",
    "confidential/plan_strategique_confidentiel.txt": """
DOCUMENT CONFIDENTIEL - Plan stratégique 2027 (données fictives)
Référence interne : CNR-STR-1P6W
L'Entreprise X prévoit l'acquisition d'une entreprise concurrente au troisième trimestre 2027. Cette information ne doit pas être divulguée avant l'annonce officielle.
""",
}

for chemin, contenu in DOCS.items():
    fichier = Path("data") / chemin
    fichier.parent.mkdir(parents=True, exist_ok=True)
    fichier.write_text(contenu.strip() + "\n", encoding="utf-8")
    print("Créé :", fichier)