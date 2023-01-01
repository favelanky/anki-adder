def add_card(word, translation_tuple, synonyms):
    """Function for adding word to Anki"""
    translations, examples = translation_tuple
    print(word)
    print(translations)
    print(examples)
    with open("D:\\PyCharmProjects\\anki_adder\\src\\test.txt", "a", encoding='UTF-8') as f:
        f.write(f"<b>{word}</b> :")
        for i in range(min(5, len(synonyms))):
            f.write(f" {synonyms[i]}")
            if i + 1 == min(5, len(synonyms)):
                f.write(".")
            else:
                f.write(",")
        f.write("<br>")
        f.write("<br>")
        color = '<b style="background-color: #ffe100; color: #373737">'
        f.write(f'{examples[0].replace(word, color + word + "</b>")}<br>')
        f.write(f'{examples[1].replace(word, color + word + "</b>")}')
        f.write("~")
        for i in range(min(5, len(translations))):
            f.write(f" {translations[i]}")
            if i + 1 == min(5, len(translations)):
                f.write(".")
            else:
                f.write(",")
        f.write('\n')
