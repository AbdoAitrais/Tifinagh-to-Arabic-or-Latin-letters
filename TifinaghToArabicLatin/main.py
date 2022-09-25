from tifinagh_conversion import word_tifinar_to_arabic
from tifinagh_conversion import word_tifinar_to_latin


choice = 1

print("*********** Tifinagh converter ***********\n")

while choice != 0:
    tifinar_string = input("Tifinagh word : ").split(" ")
    arab_string = ""
    latin_string = ""
    for tifinar_word in tifinar_string:
        arab_string += word_tifinar_to_arabic(tifinar_word) + " "
        latin_string += word_tifinar_to_latin(tifinar_word) + " "

    print("بالحروف العربية : " + arab_string)
    print("In latin : " + latin_string)

    choice = int(input("Want another round ?\n0. No\n1. Yes\n> "))

