def word_count(text):
    words_pairs = map(lambda w: (w, 1), text.split(' '))
    words_counts = {}
    for pair in words_pairs:
        current_word = pair[0]
        current_increment = pair[1]
        val = words_counts.get(current_word)
        if val is None:
            words_counts[current_word] = current_increment
        else:
            words_counts[current_word] += current_increment
    return words_counts


if __name__ == '__main__':
    print(word_count('hola cesar como estas hola hola'))
