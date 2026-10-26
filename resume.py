import json
import sys

for chemin in sys.argv[1:]:
    d = json.load(open(chemin, encoding="utf-8"))
    cond = d.get("condition", d.get("version"))
    print(f"\nRésumé ({d['resultats'][0]['n']} essais par attaque, {cond}) :")
    print(f"{'ID':<6}{'Catégorie':<11}{'Succès':<9}{'Taux':<7}{'Fuite':<8}{'Outils':<8}{'Piège':<8}Attaque")
    for r in d["resultats"]:
        n = r["n"]
        fuite = f"{r['fuites']}/{n}" if "fuites" in r else "-"
        outils = f"{r['essais_avec_outil']}/{n}" if "essais_avec_outil" in r else "-"
        piege = f"{r['pieges_recuperes']}/{n}" if "pieges_recuperes" in r else "-"
        print(f"{r['id']:<6}{r['categorie']:<11}{str(r['reussites']) + '/' + str(n):<9}"
              f"{str(r['taux']) + ' %':<7}{fuite:<8}{outils:<8}{piege:<8}{r['nom']}")