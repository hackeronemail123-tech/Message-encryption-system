cipher = {
    "a": "M",
    "b": "!",
    "c": "&",
    "d": "#",
    "e": "@",
    "f": "$",
    "g": "%",
    "h": "~",
    "i": "^",
    "j": "*",
    "k": "(",
    "l": ")",
    "m": "-",
    "n": "+",
    "o": "=",
    "p": "[",
    "q": "]",
    "r": "{",
    "s": "}",
    "t": "|",
    "u": ";",
    "v": ":",
    "w": "'",
    "x": "\"",
    "y": "<",
    "z": ">",
    "0": "¢",
    "1": "£",
    "2": "€",
    "3": "¥",
    "4": "§",
    "5": "¶",
    "6": "†",
    "7": "‡",
    "8": "•",
    "9": "‰",
}

reverse_cipher = {v: k for k, v in cipher.items()}

while True:
    choice = input("Encrypt [e] or Decrypt [d]: ").strip().lower()
    text = input("Enter text: ")

    if choice == "e":
        result = "".join(cipher.get(char.lower(), char) for char in text)
    elif choice == "d":
        result = "".join(reverse_cipher.get(char, char) for char in text)
    else:
        result = "Invalid choice."

    print("\nResult:")
    print(result)
    
    again = input("\nContinue? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        print("Byeeeeeeeeeee")
        break
    print()
