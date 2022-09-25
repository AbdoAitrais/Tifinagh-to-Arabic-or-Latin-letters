def tifinar_to_arabic(letter):
    switcher = {
        'ⴰ': 'ا',
        'ⴱ': 'ب',
        'ⴳ': 'غ',
        'ⴳⵯ': 'غ',
        'ⴷ': 'د',
        'ⴹ': 'ض',
        'ⴻ': 'ي',
        'ⴼ': 'ف',
        'ⴽ': 'ك',
        'ⴽⵯ': 'ك',
        'ⵀ': 'ه',
        'ⵃ': 'ح',
        'ⵄ': 'ع',
        'ⵅ': 'خ',
        'ⵇ': 'ق',
        'ⵉ': 'ي',
        'ⵊ': 'ج',
        'ⵍ': 'ل',
        'ⵎ': 'م',
        'ⵏ': 'ن',
        'ⵓ': 'و',
        'ⵔ': 'ر',
        'ⵕ': 'ر',
        'ⵖ': 'غ',
        'ⵙ': 'س',
        'ⵚ': 'ص',
        'ⵛ': 'ش',
        'ⵜ': 'ت',
        'ⵟ': 'ط',
        'ⵡ': 'و',
        'ⵢ': 'ي',
        'ⵣ': 'ز',
        'ⵥ': 'ز'
    }
    output = switcher.get(letter, None)
    if output is None:
        return None
    return output


def tifinar_to_latin(letter):
    switcher = {
        'ⴰ': 'a',
        'ⴱ': 'b',
        'ⴳ': 'g',
        'ⴳⵯ': 'g',
        'ⴷ': 'd',
        'ⴹ': 'Ḍ',
        'ⴻ': 'e',
        'ⴼ': 'f',
        'ⴽ': 'k',
        'ⴽⵯ': 'k',
        'ⵀ': 'h',
        'ⵃ': 'H',
        'ⵄ': 'ɛ',
        'ⵅ': 'kh',
        'ⵇ': 'q',
        'ⵉ': 'i',
        'ⵊ': 'j',
        'ⵍ': 'l',
        'ⵎ': 'm',
        'ⵏ': 'n',
        'ⵓ': 'u',
        'ⵔ': 'r',
        'ⵕ': 'Ṛ',
        'ⵖ': 'ɣ',
        'ⵙ': 's',
        'ⵚ': 'Ṣ',
        'ⵛ': 'sh',
        'ⵜ': 't',
        'ⵟ': 'Ṭ',
        'ⵡ': 'w',
        'ⵢ': 'y',
        'ⵣ': 'z',
        'ⵥ': 'Ẓ'
    }
    output = switcher.get(letter, None)
    if output is None:
        return None
    return output


def word_tifinar_to_arabic(tifinar_word):
    arab_word = ""
    for letter in tifinar_word:
        tifinar_letter = tifinar_to_arabic(letter)
        if tifinar_letter is not None:
            arab_word = arab_word + tifinar_letter

    return arab_word


def word_tifinar_to_latin(tifinar_word):
    latin_word = ""
    for letter in tifinar_word:
        tifinar_letter = tifinar_to_latin(letter)
        if tifinar_letter is not None:
            latin_word = latin_word + tifinar_letter

    return latin_word
