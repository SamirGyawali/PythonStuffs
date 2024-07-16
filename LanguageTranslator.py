from googletrans import Translator

languagesOptions = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Koren",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    'la': "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

## checking the valid input code
def display_menu():
    print("Language Code        Language")
    print()
    for code, language in languagesOptions.items():
        print(f"{code} -----------> {language}")

def get_code_input():
    while True:
        try:
            print()
            user_input_code = input("Please enter the valid language code:").lower()
            print()
            if(user_input_code in languagesOptions.keys()):
                print(f"You've selected {languagesOptions[user_input_code]}")
                return user_input_code
            else:
                print("Please enter the valid index! PLS")
        except ValueError:
            print("heh! R U kidding me! Enter valid input")

display_menu()
while True:
    code = get_code_input()
    print("To exit please type exit")
    print("Enter the text you want to translate: ")

    raw_text = input()
    if raw_text == "exit":
        break
    ## Translating user input into the language using google translator

    translator = Translator()  #creating instance of the class

    translated_string = translator.translate(raw_text, dest=code)

    ## display translated language
    print()
    print(f"{languagesOptions[code]} translation = {translated_string.text}")
    print(f"Pronouncation: {translated_string.pronunciation}")
