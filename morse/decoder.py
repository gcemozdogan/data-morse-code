from morse.mapping import MORSE

# MORSE sözlüğünü ters çeviriyoruz: Morse -> harf
MORSE_REVERSE = {v: k for k, v in MORSE.items()}

def decode_word(morse_word):
    """
    Tek bir Morse kelimesini decode eder.
    Harfler arasında boşluk vardır.
    """
    letters = morse_word.split()
    decoded = ''.join(MORSE_REVERSE.get(letter, '') for letter in letters)
    return decoded

def decode(morse_text):
    """
    Morse cümlesini decode eder.
    Kelimeler arasında | vardır.
    """
    words = morse_text.split('|')
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

if __name__ == "__main__":
    # Örnek kullanım: tek kelime
    EXAMPLE_TEXT = ".- -... -.-."
    DECODED_TEXT = decode_word(EXAMPLE_TEXT)
    print(f"Decoded word '{EXAMPLE_TEXT}' to text: '{DECODED_TEXT}'")

    # Örnek kullanım: bir cümle
    EXAMPLE_TEXT = ".- -... -.-.|.- -... -.-."
    DECODED_TEXT = decode(EXAMPLE_TEXT)
    print(f"Decoded '{EXAMPLE_TEXT}' to text: '{DECODED_TEXT}'")
