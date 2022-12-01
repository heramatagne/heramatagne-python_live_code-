#This program creates an English to French and English to Bulgarian translation dictionary.
#This dictionary translate a  word from English to French.
english_to_french_dictionary = {
    "family" : "Famille",
    "parent" : "Parent",
    "father" : "Pere",
    "mother" : "Mere",
    "child" : "Enfant",
    "son" : "Fils",
    "daugther" : "Fille",
    "brother" : "Frere",
    "sister" : "Soeur",
    "safou Plum" : "Prune/Safou"
}

#This dictionary translate a  word from English to bulgarian.
english_to_bulgarian_dictionary = {
    "family" : "семейство",
    "parent" : "Родител",
    "father" : "баща",
    "mother" : "Майка",
    "child" : "дете",
    "son" : "син",
    "daughter" : "Дъщеря",
    "brother" : "Брат",
    "sister" : "сестра",
    "safou Plum" : "сафу слива"
}

#language selection
language = input("Select the language of your choice. Enter FR for French or BG for Bulgarian:\n")

if language.lower() == "fr":
    word = input("Enter your word: ")
    #English to French translation
    word = word.lower()
    if word in english_to_french_dictionary:
        translation = english_to_french_dictionary.get(word)
        print(f"{word} is {translation} in French.")
    else:
         print(f"{word} is not in this dictionary. Please try another word.")

if language.lower() == "bg":
    word = input("Enter your word: ")
    word = word.lower()
    #English to Bulgarian translation
    if word in english_to_bulgarian_dictionary:
        translation= english_to_bulgarian_dictionary.get(word)
        print("{} is {} in Bulgarian.".format (word, translation))
    else:
        print(f"{word} is not in this dictionary. Please try another word.")

# if my_word in english_to_french_dictionary:
#     print("{} is {} in French.".format (my_word, translation))
# elif my_word in english_to_bulgarian_dictionary:
      
# else:
#         print(f"{my_word} is not in this dictionary. Please try another word.") 