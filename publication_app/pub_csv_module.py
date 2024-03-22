import regex
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
        with open(f"{file}.txt", 'r', encoding="utf-8") as file:
            file_content = file.read()
            if file_content:
                text = file_content
    except Exception as e:
        raise Exception(f"An error with opening {file} occurred: {e}")
    return text



def words_counts(file):

    text = read_txt_file(file)
    words = regex.findall(r'\b\p{L}+\b', text.lower())
    
    dct = dict.fromkeys(words, 0)
    
    for k in dct.keys():
        dct[k] = words.count(k)

    rows = [[k,v] for k,v in dct.items()]
    
    with open('file_words_counts.csv', 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter='-', quotechar="'", quoting= csv.QUOTE_MINIMAL)
        writer.writerows(rows)
        # for key, val in dct.items():
        #     writer.writerow([key, val])



def letters_counts(file):

    text = read_txt_file(file)

    letters = [l for l in text if l.upper() != l.lower()]
    letters_lower = [l for l in text.lower() if l.upper() != l.lower()]

    dct = dict.fromkeys(letters_lower, {})

    for key in dct.keys():
        dct[key] = {
            'letter' : key,
            'cout_all' : letters_lower.count(key),
            'count_upper' : letters.count(key.upper()),
            'percent_upper' : str(round(letters.count(key.upper()) * 100 / letters_lower.count(key) , 1)) + '%'
        }


    with open('file_letters_counts.csv', 'w', newline='', encoding="utf-8") as file:
        header = ['letter', 'cout_all', 'count_upper', 'percent_upper']
        writer = csv.DictWriter(file, fieldnames=header, delimiter=',', quotechar="'", quoting= csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(dct.values())

