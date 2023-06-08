import pandas
{"A": "Alfa", "B": "Bravo"}

data=pandas.read_csv("/Users/Asus/Desktop/tiwari python/NATO-alphabet-start/nato_phonetic_alphabet.csv")

phonetic_dict={row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_letter():
    word=input("Enter the word : ").upper()
    try:
        new_list=[phonetic_dict[letter] for letter in word]


    except KeyError as error_message :
        print(f"Sorry only letters in the alphabet please")
        generate_letter()

    else:
        print(new_list)

generate_letter()