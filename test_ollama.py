import ollama

reponse = ollama.chat(
    model="qwen2.5:7b",
    messages=[{"role": "user", "content": "Dis bonjour en une phrase."}],
)
print(reponse["message"]["content"])