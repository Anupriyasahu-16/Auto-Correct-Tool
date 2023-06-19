from spellchecker import SpellChecker

def auto_correct(word):
    spell = SpellChecker()
    
    # Find and return the corrected word
    corrected_word = spell.correction(word)
    return corrected_word

# Example usage
num_words = int(input("Enter the number of words: "))

for i in range(num_words):
    word = input(f"Enter word {i+1}: ")
    corrected_word = auto_correct(word)
    print(f"Auto-corrected word {i+1}: {corrected_word}")
