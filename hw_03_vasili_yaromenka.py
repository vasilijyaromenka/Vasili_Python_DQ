import re

txt = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


# declare a RE to capture 1st word of the sentence
# ([:.!?]\s*): create a RE to capture the 1 st word after [:.!?],regardless the number of with spaces (\s*) after the symbol
# (\S+) : captures a group of 1 or more non-whitespace characters
first_word_re = r'([:.!?]\s*)(\S+)'

# a RE to capture the last word of a sentence
last_word_re = r'\b\w+\b(?=[.!?])'


# a RE to capture "iz" when it is a separate word and is not quoted
iz_re = re.compile(r'(?<!“)\biz\b(?!”)', re.IGNORECASE)

# a RE to captures aby single white space
whitespace_re = r'\s'



# 1) Implementation of the scenario with replacing Fix"iz" with Fix "iz" '
print('1) Implementation of the scenario with replacing Fix"iz" with Fix "iz" ')

# function to capitalize all the words in the match, but as there is only one in first_word_re, it fits
def capitalize_word(match):
    return match.group().title()

# convert the 1st word into capitalize and the rest into lower case
txt_fix_1 = txt.capitalize()

# it is not required in the task, but this step simplifies implementation
# since "capitalize_word" function would change 'Fix“iz”' into 'Fix“Iz”'
# see alternative version with keeping 'Fix“iz”' below
txt_fix_1 = txt_fix_1.replace('Fix“iz”'.lower(), 'fix “iz”')

# replace all 'iz' with 'is'
txt_fix_1 = re.sub(iz_re, 'is', txt_fix_1)

# capitalize every 1st word of the sentences
txt_fix_1 = re.sub(first_word_re, capitalize_word, txt_fix_1)

# count white spaced
white_space_num = len(re.findall(whitespace_re, txt_fix_1))

print(f"1st normalized version:\n\n{txt_fix_1}")
print(f"There are {white_space_num} white spaces in the text")




# 2) Implementation of the scenario with keeping Fix"iz" as is '
print('\n' + '='*100 + '\n\n2) Implementation of the scenario with keeping Fix"iz" as is ')

def capitalize_word_2 (match):
    start_spaces = match.group(1)
    word = match.group(2)
    # capitalize the word
    cap_word = word.capitalize()
    # concatenate the word and spaces
    result = f"{start_spaces}{cap_word}"

    return result


txt_fix_2 = txt.capitalize()

txt_fix_2 = re.sub(iz_re, 'is', txt_fix_2)

txt_fix_2 = re.sub(first_word_re, capitalize_word_2, txt_fix_2)

white_space_num_2 = len(re.findall(whitespace_re, txt_fix_2))

print(f"2nd fixed version:\n\n{txt_fix_2}")
print(f"There are {white_space_num_2} white spaces in the text")


# 3) Creating a sentence from last words and adding to the text
print('\n' + '='*100 + '\n\n3) Creating a sentence from last words \n')

last_words_lst = re.findall(last_word_re, txt_fix_2)
last_words_sent = ' '.join(last_words_lst).capitalize() + '.'
# and add to the end of this paragraf 
final_str = txt_fix_2.replace( "end of this paragraph.", "end of this paragraph. " + last_words_sent)

print(final_str)

