def word_count(words):
    word_set = set(words)
    word_counts = {}
    for word in word_set:
        word_counts[word]=words.count(word)
    return word_counts
words = ['red','green','red','blue','red','red','green']
print(word_count(words))