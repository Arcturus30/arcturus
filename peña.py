def is_odd_or_even():
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            print(f"{num} is Even.")
        else:
            print(f"{num} is Odd.")
    else:
        print("Invalid input! Please enter a valid number.")

def is_vowel_or_consonant():
    char = input("Enter a letter: ").lower()
    if char.isalpha() and len(char) == 1:
        if char in "aeiou":
            print(f"{char} is a Vowel.")
        else:
            print(f"{char} is a Consonant.")
    else:
        print("Invalid input! Please enter a single letter.")

def is_special_character():
    char = input("Enter a character: ")
    if not char.isalnum() and len(char) == 1:
        print(f"{char} is a Special Character.")
    else:
        print("Invalid input! Please enter a single special character.")

def combined_function():
    is_odd_or_even()
    is_vowel_or_consonant()
    is_special_character()

def main():
    while True:
        print("\nMenu:")
        print("1. Determine Odd or Even")
        print("2. Determine Vowel or Consonant")
        print("3. Determine Special Character")
        print("4. Run All Functions")
        print("Type 'STOP' to exit.")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            is_odd_or_even()
        elif choice == '2':
            is_vowel_or_consonant()
        elif choice == '3':
            is_special_character()
        elif choice == '4':
            combined_function()
        elif choice.upper() == 'STOP':
            print("Program terminated.")
            break
        else:
            print("Invalid choice! Please enter a number between 1-4 or type 'STOP'.")

if __name__ == "__main__":
    main()
