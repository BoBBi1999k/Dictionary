import tkinter as tk
from tkinter import messagebox

dictionaries = {
    "Yoruba": {
        'omo':"child", 'ile':"House", 'eja':"fish", 'owo':"money", 'ise':"work", 'eti': "ear",
        'ojo':"day", 'ale':"night",'ounje':"food",'oko':"husband", 'bawo':"hello", 'E kabo':"thank you",
        'ore':"friend", 'iya':"mother", 'baba':"father", 'ase':"agreement", 'o jo':"rain",
        'omi':"water", 'ayo':"joy", 'eko':"lagos"
    },
    "Hausa":{
        'wawa':"fool", 'chokali':"spoon", 'baki':"mouth", 'ido':"eye", 'rana':"day", 'kwano':"plate",
        'dare':"night", 'duste':"stone", 'jaki':"donkey", 'kafa':"leg", 'ina kwana':"good morning",
        'na gode':"thank you", 'aboki':"friend", 'ran a':"tomorrow", 'lafiya':"good health",
        'gida':"home", 'uwa':"mother", 'baba':"father", 'kwa no':"pot"

    },
    "Igbo":{
        'Nno':"hello", 'kedu':"how are you?",'imela':"thank you", 'biko':"please", 'oga':"sir/mister",
        'Nne':"mother", 'Nna':"father", 'nwannem':"brother/sister", 'onye':"person", 'afo':"year",
        'ora':"town", 'uzo':"road", 'Mmiri':"water", 'anya':"eye", 'ozu':"bone", 'eke':"python",
        'okuko':"chicken", 'aku':"tiger", 'ude':"peace", 'chukwu':"God"
    },
  
    "Spanish":{
            'hola':"hello",'adios':"goodbye",'buenos dias':"good morning",'bien':"good",'buenas tardes':"good afternoon",
            'buenas noches':"good evening/night",'mal':"bad",'¿como estáS?':"How are you",'mas o menos':"so-so",
            'por favor':"please",'uno':"one",'tres':"three",'diez':"ten",'rojo':"red",'azul':"blue",
            'Verde':"green",'madre':"mother",'parde':"father",'hermana':"sister",'abuelo':"grandfather"
    },

    "efik":{
        'Mme':"hello", 'koko':"good morning", 'ke':"thank you", 'Mmi':"mother", 'ada':"father", 'ete':"brother",
        'eka':"sister", 'urua':"town", 'mbakara':"river", 'ukot':"farm", 'ekpo':"ghost", 'nsia':"love", 'ekaete':"beautiful",
        'mfia':"good", 'ukpono':"peace", 'aifa':"joy", 'ekemma':"wisdom", 'uwem':"life", 'abasi':"God",
    }
}

# Function to search the selected dictionary
def search_word():
    selected_dictionary = dictionary_var.get()
    word = entry.get().strip().lower()  # Get user input, trim spaces, and convert to lowercase
    meaning = dictionaries.get(selected_dictionary, {}).get(word)

    if meaning:
        result_label.config(text=f"Meaning: {meaning}")
    else:
        result_label.config(text="")
        messagebox.showinfo(
            "Not Found",
            f"The word '{word}' is not in the {selected_dictionary} dictionary.",
        )


root = tk.Tk()
root.title("Nigerian Dictionary")
welcome_label = tk.Label(root, text="Welcome", padx=200, pady=80, bg='red', fg="white",
                         font='Arial 16')
welcome_label.pack()
root.geometry("600x600")

# Title
title_label = tk.Label(root, text="Please select a Language")
title_label.pack(pady=10)

# Sekection menu
dictionary_var = tk.StringVar(value="language")
dictionary_menu = tk.OptionMenu(root, dictionary_var, *dictionaries.keys())
dictionary_menu.pack()

# Word Entry
word_label = tk.Label(root, text="Enter a word:")
word_label.pack()

entry = tk.Entry(root)
entry.pack()

# Search Button
search_button = tk.Button(root, text="Search", command=search_word, pady=10, padx=10)
search_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Meaning will appear here.")
result_label.pack(pady=20)

# Run the application
root.mainloop()
