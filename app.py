import json
import time
from datetime import datetime

import gradio as gr
from rag import indexer, repondre

indexer()


def journaliser(entree):
    with open("journal.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(entree, ensure_ascii=False) + "\n")


def chat(message, historique, profil):
    debut = time.time()
    reponse, sources, appels = repondre(message)
    journaliser({
        "horodatage": datetime.now().isoformat(),
        "utilisateur": profil,
        "question": message,
        "sources": sources,
        "outils": appels,
        "reponse": reponse,
        "duree_s": round(time.time() - debut, 2),
    })
    infos = f"\n\n*Sources : {', '.join(sources)}*"
    if appels:
        infos += f"\n\n*Outils appelés : {appels}*"
    return reponse + infos


demo = gr.ChatInterface(
    fn=chat,
    additional_inputs=[gr.Dropdown(["utilisateur", "admin"], value="utilisateur", label="Profil")],
    title="Assistant interne de l'Entreprise X",
)

if __name__ == "__main__":
    demo.launch()