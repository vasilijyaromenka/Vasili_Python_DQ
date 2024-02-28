import re


# function to capitalize the 1st word in the match 
def capitalize_word(match):
    start_spaces = match.group(1)
    word = match.group(2)
    # capitalize the word
    cap_word = word.capitalize()
    # concatenate the word and spaces
    result = f"{start_spaces}{cap_word}"
    return result

# func to capitalize 1st sentence words 
def capitalize_1st_words(txt):
    # declare a RE to capture 1st word of the sentence
    first_word_re = r'([:.!?]\s*)(\S+)'
    # capitalize every 1st word of the sentences and return edited string
    return re.sub(first_word_re, capitalize_word, txt)

# func to normalize text case
def normalize_case(txt):
    new_txt = txt.lower()
    new_txt = new_txt.capitalize()
    new_txt = capitalize_1st_words(new_txt)
    return new_txt

# func to replace word -  only word, not a part of the string - with another one
def replace_word(txt, old_word, new_word, ignorecase = True):
    # a RE to capture old_word when it is a separate word and is not quoted
    if ignorecase:
        word_re = re.compile(fr'(?<!“)\b{old_word}\b(?!”)', re.IGNORECASE)
    else:
        word_re = re.compile(fr'(?<!“)\b{old_word}\b(?!”)')
    # replace all old_word with new_words and return edited string
    return re.sub(word_re, new_word, txt)

# func to count all whitesapces in the string
def white_space_count(txt):
    # a RE to captures each single white space
    whitespace_re = r'\s'
    # count and return white spaced
    return len(re.findall(whitespace_re, txt))

# func to create list from last words in the sentences of the string
def last_words_to_list(txt):
    # a RE to capture the last word of a sentence
    last_word_re = r'\b\w+\b(?=[.!?])'
    return re.findall(last_word_re, txt)

# func to create a sentence from last words in the  sentences of the string
def last_words_to_sentence(txt, punct_mark = '.'):
    last_words_to_lst = last_words_to_list(txt)
    string = " ".join(last_words_to_lst) 
    sentence = string.capitalize() + punct_mark.strip()
    return sentence


# func to insert string after specifid substring
def strig_after_substring(txt, substring, str_to_insert, left_separator = ' ', ignorecase = True):
    if ignorecase:
        substring_re = re.compile(fr'{substring}', re.IGNORECASE)
    else:
        substring_re = re.compile(fr'{substring}')

    return re.sub(substring_re, fr'\g<0>{left_separator}{str_to_insert}', txt)



txt = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


# normalize text case
result_text = normalize_case(txt)

# replace iz with is
result_text = replace_word(result_text, 'iz', 'is')

# add one more sentence from last words of text sentences
result_text = strig_after_substring(result_text, 'end OF thIs ParAgrAph.', last_words_to_sentence(result_text) )

# calculate number of whitespace characters in this text
ws_count = white_space_count(txt)

print(f"Normalized text with the added sentence: \n\n{result_text}")

print(f"\n\nThere are {ws_count} white spaces in the initial text.")


