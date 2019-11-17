##########################################################################
# TASK 1. методами строк очистить текст от знаков препинания;
##########################################################################
# read text from the file
with open('hwm3text.txt', 'rt', encoding='utf-8') as text_file:
    text = text_file.read()
    text_file.close()

# remove leading and trailing characters of the string
text = text.strip()

# remove all punctuation symbols
import string
#  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
all_extra_chars = string.punctuation.__add__('0123456789«»—')

# add line breaks and tabs
all_extra_chars.__add__('\t\n\r')

# - is used in the text, keep it
all_extra_chars.replace('-', '', all_extra_chars.count('-'))
for s in all_extra_chars:
    text = text.replace(s, '', text.count(s))

print('The text without punctuation symbols:\n', text, '\n\n')
##########################################################################
# TASK 2. сформировать list со словами (split)
##########################################################################
words = text.split(' ')
# check the total amount of words in the text
print('total words count: {}'.format(len(words)))
words.sort()
print('All sorted words:\n', words)

##########################################################################
# TASK 3. привести все слова к нижнему регистру (map);
##########################################################################
print(words, '\n\n')
words_list = list(map(lambda w: w.lower(), words))

# remove all line breaks
words_list = list(map(lambda w: w.replace('\n',''), words_list))
print('All words transformed to lower case:\n', words_list)

##########################################################################
# TASK 4. получить из list пункта 3 dict, ключами которого являются слова,
# а значениями их количество появлений в
# тексте;
##########################################################################
# get all unique word list
unique_words = set(words_list)
unique_words = list(unique_words)
print('unique words count {}'.format(len(unique_words)))
print(unique_words, '\n')

# remove the first empty element from the list
unique_words = unique_words[1:]
print('unique words count after removing the first (empty) element {}'.format(len(unique_words)))
print(unique_words, '\n')

# sort unique words before forming a dictionary and write them to a file
unique_words.sort()
with open('unique_words.txt', mode='wt', encoding='utf-8') as u_words_file:
    for index, uw in enumerate(unique_words):
        uw_t = '{}. {}\n'.format(str(index+1), uw)
        u_words_file.write(uw_t)
    u_words_file.close()

# form a dictionary with unique words as keys
word_dic = {}
for word in unique_words:
    word_dic[word] = words_list.count(word)

# print the dictionary to the screen as well as to a file
print('\nDictionary of the text words:', word_dic)
with open('word_dict.txt', mode='w', encoding='utf-8') as word_dic_file:
    word_dic_file.write('{\n')
    for key, value in word_dic.items():
        str_f = '\t"{}": {}\n'.format(key, str(value))
        word_dic_file.write(str_f)
    word_dic_file.write('}')
    word_dic_file.close()

##########################################################################
# TASK 5. вывести 5 наиболее часто встречающихся слов (sort),
# вывести количество разных слов в тексте (set);
##########################################################################

from collections import Counter
word_counter = Counter(words_list)
print('\nFive words with the maximum counts:\n', word_counter.most_common(5))
##########################################################################
# from PRO
# выполнить light с условием: в пункте 2 дополнительно
# к приведению к нижнему регистру выполнить лемматизацию.
##########################################################################
# выполнена лемматизация отдельно
'''
Befor we can use modules we need install them
pip install pymorphy2
pip install pymorphy2-dicts
pip install DAWG-Python
'''
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
# get normal forms for unique word list
normal_forms = [morph.parse(i)[0].normal_form for i in unique_words] # Опять же, можно было map()

print(normal_forms)

# write both forms of words to a file
with open('words_and_normal_forms.txt', mode = 'w', encoding = 'utf-8') as forms_file:
    for i in range(len(unique_words)):
        pair = '{} -->> {}\n'.format(unique_words[i], normal_forms[i])
        forms_file.write(pair)
    forms_file.close()