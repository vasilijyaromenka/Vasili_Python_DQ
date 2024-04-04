import regex
import csv



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
    #words = regex.findall(r'\b\p{L}+\b', text.lower())
    words = regex.findall(r'\b\p{L}+-*\p{L}*\b', text.lower())
    
    dct = dict.fromkeys(words, 0)
    
    for k in dct.keys():
        dct[k] = words.count(k)

    rows = [[k,v] for k,v in dct.items()]
    
    with open('file_words_counts.csv', 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter='=', quotechar="'", quoting= csv.QUOTE_MINIMAL)
        writer.writerows(rows)
        # for key, val in dct.items():
        #     writer.writerow([key, val])



def letters_counts(file):

    text = read_txt_file(file)

    letters = [l for l in text if l.upper() != l.lower()]
    letters_lower = [l for l in text.lower() if l.upper() != l.lower()]
    letters_lower.sort()

    dct = dict.fromkeys(letters_lower, {})

    for key in dct.keys():
        dct[key] = {
            'letter' : key,
            'cout_all' : letters_lower.count(key),
            'count_upper' : letters.count(key.upper()),
            'percentage' : round(letters_lower.count(key) * 100 / len(letters), 2)
        }


    with open('file_letters_counts.csv', 'w', newline='', encoding="utf-8") as file:
        header = ['letter', 'cout_all', 'count_upper', 'percentage']
        writer = csv.DictWriter(file, fieldnames=header, delimiter=',', quotechar="'", quoting= csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(dct.values())

if __name__ == '__main__':
    letters_counts('feed')
    words_counts('feed')