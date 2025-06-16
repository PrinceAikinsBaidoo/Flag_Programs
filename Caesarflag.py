def caesar_encode(text, shift=3):
    """
    Encodes text using Caesar cipher with specified shift (default 3)
    Only shifts alphabetic characters, preserves case and other characters
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            if char.isupper():
                # Shift within A-Z range
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift within a-z range
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def main():
    print("Caesar Cipher Encoder (Shift +3)")
    print("=" * 35)
    
    while True:
        # Get user input
        user_input = input("\nEnter text to encode (or 'quit' to exit): ")
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Encode the text
        encoded_text = caesar_encode(user_input)
        
        # Display results
        print(f"Original:  {user_input}")
        print(f"Encoded:   {encoded_text}")
        
        # Show character-by-character transformation
        print("\nCharacter transformation:")
        for i, char in enumerate(user_input):
            encoded_char = encoded_text[i]
            if char.isalpha():
                print(f"'{char}' -> '{encoded_char}'")
            else:
                print(f"'{char}' -> '{encoded_char}' (unchanged)")

if __name__ == "__main__":
    main()