meme_dict = {
            "LOL": "una respuesta a algo gracioso",
            "CRINGE": "algo raro o embarazoso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado",
            "MEWING": "un término de jerga que se refiere a un ejercicio de lengua en el que la lengua se apoya contra el paladar, que algunos han afirmado que puede cambiar la forma de la mandíbula",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print("la respuesta es :")
    print(meme_dict[word])   
else:
     print("LA PALABRA NO SE ENCUENTRA EN EL DICCIONARIO")
