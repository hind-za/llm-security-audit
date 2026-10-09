import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data")


def read_file(path: str) -> str:
    """Lit un fichier de la base documentaire et retourne son contenu.

    Args:
        path: chemin du fichier, par exemple public/conges.txt
    """
    try:
        return (DATA_DIR / path).read_text(encoding="utf-8")
    except Exception as e:
        return f"Erreur : {e}"


def send_email(to: str, subject: str, body: str) -> str:
    """Envoie un email (simulé : écrit dans outbox.jsonl).

    Args:
        to: adresse du destinataire
        subject: objet du message
        body: contenu du message
    """
    ligne = {"date": datetime.now().isoformat(), "to": to, "subject": subject, "body": body}
    with open("outbox.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    return f"Email envoyé à {to}."


OUTILS = {"read_file": read_file, "send_email": send_email}