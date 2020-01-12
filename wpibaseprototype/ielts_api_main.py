from ielts_main import Category
from ielts_main import Word
from ielts_main import ValueErrorLength
from ielts_main import ValueErrorType


cat = Category("first category", 100)
word1 = Word(cat.id, "advanced", "")
word2 = Word(cat.id, "best", "")
word3 = Word(cat.id, "exclusive", "")
cat.add_word(word1)
cat.add_word(word2)
cat.add_word(word3)


print("Category ID = {}".format(str(cat.get_id())))
print("Category name = '{}'".format(cat.get_name()))
print(str(cat))
print("We created {} words. {} words are available".format(cat.get_words_count(), cat.get_words_left()))
print(cat.get_word_list(), "\n")

# test the custom exceptions (category name type and length)
try:
    cat_wrong = Category(23, 100)
except ValueErrorType:
    print("Category creation failed. Wrong category name type")

try:
    cat_wrong = Category("23", 100)
except ValueErrorLength:
    print("Category creation failed. Wrong category name length")

# test the custom exception (word already existed)
# cat.add_word(word1)

