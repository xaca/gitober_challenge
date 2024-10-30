import os
import google.generativeai as genai

# Se debe guardar la clave en una variable de entorno de esta forma "export GEMINI_API_KEY="XXXXXXXXXXXXXXXXXXXXX"
#debes instalar antes de correr el proyecto"pip install google-generativeai"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 256,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "Limítate a responder exclusivamente sobre temas de Halloween. Habla sobre tradiciones, historias de terror, personajes icónicos, películas de Halloween, disfraces, decoración, mitos y leyendas, o cualquier tema relacionado con Halloween. No respondas preguntas ni des información que no esté directamente relacionada con Halloween.\n",
            ],
        },
        {
            "role": "model",
            "parts": [
                "¡Perfecto! Estoy listo para hablar de Halloween. ¿Te gustaría saber sobre las tradiciones más populares, historias de terror clásicas, personajes icónicos como Drácula o Frankenstein, o quizás te interesa la decoración espeluznante?  ¿Prefieres saber de películas de terror clásicas o disfraces creativos? \n\n¡Dime qué te interesa y empecemos a celebrar Halloween! 🎃👻 \n",
            ],
        },
    ]
)

def halloween_chatbot():
    print("¡Bienvenido al Chatbot de Halloween! Pregúntame cualquier cosa sobre Halloween.")
    
    while True:
        user_input = input("Tú: ")

        if user_input.lower() in ["salir", "exit", "adiós"]:
            print("Chatbot: ¡Hasta luego y que tengas un Halloween espeluznante! 🎃")
            break

        response = chat_session.send_message(user_input)
        
        print(f"Chatbot: {response.text}")

if __name__ == "__main__":
    halloween_chatbot()
