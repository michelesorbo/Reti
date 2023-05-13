import openai
import time
#Importare la mia ApenAI API Key
openai.api_key = "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"

#Settare il modello e il prompt
model_engine = "davinci"
prompt = "Ciao come posso aiutarti?" #Messaggio iniziale

#Genero la risposta
completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5,
)

response = completion.choices[0].text.strip()
print(response)


# Funzione per ottenere la risposta di ChatGPT
# def get_gpt_response(prompt):
#     try:
#         # Chiamata all'API di OpenAI per ottenere la risposta di ChatGPT
#         response = openai.Completion.create(
#           engine="davinci",
#           prompt=prompt,
#           max_tokens=1024,
#           n=1,
#           stop=None,
#           temperature=0.7,
#         )
#         # Estrae la risposta dal risultato della chiamata all'API
#         message = response.choices[0].text.strip()
#         return message
#     except Exception as e:
#         print("Errore:", e)
#         return None

# # Loop principale del programma
# while True:
#     # Chiede all'utente di inserire il messaggio
#     message = input("Inserisci il tuo messaggio: ")
#     # Aggiunge il messaggio alla prompt di ChatGPT
#     prompt = "Utente: " + message + "\nChatGPT:"
#     # Ottiene la risposta di ChatGPT
#     response = get_gpt_response(prompt)
#     # Se la risposta è stata ottenuta, la stampa a video
#     if response is not None:
#         print(response)
#     else:
#         print("Errore nella richiesta.")
#     # Pausa di 1 secondo
#     time.sleep(1)