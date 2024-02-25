
# function to capitalize all the words in the match, but as there is only one in first_word_re, it fits
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
    import re
    # declare a RE to capture 1st word of the sentence
    first_word_re = r'([:.!?]\s*)(\S+)'
    # capitalize every 1st word of the sentences and return edited string
    return re.sub(first_word_re, capitalize_word, txt)

# func to normalize text case
def normalize_case(txt):
    txt = txt.lower()
    txt = txt.capitalize()
    txt = capitalize_1st_words(txt)
    return txt

# func to replace word -  only word, not a part of string - with another one
def replace_word(txt, old_word, new_word):
    import re
    # a RE to capture old_word when it is a separate word and is not quoted
    word_re = fr"(?<!“)\b{old_word}\b(?!”)"
    # replace all old_word with new_words and return edited string
    return re.sub(word_re, new_word, txt)

# func to count all whitesapces in the string
def white_space_count(txt):
    import re
    # a RE to captures each single white space
    whitespace_re = r'\s'
    # count and return white spaced
    return len(re.findall(whitespace_re, txt))

# func to create list from last words in the sentences of the string
def last_words_to_list(txt):
    import re
    # a RE to capture the last word of a sentence
    last_word_re = r'\b\w+\b(?=[.!?])'
    return re.findall(last_word_re, txt)

# func to create a sentence from last words in the  sentences of the string
def last_words_to_sentence(txt, punct_mark = '.'):
    last_words_to_lst = last_words_to_list(txt)
    string = " ".join(last_words_to_lst)
    sentence = string.capitalize() + punct_mark.strip()
    return sentence



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
result_text = f"{result_text}\n\t{last_words_to_sentence(result_text, ' !')}"


print(f"Normalized text with the added sentence: \n\n{result_text}")

ws_count = white_space_count(txt)

print(f"\n\nThere are {ws_count} white spaces in the initial text.")


