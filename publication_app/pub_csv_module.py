import re
import csv

text = """
homEwork:
 tHis is your homeWork, copy these Text to variable.
You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
it iS misspeLLing here. fix“iS” with correct “is”, but ONLY when it Iz a mistAKE.
last is TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


def read_txt_file(file):
    text = ''
    try:
        with open(f"{file}.txt", 'r') as file:
            file_content = file.read()
            if file_content:
                text = file_content
    except Exception as e:
        raise Exception(f"An error with opening {file} occurred: {e}")
    return text







def words_counts(file):

    text = read_txt_file(file)

    words = re.findall(r'\b\w+\b', text.lower())

    dct = dict.fromkeys(words,0)

    for k, v in dct.items():
        dct[k] = words.count(k)

    with open('file_words_counts.csv', 'w', newline='') as file:
        header = ['word', 'count']
        writer = csv.DictWriter(file, fieldnames=header, delimiter=',', quotechar="'", quoting= csv.QUOTE_MINIMAL)
        writer.writeheader()
        for key, val in dct.items():
            writer.writerow({'word' : key, 'count' : val })


def letters_counts(file):

    text = read_txt_file(file)

    letters = re.findall(r'[a-zA-Z]', text)
    letters_lower = re.findall(r'[a-zA-Z]', text.lower())

    dct = dict.fromkeys(letters_lower, {})

    for key in dct.keys():
        dct[key] = {
            'letter' : key,
            'cout_all' : letters_lower.count(key),
            'count_upper' : letters.count(key.upper()),
            'percent_upper' : str(round(letters.count(key.upper()) * 100 / letters_lower.count(key) , 1)) + '%'
        }


    with open('file_letters_counts.csv', 'w', newline='') as file:
        header = ['letter', 'cout_all', 'count_upper', 'percent_upper']
        writer = csv.DictWriter(file, fieldnames=header, delimiter=',', quotechar="'", quoting= csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(dct.values())
