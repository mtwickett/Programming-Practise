def word_length(*words):
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))
    word_lengths.sort()
    return (f'shortest_word: {word_lengths[0]}\nlongest word: {word_lengths[-1]}\naverage word length: {sum(word_lengths) / len(word_lengths)}')

print(word_length('jason', 'train', 'far', 'america', 'alley', 'elephant', 'gamification', 'many'))
