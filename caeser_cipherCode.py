def caesar_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            new_char_ord = ord(char) + shift
            if char.islower() and new_char_ord > ord('z'):
                new_char_ord = new_char_ord - ord('z') + ord('a') - 1
            elif char.isupper() and new_char_ord > ord('Z'):
                new_char_ord = new_char_ord - ord('Z') + ord('A') - 1
            encrypted_text.append(chr(new_char_ord))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 1 and 25. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 25.")

def main():
    text = input("Enter the text to encrypt: ")
    shift = get_valid_shift()
    encrypted_text = caesar_cipher(text, shift)
    print("Encoded text:", encrypted_text)

if __name__ == "__main__":
    main()
