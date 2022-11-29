#This program creates an English to French and English to Bulgarian translation dictionary.

#This dictionary translate a  word from English to French.
english_to_french_dictionary = {
    "Family" : "Famille",
    "Parent" : "Parent",
    "Father" : "Pere",
    "Mother" : "Mere",
    "child" : "Enfant",
    "Son" : "Fils",
    "Daugther" : "Fille",
    "Brother" : "Frere",
    "Sister" : "Soeur",
    "Safou Plum" : "Prune/Safou"
}

#This dictionary translate a  word from English to bulgarian.
english_to_bulgarian_dictionary = {
    "Love" : "любов",
    "Grandparents" : "Дядо и баба",
    "Dad" : "татко",
    "Mum" : "мама",
    "kid" : "хлапе",
    "Boy" : "момче",
    "Girl" : "момиче",
    "Uncle" : "чичо",
    "Aunt" : "леля",
    "Plum" : "слива"
}
my_word = input("Enter your word \n")

#English to French translation
translation = english_to_french_dictionary.get(my_word)
#English to Bulgarian translation
translation2= english_to_bulgarian_dictionary.get(my_word)

if my_word in english_to_french_dictionary:
    print("{} is {} in French.".format (my_word, translation))
elif my_word in english_to_bulgarian_dictionary:
    print("{} is {} in Bulgarian.".format (my_word, translation2))  
else:
        print(f"{my_word} is not in this dictionary. Please try another word.") 