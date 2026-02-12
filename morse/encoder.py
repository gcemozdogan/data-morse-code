"""
This module provides functions to encode text into Morse code.

Functions:
- encode(text): Encodes a given text into Morse code, separating words with a pipe (|) and
  letters with a space.
- encode_word(word): Encodes a single word into Morse code, separating letters with a space.
"""

from morse.mapping import MORSE

def encode_word(word):
    """
    Encodes a single word into Morse code.
    Letters are separated by a space.
    """
    # Tek kelimeyi harf harf Morse'a çeviriyoruz
    return ' '.join(MORSE[char.upper()] for char in word if char.upper() in MORSE)


def encode(text):
    """
    Encodes the given text into Morse code.
    Words are separated by a pipe (|) and letters by a space.
    """
    # Cümleyi kelimelere ayır
    words = text.split()
    # Her kelimeyi encode_word ile çevir ve kelimeler arası | koy
    return '|'.join(encode_word(word) for word in words)


if __name__ == "__main__":
    # Örnek tek kelime
    EXAMPLE_TEXT = "abc"
    ENCODED_TEXT = encode_word(EXAMPLE_TEXT)
    print(f"Encoded word '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")

    # Örnek cümle
    EXAMPLE_TEXT = "abc ABC"
    ENCODED_TEXT = encode(EXAMPLE_TEXT)
    print(f"Encoded '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")
