from outils import read_file

print("--- Test 1 : fichier légitime ---")
print(read_file("public/horaires.txt")[:120])

print("\n--- Test 2 : fichier confidentiel, aucun contrôle d'accès ---")
print(read_file("confidential/salaires_confidentiel.txt")[:120])

print("\n--- Test 3 : remontée de chemin hors du dossier data ---")
print(read_file("../creer_documents.py")[:120])