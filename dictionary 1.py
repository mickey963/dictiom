import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# the dictionary
translations = {
    "Spanish": {"hello": "hola", "goodbye": "adiós", "please": "por favor", "thank you": "gracias", "yes": "si", "no": "no","sorry": "lo siento",
                "good morning": "Buenos días", "good night": "Buenas noches", "how are you": "¿Cómo estás", "i'm fine": "Estoy bien","water": "agua",
               "food": "comida", "help": "Ayuda", "friend": "amigo","excuse me": "pardon", "my name is": "Me llamo...", "How much is it?":"¿Cuánto cuesta?",
                "What’s your name": "¿Cómo te llamas?", "welcome": "Bienvenido/a", "home": "casa", "happy": "feliz"},

    "French": {"hello": "bonjour", "goodbye": "au revoir", "please": "S'il vous plaît", "thank you": "merci", "yes": "oui", "no": "non","sorry": "Désolé(e)",
                "good morning": "bonjour", "good night": "	Bonne nuit", "how are you": "Comment ça va ?", "i'm fine": "Ça va bien","water": "eau",
               "food": "Nourriture", "help": "aide", "friend": "ami(e)","excuse me": "Excusez-moi", "my name is": "Je m'appelle...", "How much is it?":"Combien ça coûte ?",
                "What’s your name": "Comment vous appelez-vous ?", "welcome": "bienvenue", "home": "maison", "happy": "heureux"},
   "german": {
        "hello": "hallo.",
        "goodbye": "auf Wiedersehen.",
        "please": "bitte.",
        "thank you": "danke.",
        "yes": "ja.",
        "no": "nein.",
        "cheese":"Käse.",
        "fish": "Fisch.",
        "bread": "Brot.",
        "school": "School",
        "window": "Schule",
        "door": "Tür",
        "water": "Wasser",
        "flower": "Blume",
        "light": "Licht",
        "heart": "Herz",
        "mountain": "Berg",
        "desert": "Wüste",
        "medicine": "Medizin",
        "refrigerator": "Kühlschrank"
},
 
"Igala_dictionary" = {"what is it?":"Ewnde.",
                    "stand":"Kwane.",
                    "sit up":"Kwane Gwane.",
                    "bend down":"Tekpe.",
                    "good morning":"Olodu.",
                    "God":"Ojo.",
                    "amen":"Amin.",
                    "pray":"Chadua.",
                    "king":"Onu.",
                    "prince":"Omonu.",
                    "messenger":"Onuche.",
                    "good afternoon":"Oroka.",
                    "welcome":"Olale.",
                    "good evening":"Olane.",
                    "who is it?":"Enede.",
                    "rice":"Oscapa.",
                    "yam":"Ushu.",
                    "beans":"Egwa.",
                    "water":"Omi",
                    "thank you":"Olakolo."
},

    "japanese": {
    "hello": "konnichiwa", "thank you": "arigatou", "goodbye": "sayounara",
    "good morning": "ohayou", "good evening": "konbanwa", "excuse me": "sumimasen",
    "yes": "hai", "no": "iie", "love": "ai", "friend": "tomodachi", "family": "kazoku",
    "food": "tabemono", "drink": "nomimono", "school": "gakkou", "teacher": "sensei",
    "student": "gakusei", "time": "jikan", "japan": "nihon", "cat": "neko", "dog": "inu",
}
}
# Function to translate"
def translate_word():
    selected_language = language_selector.get()
    english_word = english_entry.get().lower()

    if selected_language == "choose a language":
        messagebox.showerror("Error", " choose a language.")
        return

    if english_word in translations[selected_language]:
        translated_word = translations[selected_language][english_word]
        result_label.config(text=f'Translation: {translated_word}')
    else:
        result_label.config(text=" Translation not found.")
# GUI setup
root = tk.Tk()
root.title("5 language dictionary")
# language selector portion
language_label = tk.Label(root, text=" choose a language:")
language_label.pack(pady=5)

language_selector = ttk.Combobox(root, values=["Select Language"] + list(translations.keys()), state="readonly")
language_selector.set("pick a language")
language_selector.pack(pady=5)

english_label = tk.Label(root, text="Enter English Word:")
english_label.pack(pady=5)

english_entry = tk.Entry(root)
english_entry.pack(pady=5)

 #translate button
translate_button = tk.Button(root, text="Translate", command=translate_word)
translate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
