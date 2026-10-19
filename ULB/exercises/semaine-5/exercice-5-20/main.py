def nouveaux_heros(premier_fichier_txt: str, deuxieme_fichier_txt: str) -> None:
    with open(premier_fichier_txt) as f:
        texte = f.read()

    texte = texte.replace("Paul", "Tom")
    texte = texte.replace("Pierre", "Paul")
    texte = texte.replace("Jacqueline", "Mathilde")

    with open(deuxieme_fichier_txt, "w") as s:
        s.write(texte)
