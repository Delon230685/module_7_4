class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for punct in punctuation:
                    text = text.replace(punct, ' ')
                words = text.split()
                all_words[file_name] = words
            return all_words
    def find(self, word):
        word = word.lower()
        word_place = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                place = words.index(word) + 1
            else:
                place = None
            word_place[name] = place
        return word_place

    def count(self, word):
        word = word.lower()
        word_counts = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            word_counts[name] = words.count(word)
        return word_counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего